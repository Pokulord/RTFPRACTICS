import psycopg2
import datetime



def connect_to_database(db_host=None, 
                        db_user= None,
                        db_pass = None,
                        n_database = None):
    connection  = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "futurama3225",
        database = "Pizzeria",
        port = "5432"
    )
    print("Success")


connect_to_database()