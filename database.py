import psycopg2
from Insert_NewUser import insert_data
from Fetch_User import fetch_user

def database(user_sign):
    """ Chooses which procedure to proceed with the database """
    
    if user_sign == 'nu':
        insert_data()

    elif user_sign == 'u':
        fetch_user()

if __name__ == '__main__':
    database('nu')