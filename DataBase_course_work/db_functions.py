import psycopg2
import datetime




class Connect_to_DB:

    def connect_to_database(self, db_host="localhost", 
                            db_user= "postgres",
                            db_pass = "None",
                            n_database = None,
                            db_port = "5432"):
        global connection             
        connection  = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = db_pass,
            database = "It_Cube",
            port = db_port
        )
        return True

    def Select_all_db_tables(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' ; ")
            return cursor.fetchall()
        
    def Queries(self, query_type,
                table_to_select = None , 
                data_to_insert = None):
        with connection.cursor() as cursor:
            if query_type == "select":
                cursor.execute(f"select * from {table_to_select} ;")
                all_rows = cursor.fetchall()
                cursor.execute(f"SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name ='{table_to_select}';")
                all_tables = cursor.fetchall()

# var1 = Connect_to_DB()
# var1.connect_to_database()