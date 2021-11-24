import psycopg2 as pg2
import userinterface
import os

from dotenv import load_dotenv

load_dotenv()

class Databases():

    def __init__(self):
        self.UI = userinterface.UserInterface()
        

    def connect_to_database(self,username,userpassword):        
        try:            
            self.conn = pg2.connect(database=os.environ["DB_DATABASE"], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"])
            self.cur = self.conn.cursor()            
            print("Connection established to database")
        except pg2.OperationalError:
            print(("Connection error"))
        except:
            print(("Something else went wrong!"))        
        
        self.cur.execute("SELECT admin FROM users WHERE username = %s AND password = %s", (username,userpassword ));
        result = self.cur.fetchone()        

        if result is None:
            print(self.UI.error_messagebox("Login name or password was incorrect"))
            return False
        else:
            print(self.UI.error_messagebox("You have succesfully logged in!"))           
            return True           

    def query_from_database(self):

        with self.conn:

            self.cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'kirjat'")

            column_names = self.cur.fetchall()
            #print(column_names)

            columns_list = []

            for tup in column_names:
                columns_list += [ tup[0] ]
            
            data_tuple = (*columns_list,)

            print(data_tuple)          

            self.cur.execute("SELECT * FROM kirjat")

            data_queries = self.cur.fetchall()
            
            data_queries.append(data_queries[0])
            data_queries[0] = data_tuple

        #print(data)            
        
        return data_queries

