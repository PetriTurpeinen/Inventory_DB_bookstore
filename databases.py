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
        print(title,author,category,isbn,price)
        # A test query to get books from the database        
        title = "%" + title + "%"
        author = "%" + author + "%"
        category = "%" + category + "%"
        isbn = "%" + isbn + "%"
        price = "%" + price + "%"        

        with self.conn:
            #Add column names to the query
            self.cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'kirjat'")

            column_names = self.cur.fetchall()
            print(column_names)

            columns_list = []

            for tup in column_names:
                columns_list += [ tup[0] ]
            #Add columns to a tuple so it can be combined with query
            data_tuple = (*columns_list,)

            #print(data_tuple)         

            self.cur.execute("SELECT * FROM kirjat WHERE nimeke LIKE %s AND tekija LIKE %s AND kategoria LIKE %s AND isbn LIKE %s AND hinta LIKE %s ORDER BY kirjat_id ASC", (title,author,category,isbn,price));

            data_queries = self.cur.fetchall()
            #print(data_queries)
            
            data_queries.append(data_queries[0])
            data_queries[0] = data_tuple

        #print(data)            
        
        return data_queries

    def add_to_database(self,title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price):
        #title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price
        #print(title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price)

        #lista = [title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price]
        #print(len(lista))

        
        
        self.cur.execute("INSERT INTO kirjat (nimeke, tekija, isbn, kategoria, kustantaja, kielet, julkaisuvuosi, painos, sivumaara, painoasu, kuntoluokka, kappalemaara, lisatiedot, hinta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING kirjat_id;",(title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price));
        #self.cur.execute("INSERT INTO testi(nimi,ika) VALUES(%s, %s) RETURNING testi_id;", (title,author))
        id = self.cur.fetchone()[0]
        self.conn.commit()    

        print(self.UI.error_messagebox(f"Title id: {id} was succesfully added to the database!"))
    
    def add_payment_to_database(self, title_id, price, postage, location, date):

        self.cur.execute("INSERT INTO maksut (kirjat_id, hinta, toimituskulut, kaupunki, maksupvm) VALUES (%s, %s, %s, %s, %s) RETURNING maksut_id;",(title_id, price, postage, location, date));

        id = self.cur.fetchone()[0]
        self.conn.commit()    

        print(self.UI.error_messagebox(f"Payment transaction: {id} was succesfully added to the database!"))

        
                
            
        
        



