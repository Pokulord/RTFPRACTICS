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
                datato_insert = None):
        with connection.cursor() as cursor:
            if query_type == "select":
                cursor.execute(f"select * from {table_to_select} ;")
                all_rows = cursor.fetchall()
                cursor.execute(f"SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name ='{table_to_select}';")
                all_columns = [index[3] for index in cursor.fetchall()]
                return [all_columns, all_rows,  "update columns"]
            
            if query_type == "insert":
                print(f" Данные для вставки : {datato_insert}")
                # data_to_query = ",".join(datato_insert[1::])
                # print(data_to_query)
                data_to_query = tuple(datato_insert)
                print(data_to_query)
                values_to_insert_template = ",".join(["%s" for i in range(len(data_to_query))])
                
                query = f"INSERT INTO {table_to_select} VALUES({values_to_insert_template}) "
                print(query)
                # print(query)
                cursor.execute(query, data_to_query)
                connection.commit()
                return "Success"

# var1 = Connect_to_DB()
# var1.connect_to_database()