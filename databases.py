import psycopg2 as pg2
import userinterface


class Databases():

    def __init__(self):
        pass

    def connect_to_database(self,username,userpassword):

        UI = userinterface.UserInterface()

        conn = pg2.connect(database='kirjakauppa', user=username, password=userpassword)
        cur = conn.cursor()
        print("Connection established to database")
