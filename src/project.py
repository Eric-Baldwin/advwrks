import psycopg2
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Define connection parameters
params = {
    "dbname": os.getenv("AW_DB"),
    "user": os.getenv("AW_USER"),
    "password": os.getenv("AW_PASSWORD"),
    "host": os.getenv("AW_HOST"),
    "port": os.getenv("AW_PORT")
}

# Establish the connection
conn = psycopg2.connect(**params)

# Create a cursor object
cur = conn.cursor()

# Execute the SQL query
with open('sql_queries/emp_name.sql', 'r') as sql_file:
    cur.execute(sql_file.read())

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

# Close the cursor and connection
cur.close()
conn.close()