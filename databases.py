import psycopg2 as pg2
import uimethods
import os

from dotenv import load_dotenv

load_dotenv()

message = "You have succesfully logged in!"

class Databases():

    def __init__(self):
        pass      

    def connect_to_database(self):
        #Connection to postgresql database and login check     
        try:            
            self.conn = pg2.connect(database=os.environ["DB_DATABASE"], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"])
            self.cur = self.conn.cursor()            
            print("Connection established to database")
        except pg2.OperationalError:
            print(("Connection error"))
        except:
            print(("Something else went wrong!"))

    def is_admin(self,username,userpassword):        

        self.connect_to_database()        
        try:
            self.cur.execute("SELECT admin FROM users WHERE username = %s AND password = %s", (username,userpassword ));
            result = self.cur.fetchone()        

            if result is None:
                print(uimethods.UiMethods.showinfo_messagebox("","Error", "Login name or password was incorrect"))
                self.conn.close()
                return False
            else:
                print(uimethods.UiMethods.showinfo_messagebox("","Info", "You have succesfully logged in!"))
                self.conn.close()                       
                return True
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Unknown error."))         

    def query_from_database(self, title, author, category, isbn, price):
        #print(title,author,category,isbn,price)
        # A test query to get books from the database        
        self.connect_to_database()

        try:
            title = "%" + title + "%"
            author = "%" + author + "%"
            category = "%" + category + "%"
            isbn = "%" + isbn + "%"
            price = "%" + price + "%"        

            
            #Add column names to the query
            self.cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'kirjat'")

            column_names = self.cur.fetchall()
            #print(column_names)

            columns_list = []

            for tup in column_names:
                columns_list += [ tup[0] ]
            #Add columns to a tuple so it can be combined with query
            data_tuple = (*columns_list,)

            #print(data_tuple)         

            self.cur.execute("SELECT * FROM kirjat WHERE nimeke LIKE %s AND tekija LIKE %s AND kategoria LIKE %s AND isbn LIKE %s AND hinta LIKE %s ORDER BY kirjat_id ASC", (title,author,category,isbn,price));

            data_queries = self.cur.fetchall()
            self.conn.close()
            #print(data_queries)

            new_data_queries = []
            new_data_queries.append(data_tuple)
            for i in range(len(data_queries)):
                new_data_queries.append(data_queries[i])
            
            #data_queries.append(data_queries[0])
            #data_queries[0] = data_tuple

            #print(data)            
            
            return new_data_queries
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong.")) 

    def add_to_database(self,title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price):

        
        #title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price
        #print(title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price)

        #lista = [title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price]
        #print(len(lista))

        try:

            self.connect_to_database()      
            
            self.cur.execute("INSERT INTO kirjat (nimeke, tekija, isbn, kategoria, kustantaja, kielet, julkaisuvuosi, painos, sivumaara, painoasu, kuntoluokka, kappalemaara, lisatiedot, hinta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING kirjat_id;",(title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price));
            #self.cur.execute("INSERT INTO testi(nimi,ika) VALUES(%s, %s) RETURNING testi_id;", (title,author))
            id = self.cur.fetchone()[0]
            self.conn.commit()
            self.conn.close()    

            print(uimethods.UiMethods.showinfo_messagebox("","Info", f"Title id: {id} was succesfully added to the database!"))
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Info", "Something went wrong"))
    
    def add_payment_to_database(self, title_id, price, postage, location, date):
        
        self.connect_to_database()        
        try:
            self.cur.execute("INSERT INTO maksut (kirjat_id, hinta, toimituskulut, kaupunki, maksupvm) VALUES (%s, %s, %s, %s, %s) RETURNING maksut_id;",(title_id, price, postage, location, date));

            id = self.cur.fetchone()[0]
            self.conn.commit()
            self.conn.close()
            print(uimethods.UiMethods.showinfo_messagebox("","Info", f"Payment transaction: {id} was succesfully added to the database!"))
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
        
    
    def get_payment_transactions(self, startdate, enddate):        

        #Get payment transactions from the database based on startdate and enddate

        self.connect_to_database()

        try:

            self.cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'maksut'")

            column_names = self.cur.fetchall()
            #print(column_names)

            columns_list = []

            for tup in column_names:
                columns_list += [ tup[0] ]
                #Add columns to a tuple so it can be combined with query
            data_tuple = (*columns_list,)
            #print(data_tuple)

            if startdate == "" and enddate == "":
                self.cur.execute("SELECT * FROM maksut ORDER BY maksupvm;");
            elif startdate == "":
                self.cur.execute("SELECT * FROM maksut WHERE maksupvm::date <= %s ORDER BY maksupvm;",(enddate,));
            elif enddate == "":
                self.cur.execute("SELECT * FROM maksut WHERE maksupvm::date >= %s ORDER BY maksupvm;",(startdate,));
            else:
                self.cur.execute("SELECT * FROM maksut WHERE maksupvm BETWEEN %s AND %s ORDER BY maksupvm;",(startdate,enddate));

            data_queries = self.cur.fetchall()
            self.conn.close()

            new_data_queries = []
            new_data_queries.append(data_tuple)
            for i in range(len(data_queries)):
                new_data_queries.append(data_queries[i])
            #print(new_data_queries)           

            return new_data_queries
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
    
    def delete_from_payments(self, payment_id):
        

        self.connect_to_database()        

        #print(payment_id)
        try:
            self.cur.execute("DELETE FROM maksut WHERE maksut_id = %s RETURNING maksut_id;",(payment_id,));
            id = self.cur.fetchone()[0]
            self.conn.commit()
            self.conn.close()
            print(uimethods.UiMethods.showinfo_messagebox("","Info", f"Payment transaction: {id} was succesfully deleted from the database"))            
        except pg2.errors.InvalidTextRepresentation:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", f"{payment_id} isn't a numeric value!"))
        except TypeError:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", f"Payment id: {payment_id} was not found from the database."))
        except pg2.errors.NumericValueOutOfRange:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Index out of range."))
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))    
                   
    
    def delete_title_from_books(self, title_id):

        self.connect_to_database()        

        #print(title_id)
        try:
            self.cur.execute("DELETE FROM kirjat WHERE kirjat_id = %s RETURNING kirjat_id;",(title_id,));

            id = self.cur.fetchone()[0]
            self.conn.commit()
            self.conn.close()    

            print(uimethods.UiMethods.showinfo_messagebox("","Info", f"Title: {id} was succesfully deleted from the database"))
        except pg2.errors.InvalidTextRepresentation:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", f"{title_id} isn't a numeric value!"))
        except TypeError:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", f"Title id: {title_id} was not found from the database."))
        except pg2.errors.NumericValueOutOfRange:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Index out of range."))
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))

