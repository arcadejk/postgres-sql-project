from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

# Initialize MetaData without passing the engine (as per SQLAlchemy 2.0+)
meta = MetaData()

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),  # Corrected ForeignKey reference
    Column("MediaTypeId", Integer),
    Column("GenreId", Integer),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float),
)

# Create tables (if not already created)
meta.create_all(db)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only the "Queen" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name == "Queen"])

    # Query 4 - select only the "ArtistID" #51 column from the "Artist" table
    select_query = artist_table.select().with_only_columns([artist_table.c.ArtistID == 51])


    results = connection.execute(select_query)
    for result in results:
        print(result)
