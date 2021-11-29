import psycopg2 as pg2
import userinterface
import os

from dotenv import load_dotenv

load_dotenv()

class Databases():

    def __init__(self):
        #Instance of UI class
        self.UI = userinterface.UserInterface()
        

    def connect_to_database(self,username,userpassword):
        #Connection to postgresql database and login check     
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

    def query_from_database(self, title, author, category, isbn, price):
        # A test query to get books from the database        
        title = "%" + title + "%"
        author = "%" + author + "%"
        category = "%" + category + "%"
        isbn = "%" + isbn + "%"        

        with self.conn:
            #Add column names to the query
            self.cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'kirjat'")

            column_names = self.cur.fetchall()
            #print(column_names)

            columns_list = []

            for tup in column_names:
                columns_list += [ tup[0] ]
            
            data_tuple = (*columns_list,)

            #print(data_tuple)          

            #self.cur.execute("SELECT * FROM kirjat")
            self.cur.execute("SELECT * FROM kirjat WHERE nimeke LIKE %s AND tekija LIKE %s AND kategoria LIKE %s AND isbn LIKE %s AND hinta = %s", (title,author,category,isbn,price));

            data_queries = self.cur.fetchall()
            
            data_queries.append(data_queries[0])
            data_queries[0] = data_tuple

        #print(data)            
        
        return data_queries

