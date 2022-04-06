import sqlite3

# creating a database
conn = sqlite3.connect("Reading_info.db")

# creating a cursor
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE books (
        title text,
        author text,
        genre text,
        language text,
        page integer,
        status text )
    """)


# commit changes
conn.commit()

# close connection
conn.close()
