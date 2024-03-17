import os
import psycopg2
from psycopg2 import OperationalError
from urllib.parse import urlparse


def check_database_connection():
    database_uri = os.getenv("DATABASE_URI")
    if database_uri is None:
        return "DATABASE_URI not found in environment variables."

    try:
        # Parse the database URI to extract the database name
        result = urlparse(database_uri)
        dbname = result.path[1:]  # Remove the leading '/'

        connection = psycopg2.connect(database_uri)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        connection.close()
        return f"Database connection successful. Connected to '{dbname}'."
    except OperationalError as e:
        return f"Database connection failed: {e}"


# Uncomment the line below to run the check (if running in an environment where the DATABASE_URI is set)
print(check_database_connection())
