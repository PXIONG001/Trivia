import psycopg2
from config import config

def insert_data(id, name, password):
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO users("ID", "Name", "Password") VALUES (%s,%s,%s)"""
        record_to_insert = (9, 'One Plus 6', 'Seven')
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

