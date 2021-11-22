import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import databases

class UserInterface():

    def __init__(self):
        pass
        
    def setRoot(self):
        self.root = tk.Tk()
        self.root.title('Quality Books tietokantasovellus')
        self.root.geometry('800x600')
        
        self.frame = LabelFrame(self.root)
        self.frame.grid(row=0, column = 0, sticky = W+E+N+S, padx=10,pady=10)
        
        self.frame2 = LabelFrame(self.root)
        self.frame2.grid(row = 2, column = 0, sticky = W+E+N+S,padx=10, pady=10)

    def MainLoop(self):
        self.root.mainloop()

    def remove_widgets(self):

        #Remove widgets so objects aren't placed on top of each others 

        for widget in self.frame.winfo_children():
            widget.destroy()

        for widget in self.frame2.winfo_children():
            widget.destroy()

        self.frame2.grid_forget()

    def error_messagebox(self, message):
        messagebox.showinfo("Error Message", message)

    def showinfo_about(self):
        
        #ABOUT
        
        messagebox.showinfo("About", "© 2021 Petri Turpeinen.  All rights reserved.")

    def send_login_info(self):
        data = databases.Databases()
        
        data.connect_to_database(self.user_name_var.get(), self.user_password_var.get())
      
    def create_menu(self):

        #MENU

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Login", command=self.login)
        filemenu.add_command(label="Lisää/Poista/Muokkaa", command=self.add_modify_update)
        filemenu.add_command(label="Kyselyt", command=self.queries)
        filemenu.add_command(label="Maksutapahtumat", command=self.payment_transactions)

        filemenu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.showinfo_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)

    def login(self):

        self.user_name_var = StringVar(self.root)
        self.user_password_var = StringVar(self.root)     
        
        self.remove_widgets()

        #User login to the sql database
        
        username_label = tk.Label(self.frame, text="Käyttäjätunnus:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = tk.Entry(self.frame, textvariable = self.user_name_var)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        password_label = tk.Label(self.frame, text="Salasana:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = tk.Entry(self.frame, show="*", textvariable = self.user_password_var)
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        ok_button = tk.Button(self.frame, text="Kirjaudu sisään",command=self.send_login_info)
        ok_button.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

    def add_modify_update(self):

        self.remove_widgets()    
      
       #Form to add/remove/modify titles

        price_label = tk.Label(self.frame, text="Hinta:")
        price_label.grid(row=0, column = 0, sticky=tk.W, padx=5, pady=5)

        price_entry = tk.Entry(self.frame)
        price_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)

        isbn_label = tk.Label(self.frame, text="Isbn:")
        isbn_label.grid(row=1, column = 0, sticky=tk.W, padx=5, pady=5)

        isbn_entry = tk.Entry(self.frame)
        isbn_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

        publish_year_label = tk.Label(self.frame, text="Julkaisuvuosi:")
        publish_year_label.grid(row=2, column = 0, sticky=tk.W, padx=5, pady=5)

        publish_year_entry = tk.Entry(self.frame)
        publish_year_entry.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

        amount_label = tk.Label(self.frame, text="Kappalemäärä:")
        amount_label.grid(row=3, column = 0, sticky=tk.W, padx=5, pady=5)

        amount_entry = tk.Entry(self.frame)
        amount_entry.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

        category_label = tk.Label(self.frame, text="Kategoria:")
        category_label.grid(row=4, column = 0, sticky=tk.W, padx=5, pady=5)

        category_entry = tk.Entry(self.frame)
        category_entry.grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)

        languages_label = tk.Label(self.frame, text="Kielet:")
        languages_label.grid(row=5, column = 0, sticky=tk.W, padx=5, pady=5)

        languages_entry = tk.Entry(self.frame)
        languages_entry.grid(row=5, column=1, sticky=tk.E, padx=5, pady=5)

        publisher_label = tk.Label(self.frame, text="Kustantaja:")
        publisher_label.grid(row=6, column = 0, sticky=tk.W, padx=5, pady=5)

        publisher_entry = tk.Entry(self.frame)
        publisher_entry.grid(row=6, column=1, sticky=tk.E, padx=5, pady=5)

        condition_label = tk.Label(self.frame, text="Kuntoluokka:")
        condition_label.grid(row=7, column = 0, sticky=tk.W, padx=5, pady=5)

        condition_entry = tk.Entry(self.frame)
        condition_entry.grid(row=7, column=1, sticky=tk.E, padx=5, pady=5)

        extra_information_label = tk.Label(self.frame, text="Lisätiedot:")
        extra_information_label.grid(row=8, column = 0, sticky=tk.W, padx=5, pady=5)

        extra_information_entry = tk.Entry(self.frame)
        extra_information_entry.grid(row=8, column=1, sticky=tk.E, padx=5, pady=5)

        title_label = tk.Label(self.frame, text="Nimeke:")
        title_label.grid(row=9, column = 0, sticky=tk.W, padx=5, pady=5)

        title_entry = tk.Entry(self.frame)
        title_entry.grid(row=9, column=1, sticky=tk.E, padx=5, pady=5)

        extra_information_label = tk.Label(self.frame, text="Painoasu:")
        extra_information_label.grid(row=10, column = 0, sticky=tk.W, padx=5, pady=5)

        extra_information_entry = tk.Entry(self.frame)
        extra_information_entry.grid(row=10, column=1, sticky=tk.E, padx=5, pady=5)

        extra_information_label = tk.Label(self.frame, text="Tekijä:")
        extra_information_label.grid(row=11, column = 0, sticky=tk.W, padx=5, pady=5)

        extra_information_entry = tk.Entry(self.frame)
        extra_information_entry.grid(row=11, column=1, sticky=tk.E, padx=5, pady=5)

        add_button = tk.Button(self.frame, text="Lisää nimeke")
        add_button.grid(row=11, column=2, sticky=tk.E, padx=5, pady=5)

        remove_button = tk.Button(self.frame, text="Poista nimeke")
        remove_button.grid(row=11, column=3, sticky=tk.E, padx=5, pady=5)

        modify_button = tk.Button(self.frame, text="Muokkaa nimekettä")
        modify_button.grid(row=11, column=4, sticky=tk.E, padx=5, pady=5)

    def queries(self):

        self.remove_widgets()          

        tkvar = StringVar(self.root)
        tkvar2 = StringVar(self.root)
        tkvar3 = StringVar(self.root)

        #QUERY FORMS

        options_categories = [ "Isbn","Kategoria","Kielet","Kustantaja","Kuntoluokka","Lisätiedot","Nimeke","Painoasu","Tekijä"]
        options_categories2 = [ "Hinta","Julkaisuvuosi","Kappalemäärä"]
        options_categories2_criteria = [ "=",">","<",">=","<="]

        tkvar.set('Nimeke')
        optionmenu_category = ttk.OptionMenu(self.frame,tkvar,options_categories[6], *options_categories)
        optionmenu_category.grid(row=0,column=0, padx=(5,5),pady=0)    

        tkvar2.set('hinta')
        optionmenu_category2 = ttk.OptionMenu(self.frame,tkvar2,options_categories2[0], *options_categories2)
        optionmenu_category2.grid(row=1,column=0, padx=(5,5),pady=0)

        tkvar3.set('=')
        optionmenu_category2_criteria = ttk.OptionMenu(self.frame,tkvar3,options_categories2_criteria[0], *options_categories2_criteria)
        optionmenu_category2_criteria.grid(row=1,column=1, padx=(5,5),pady=0)

        options_label_startdate = tk.Label(self.frame, text="Alkupäivämäärä:")
        options_label_startdate.grid(row=2, column=0, padx=5, pady=5)

        options_label_enddate = tk.Label(self.frame, text="Loppupäivämäärä:")
        options_label_enddate.grid(row=3, column=0, padx=5,pady=5)    

        options_entry_categories_string = tk.Entry(self.frame, width=15)
        options_entry_categories_string.grid(row=0, column=2)

        options_entry_categories_int = tk.Entry(self.frame, width=15)
        options_entry_categories_int.grid(row=1, column=2)

        options_entry_startdate = tk.Entry(self.frame, width=15)
        options_entry_startdate.grid(row=2, column=2)

        options_entry_enddate = tk.Entry(self.frame, width=15)
        options_entry_enddate.grid(row=3, column=2)

        options_search_button = tk.Button(self.frame, text="Hae tiedot")
        options_search_button.grid(row=3, column=3, padx=(5,5))

        options_checkbuttons_label = tk.Label(self.frame, text="Sarakkeet:")
        options_checkbuttons_label.grid(row = 4, column = 0,ipadx = 5, pady=10)

        #CHECKBUTTONS

        options_checkbutton1 = Checkbutton(self.frame, text="tekijä", onvalue = 1, offvalue = 0)
        options_checkbutton1.select()
        options_checkbutton1.grid(row=5, column=0, padx=(5,5), pady=5)

        options_checkbutton2 = Checkbutton(self.frame, text="isbn", onvalue = 1, offvalue = 0)
        options_checkbutton2.select()
        options_checkbutton2.grid(row=5, column=1, padx=(5,5), pady=5)

        options_checkbutton3 = Checkbutton(self.frame, text="kategoria", onvalue = 1, offvalue = 0)
        options_checkbutton3.select()
        options_checkbutton3.grid(row=5, column=2, padx=(30,5), pady=5)

        options_checkbutton4 = Checkbutton(self.frame, text="kustantaja", onvalue = 1, offvalue = 0)
        options_checkbutton4.select()
        options_checkbutton4.grid(row=5, column=3, padx=(30,5), pady=5)

        options_checkbutton5 = Checkbutton(self.frame, text="kielet", onvalue = 1, offvalue = 0)
        options_checkbutton5.select()
        options_checkbutton5.grid(row=6, column=0, padx=(5,5), pady=5)

        options_checkbutton6 = Checkbutton(self.frame, text="julkaisuvuosi", onvalue = 1, offvalue = 0)
        options_checkbutton6.select()
        options_checkbutton6.grid(row=6, column=1, padx=(50,5), pady=5)

        options_checkbutton7 = Checkbutton(self.frame, text="Nimeke", onvalue = 1, offvalue = 0)
        options_checkbutton7.select()
        options_checkbutton7.grid(row=6, column=2, padx=(22,5), pady=5)   

        options_checkbutton8 = Checkbutton(self.frame, text="painoasu", onvalue = 1, offvalue = 0)
        options_checkbutton8.select()
        options_checkbutton8.grid(row=6, column=3, padx=(20,5), pady=5)

        options_checkbutton9 = Checkbutton(self.frame, text="kuntoluokka", onvalue = 1, offvalue = 0)
        options_checkbutton9.select()
        options_checkbutton9.grid(row=7, column=0, padx=(40,5),pady=5)

        options_checkbutton10 = Checkbutton(self.frame, text="kappalemäärä", onvalue = 1, offvalue = 0)
        options_checkbutton10.select()
        options_checkbutton10.grid(row=7, column=1, padx=(55,5), pady=5)

        options_checkbutton11 = Checkbutton(self.frame, text="lisätiedot", onvalue = 1, offvalue = 0)
        options_checkbutton11.select()
        options_checkbutton11.grid(row=7, column=2, padx=(30,5), pady=5)

        options_checkbutton12 = Checkbutton(self.frame, text="hinta", onvalue = 1, offvalue = 0)
        options_checkbutton12.select()
        options_checkbutton12.grid(row=7, column=3, padx=(0,5), pady=5)

    def payment_transactions(self):

        self.remove_widgets()

        #Add payment transactions
  
        self.frame2.grid(row = 2, column = 0, sticky = W+E+N+S,padx=10, pady=10)

        nimeke_id_label = tk.Label(self.frame, text="Nimeke id:")
        nimeke_id_label.grid(row=0, column=0, padx=5, pady=5)

        nimeke_id_entry = tk.Entry(self.frame)
        nimeke_id_entry.grid(row=0, column=1, padx=5,pady=5)

        payment_date_label = tk.Label(self.frame, text="Päivämäärä:")
        payment_date_label.grid(row=1, column=0, padx=5, pady=5)

        payment_date_entry = tk.Entry(self.frame)
        payment_date_entry.grid(row=1, column=1, padx=5,pady=5)

        payment_add_button = tk.Button(self.frame, text="Lisää maksutapahtuma")
        payment_add_button.grid(row=1, column=2, padx=5, pady=5)

        payment_modify_button = tk.Button(self.frame, text="Muokkaa maksutapahtumaa")
        payment_modify_button.grid(row=1, column=3, padx=5, pady=5)

        payment_delete_button = tk.Button(self.frame, text="Poista maksutapahtuma")
        payment_delete_button.grid(row=1, column=4, padx=5, pady=5)

        #Get payment transactions

        start_date_label = tk.Label(self.frame2, text="Aloitus päivämäärä:")
        start_date_label.grid(row=0, column=0, padx=5, pady=5)

        start_date_id_entry = tk.Entry(self.frame2)
        start_date_id_entry.grid(row=0, column=1, padx=5,pady=5)

        end_date_label = tk.Label(self.frame2, text="Lopetus päivämäärä:")
        end_date_label.grid(row=1, column=0, padx=5, pady=5)

        end_date_id_entry = tk.Entry(self.frame2)
        end_date_id_entry.grid(row=1, column=1, padx=5,pady=5)

        get_payments_button = tk.Button(self.frame2, text="Hae maksutapahtumat")
        get_payments_button.grid(row=1, column=2, padx=5, pady=5)

    
        
        
        
