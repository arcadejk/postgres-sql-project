import psycopg2
from psycopg2 import sql

try:
    # Connect to the "chinook" database
    connection = psycopg2.connect(
        dbname="chinook",
        user="gitpod",
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
    # cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

    # Query 4 - Select only by "ArtistId" #51 from the "Artist" table
    # cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

    # Query 5 - Select only the albums with "ArtistId" #51 from the "Album" table
    cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

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
