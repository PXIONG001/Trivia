import psycopg2
from config import config

def database(user_sign):
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        postgres_insert_query = """ SELECT * FROM users;"""
        cursor.execute(postgres_insert_query)

        result = cursor.fetchall()
        print(result)
        connection.commit()

        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch record from users table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == '__main__':
    fetch_user('Penguin')