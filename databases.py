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
            conn = pg2.connect(database=os.environ["DB_DATABASE"], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"])
            self.cur = conn.cursor()            
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
            print(self.UI.error_messagebox("User and password were right"))           
            return True           

    def query_from_database(self):        

        self.cur.execute('SELECT * FROM kirjat')

        data = self.cur.fetchmany(10)
        print(data)
