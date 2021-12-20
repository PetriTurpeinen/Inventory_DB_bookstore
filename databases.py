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
            #print(data_queries)

            new_data_queries = []
            new_data_queries.append(data_tuple)
            for i in range(len(data_queries)):
                new_data_queries.append(data_queries[i])        
   
            #print(data)            
            
            return new_data_queries
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong."))
        finally:
            self.conn.close() 

    def add_to_database(self,title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price):

        
        #title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price
        #print(title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price)

        #lista = [title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price]
        #print(len(lista))

        try:

            self.connect_to_database()      
            
            self.cur.execute("INSERT INTO kirjat (nimeke, tekija, isbn, kategoria, kustantaja, kielet, julkaisuvuosi, painos, sivumaara, painoasu, kuntoluokka, kappalemaara, lisatiedot, hinta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING kirjat_id;",(title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price));            
            id = self.cur.fetchone()[0]
            self.conn.commit()              

            print(uimethods.UiMethods.showinfo_messagebox("","Info", f"Title id: {id} was succesfully added to the database!"))
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Info", "Something went wrong"))
        finally:
            self.conn.close()
    
    def update_title(self,title_id,title,author,isbn,category,publisher,languages,publishyear,edition,pages,typography,condition,amount,extrainformation,price):
        new_title_values = []               
        new_title_values.append(title)
        new_title_values.append(author)
        new_title_values.append(isbn)
        new_title_values.append(category)
        new_title_values.append(publisher)
        new_title_values.append(languages)
        new_title_values.append(publishyear)
        new_title_values.append(edition) 
        new_title_values.append(pages) 
        new_title_values.append(typography)
        new_title_values.append(condition) 
        new_title_values.append(amount) 
        new_title_values.append(extrainformation) 
        new_title_values.append(price)                        

        self.connect_to_database()

        try:
            self.cur.execute("SELECT nimeke, tekija, isbn, kategoria, kustantaja, kielet, julkaisuvuosi, painos, sivumaara, painoasu, kuntoluokka, kappalemaara, lisatiedot, hinta FROM kirjat WHERE kirjat_id = %s;", (title_id,));
            old_title_values = self.cur.fetchall()[0]         
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
        finally:
            self.conn.close()  

        #print(f"Length of tuple {len(old_title_values)}")
        print(old_title_values)

       

        #If field has no value, replace it with the old one
        for i in range(len(new_title_values)):
            if new_title_values[i] == "":
                new_title_values[i] = old_title_values[i]

        print(new_title_values)

        try:
            self.cur.execute("UPDATE kirjat SET nimeke = %s, tekija = %s, isbn = %s, kategoria = %s, kustantaja = %s, kielet = %s, julkaisuvuosi = %s, painos = %s,sivumaara= %s, painoasu = %s, kuntoluokka = %s, kappalemaara= %s, lisatiedot = %s, hinta = %s WHERE kirjat_id = %s;", (new_title_values[0],new_title_values[1], new_title_values[2],new_title_values[3],new_title_values[4],new_title_values[5],new_title_values[6],new_title_values[7],new_title_values[8],new_title_values[9], new_title_values[10],new_title_values[11],new_title_values[12],new_title_values[13], title_id));
            self.conn.commit()
            self.conn.close()            
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
            self.conn.close()

    def delete_title_from_books(self, title_id):
    
        self.connect_to_database()        

        #print(title_id)
        try:
            self.cur.execute("DELETE FROM kirjat WHERE kirjat_id = %s RETURNING kirjat_id;",(title_id,));

            id = self.cur.fetchone()[0]
            self.conn.commit()                

            print(uimethods.UiMethods.showinfo_messagebox("","Info", f"Title: {id} was succesfully deleted from the database"))
        except pg2.errors.InvalidTextRepresentation:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", f"{title_id} isn't a numeric value!"))
        except TypeError:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", f"Title id: {title_id} was not found from the database."))
        except pg2.errors.NumericValueOutOfRange:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Index out of range."))
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
        finally:
            self.conn.close()
    
    def add_payment_to_database(self, title_id, price, postage, location, date):
        
        self.connect_to_database()        
        try:
            self.cur.execute("INSERT INTO maksut (kirjat_id, hinta, toimituskulut, kaupunki, maksupvm) VALUES (%s, %s, %s, %s, %s) RETURNING maksut_id;",(title_id, price, postage, location, date));

            id = self.cur.fetchone()[0]
            self.conn.commit()            
            print(uimethods.UiMethods.showinfo_messagebox("","Info", f"Payment transaction: {id} was succesfully added to the database!"))
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
        self.conn.close()
        
    
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
            new_data_queries = []
            new_data_queries.append(data_tuple)
            for i in range(len(data_queries)):
                new_data_queries.append(data_queries[i])
            print(new_data_queries)                

        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
        finally:
            self.conn.close()
        
        return new_data_queries
    
    def update_payment(self, payment_id, price, postage, location, date):
        #payment_id, title_id, price, postage, location, date
        #print(payment_id)
        new_payment_values = []               
        new_payment_values.append(price)
        new_payment_values.append(postage)
        new_payment_values.append(location)
        new_payment_values.append(date)                      

        self.connect_to_database()

        try:
            self.cur.execute("SELECT hinta, toimituskulut, kaupunki, maksupvm FROM maksut WHERE maksut_id = %s;", (payment_id,));
            old_payment_values = self.cur.fetchall()[0]            
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
        finally:
            self.conn.close()  

        #Split tuple values to a list
        #old_payment_values_list = old_payment_values[0][0][1:-1].split(",")

        print(old_payment_values[3])

        #If field has no value, replace it with the old one
        for i in range(len(new_payment_values)):
            if new_payment_values[i] == "":
                new_payment_values[i] = old_payment_values[i]

        print(new_payment_values)

        #Update the row based on user input
        try:
            self.cur.execute("UPDATE maksut SET hinta = %s, toimituskulut = %s, kaupunki = %s, maksupvm = %s WHERE maksut_id = %s;", (new_payment_values[0], new_payment_values[1], 
                                                                                                                        new_payment_values[2], new_payment_values[3], payment_id));
            self.conn.commit()
            self.conn.close()            
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
        finally:
            self.conn.close()
                                  

    
    def delete_from_payments(self, payment_id):
        

        self.connect_to_database()        

        #print(payment_id)
        try:
            self.cur.execute("DELETE FROM maksut WHERE maksut_id = %s RETURNING maksut_id;",(payment_id,));
            id = self.cur.fetchone()[0]
            self.conn.commit()            
            print(uimethods.UiMethods.showinfo_messagebox("","Info", f"Payment transaction: {id} was succesfully deleted from the database"))            
        except pg2.errors.InvalidTextRepresentation:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", f"{payment_id} isn't a numeric value!"))
        except TypeError:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", f"Payment id: {payment_id} was not found from the database."))
        except pg2.errors.NumericValueOutOfRange:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Index out of range."))
        except:
            print(uimethods.UiMethods.showinfo_messagebox("","Error", "Something went wrong"))
        finally:
            self.conn.close()   
                   

