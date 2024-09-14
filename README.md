####BUG FIX 

## Error = **foreign key violations**
The errors you're encountering indicate that there are **foreign key violations** in the `PlaylistTrack` table. Specifically, some `TrackId` values that you're trying to insert into the `PlaylistTrack` table do not exist in the `Track` table. This is a common issue when data is inserted in the wrong order or if the `Track` table hasn't been fully populated before trying to insert records into `PlaylistTrack`.

Here’s how to resolve this:

### Steps to Fix Foreign Key Violations:

1. **Check the `Track` Table**:
   First, check if the `Track` table has been fully populated. Run the following query to verify the presence of data in the `Track` table:

   ```sql
   SELECT * FROM "Track" WHERE "TrackId" IN (1984, 1942, 1945);
   ```

   If these records do not exist in the `Track` table, it means the `Track` table was not fully loaded before the `PlaylistTrack` inserts.

2. **Ensure the Correct Order of Insertion**:
   The tables must be populated in a specific order to respect foreign key constraints. Typically, you should insert data into the referenced tables (`Track`, `Playlist`, etc.) before inserting into the referencing tables (`PlaylistTrack`).

   - Ensure that all the data for the `Track` table is inserted first.
   - After confirming that the `Track` table is fully populated, you can insert data into `PlaylistTrack`.

3. **Fix the Data Load:**
   You may need to reload the `Chinook_PostgreSql.sql` file, but ensure the order of inserts is correct:

   - First, insert records into `Track`.
   - Then, insert records into `PlaylistTrack`.

   If the SQL file is pre-ordered but is still throwing errors, you might want to **temporarily disable foreign key constraints**, insert the data, and then re-enable the constraints:

   ```sql
   -- Disable foreign key checks
   SET session_replication_role = 'replica';

   -- Reload the SQL file
   \i /path/to/Chinook_PostgreSql.sql

   -- Re-enable foreign key checks
   SET session_replication_role = 'origin';
   ```

   **Warning**: Disabling foreign key checks can allow inconsistent data to be inserted, so make sure the data is accurate before re-enabling them.

4. **Manually Insert Missing Tracks** (if necessary):
   If specific `TrackId` values are missing, you can manually insert those records into the `Track` table:

   ```sql
   INSERT INTO "Track" ("TrackId", "Name", "AlbumId", "MediaTypeId", "GenreId", "Composer", "Milliseconds", "Bytes", "UnitPrice")
   VALUES (1984, 'Track Name', 1, 1, 1, 'Composer Name', 300000, 5000000, 0.99);
   ```

   After inserting the missing tracks, retry inserting the records into `PlaylistTrack`.

By following these steps, you should be able to resolve the foreign key violations and successfully load the Chinook database. Let me know how it goes!

###Commands
\copy (select * FROM "Track" Where "Composer" = 'Queen') TO 'test.csv' WITH CSV DELIMITER ',' HEADER;
\o test.json
SELECT json_agg(t) FROM (SELECT * FROM "Track" WHERE "Composer" = 'Queen') t;


### Fix sql-psycopg2.py

Sure! Here's your updated Python code with the ability to switch between different queries by uncommenting the relevant section:

```python
import psycopg2
from psycopg2 import sql

try:
    # Connect to the "chinook" database
    connection = psycopg2.connect(
        dbname="chinook",
        user="your_username",
        password="your_password",
        host="localhost",  # or your database host
        port="5432"        # or your database port
    )

    # Build a cursor object
    cursor = connection.cursor()

    # Uncomment the query you want to test

    # Query 1 - Select all records from the "Artist" table
    # cursor.execute('SELECT * FROM "Artist"')

    # Query 2 - Select only the "Name" column from the "Artist" table
    # cursor.execute('SELECT "Name" FROM "Artist"')

    # Query 3 - Select only "Queen" from the "Artist" table
    cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

    # Query 4 - Select only by "ArtistId" #51 from the "Artist" table
    # cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

    # Query 5 - Select only the albums with "ArtistId" #51 from the "Album" table
    # cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

    # Query 6 - Select all tracks where the composer is "Queen" from the "Track" table
    # cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

    # Fetch the results (multiple)
    results = cursor.fetchall()

    # Fetch the result (single)
    # results = cursor.fetchone()

    # Print results
    for result in results:
        print(result)

except psycopg2.Error as e:
    print(f"Database error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
```

### Instructions:
1. **Replace** `"your_username"` and `"your_password"` with your PostgreSQL credentials.
2. **Uncomment** the query you want to run by removing the `#` at the start of the relevant `cursor.execute()` line.
3. **Run** the script to execute the selected query and print the results.

Feel free to modify the script as needed for your use case!