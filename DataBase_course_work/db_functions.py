import psycopg2
import datetime




class Connect_to_DB:

    def connect_to_database(self, db_host="localhost", 
                            db_user= "postgres",
                            db_pass = "None",
                            n_database = None,
                            db_port = "5432"):             
        connection  = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = db_pass,
            database = "It_Cube",
            port = db_port
        )
        return True



# var1 = Connect_to_DB()
# var1.connect_to_database()