import tkinter as tk
from tkinter import *
import tksheet
import databases
import uimethods

class UserInterface():

    def __init__(self):        
        
        self.ui_method = uimethods.uiMethods()   
        
    def setRoot(self):
        #Initiliaze UI
        self.root = tk.Tk()
        self.root.title('Quality Books tietokantasovellus')
        self.root.geometry('800x600')
        
        self.frame = LabelFrame(self.root)
        self.frame.grid(row=0, column = 0, sticky = W+E+N+S, padx=10,pady=10)
        
        self.frame2 = LabelFrame(self.root)
        self.frame2.grid(row = 2, column = 0, sticky = W+E+N+S,padx=10, pady=10)

        self.frame3 = LabelFrame(self.root)
        self.frame3.grid(row = 3, column = 0, sticky = W+E+N+S,padx=10, pady=10)

    def MainLoop(self):
        #Keep UI running
        self.root.mainloop()     
    

    def send_login_info(self):
        #Send login info to the server and compare if it's valid
        self.data = databases.Databases()                
        
        if self.data.is_admin(self.user_name_var.get(), self.user_password_var.get()):
            self.empty_menu()
            self.full_menu()
        else:
            #only for testing
            print("something went wrong while logging") 
    
    def login_menu(self):

        #User menu before logged in

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Login", command=self.login)

        filemenu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.ui_method.showinfo_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)
      
    def full_menu(self): 
    
        #User menu after logged in to the database

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Login", command=self.login)
        filemenu.add_command(label="Lisää/Poista/Muokkaa", command=self.add_modify_update)
        filemenu.add_command(label="Kyselyt", command=self.queries)
        filemenu.add_command(label="Maksutapahtumat", command=self.payment_transactions)

        filemenu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.ui_method.showinfo_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)   
        
    def queries_menu(self):        

        #Pop menu for queries
        top = tk.Tk()
        top.title('Kyselyn tulos')     
        top.grid_columnconfigure(0, weight = 1)
        top.grid_rowconfigure(0, weight = 1)
        frame = tk.Frame(top)
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_rowconfigure(0,weight=1)             
  
        table = self.data.query_from_database(self.tkGetTitle.get(), self.tkGetAuthor.get(), self.tkGetCategory.get(), self.tkGetISBN.get(),self.tkGetPrice.get())

        sheet = tksheet.Sheet(top)

        sheet.set_sheet_data([[name for name in table[ri]] for ri in range(len(table))])  

        sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))

        sheet.grid(row = 0, column = 0, sticky = "nswe") 
  
        top.mainloop()
    
    def transactions_menu (self):

        top = tk.Tk()
        top.title('Kyselyn tulos')     
        top.grid_columnconfigure(0, weight = 1)
        top.grid_rowconfigure(0, weight = 1)
        frame = tk.Frame(top)
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_rowconfigure(0,weight=1)             
  
        table = self.data.get_payment_transactions(self.tkPayStartDate.get(),self.tkPayEndDate.get())

        sheet = tksheet.Sheet(top)

        sheet.set_sheet_data([[name for name in table[ri]] for ri in range(len(table))])  

        sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))

        sheet.grid(row = 0, column = 0, sticky = "nswe") 
  
        top.mainloop()        

    def empty_menu(self):
        #Clear UI
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

    def login(self):
        #User login UI to the sql database

        self.user_name_var = StringVar(self.root)
        self.user_password_var = StringVar(self.root)     
        
        self.ui_method.remove_widgets(self.frame, self.frame2, self.frame3)        
        
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

        #Form to add/remove/modify titles

        self.tkAddTitle = StringVar(self.root)
        self.tkAddAuthor = StringVar(self.root)
        self.tkAddISBN = StringVar(self.root)
        self.tkAddCategory = StringVar(self.root)
        self.tkAddPublisher = StringVar(self.root)
        self.tkAddLanguages = StringVar(self.root)
        self.tkAddPublishYear = StringVar(self.root)
        self.tkAddEdition = StringVar(self.root)
        self.tkAddPages = StringVar(self.root)
        self.addTypography = StringVar(self.root)
        self.addCondition = StringVar(self.root)
        self.addAmount = StringVar(self.root)
        self.addExtraInformation = StringVar(self.root)             
        self.tkAddPrice = StringVar(self.root)
        self.removetitle = StringVar(self.root)
        

        self.ui_method.remove_widgets(self.frame, self.frame2, self.frame3)   

        self.frame2.grid(row = 2, column = 0, sticky = W+E+N+S,padx=10, pady=10)         

        title_label = tk.Label(self.frame, text="Nimeke:")
        title_label.grid(row=0, column = 0, sticky=tk.W, padx=5, pady=5)

        title_entry = tk.Entry(self.frame, textvariable=self.tkAddTitle)
        title_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)

        author_label = tk.Label(self.frame, text="Tekijä:")
        author_label.grid(row=1, column = 0, sticky=tk.W, padx=5, pady=5)

        author_entry = tk.Entry(self.frame, textvariable=self.tkAddAuthor)
        author_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

        ISBN_label = tk.Label(self.frame, text="ISBN:")
        ISBN_label.grid(row=2, column = 0, sticky=tk.W, padx=5, pady=5)

        ISBN_entry = tk.Entry(self.frame, textvariable=self.tkAddISBN)
        ISBN_entry.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

        category_label = tk.Label(self.frame, text="Kategoria:")
        category_label.grid(row=3, column = 0, sticky=tk.W, padx=5, pady=5)

        category_entry = tk.Entry(self.frame, textvariable=self.tkAddCategory)
        category_entry.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

        publisher_label = tk.Label(self.frame, text="Kustantaja:")
        publisher_label.grid(row=4, column = 0, sticky=tk.W, padx=5, pady=5)

        publisher_entry = tk.Entry(self.frame, textvariable=self.tkAddPublisher)
        publisher_entry.grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)

        languages_label = tk.Label(self.frame, text="Kielet:")
        languages_label.grid(row=5, column = 0, sticky=tk.W, padx=5, pady=5)

        languages_entry = tk.Entry(self.frame, textvariable=self.tkAddLanguages)
        languages_entry.grid(row=5, column=1, sticky=tk.E, padx=5, pady=5)

        publish_year_label = tk.Label(self.frame, text="Julkaisuvuosi:")
        publish_year_label.grid(row=6, column = 0, sticky=tk.W, padx=5, pady=5)

        publish_year_entry = tk.Entry(self.frame, textvariable=self.tkAddPublishYear)
        publish_year_entry.grid(row=6, column=1, sticky=tk.E, padx=5, pady=5)

        edition_label = tk.Label(self.frame, text="Painos:")
        edition_label.grid(row=7, column = 0, sticky=tk.W, padx=5, pady=5)

        edition_entry = tk.Entry(self.frame, textvariable = self.tkAddEdition)
        edition_entry.grid(row=7, column=1, sticky=tk.E, padx=5, pady=5)

        pages_label = tk.Label(self.frame, text="Sivumäärä:")
        pages_label.grid(row=8, column = 0, sticky=tk.W, padx=5, pady=5)

        pages_entry = tk.Entry(self.frame, textvariable=self.tkAddPages)
        pages_entry.grid(row=8, column=1, sticky=tk.E, padx=5, pady=5)

        typography_label = tk.Label(self.frame, text="Painoasu:")
        typography_label.grid(row=9, column = 0, sticky=tk.W, padx=5, pady=5)

        typography_entry = tk.Entry(self.frame, textvariable=self.addTypography)
        typography_entry.grid(row=9, column=1, sticky=tk.E, padx=5, pady=5)

        condition_label = tk.Label(self.frame, text="Kuntoluokka:")
        condition_label.grid(row=10, column = 0, sticky=tk.W, padx=5, pady=5)

        condition_entry = tk.Entry(self.frame, textvariable=self.addCondition)
        condition_entry.grid(row=10, column=1, sticky=tk.E, padx=5, pady=5)

        amount_label = tk.Label(self.frame, text="Kappalemäärä:")
        amount_label.grid(row=11, column = 0, sticky=tk.W, padx=5, pady=5)

        amount_entry = tk.Entry(self.frame, textvariable=self.addAmount)
        amount_entry.grid(row=11, column=1, sticky=tk.E, padx=5, pady=5)

        extra_information_label = tk.Label(self.frame, text="Lisätiedot:")
        extra_information_label.grid(row=12, column = 0, sticky=tk.W, padx=5, pady=5)

        extra_information_entry = tk.Entry(self.frame, textvariable=self.addExtraInformation)
        extra_information_entry.grid(row=12, column=1, sticky=tk.E, padx=5, pady=5)

        price_label = tk.Label(self.frame, text="Hinta:")
        price_label.grid(row=13, column = 0, sticky=tk.W, padx=5, pady=5)

        price_entry = tk.Entry(self.frame, textvariable=self.tkAddPrice)
        price_entry.grid(row=13, column=1, sticky=tk.E, padx=5, pady=5)

        add_button = tk.Button(self.frame, text="Lisää nimeke", command=lambda: self.data.add_to_database(self.tkAddTitle.get(),self.tkAddAuthor.get(),self.tkAddISBN.get(),self.tkAddCategory.get(),self.tkAddPublisher.get(),self.tkAddLanguages.get(),self.tkAddPublishYear.get(),self.tkAddEdition.get(),self.tkAddPages.get(),self.addTypography.get(),self.addCondition.get(),self.addAmount.get(),self.addExtraInformation.get(),self.tkAddPrice.get()))
        add_button.grid(row=13, column=2, sticky=tk.E, padx=5, pady=5)        

        modify_button = tk.Button(self.frame, text="Muokkaa nimekettä")
        modify_button.grid(row=13, column=3, sticky=tk.E, padx=5, pady=5)
        
        #Remove a title entry

        title_id_label = tk.Label(self.frame2, text="Nimeke ID:")
        title_id_label.grid(row=0, column=0, padx=5, pady=5)
        
        title_id_entry = tk.Entry(self.frame2, textvariable=self.removetitle)
        title_id_entry.grid(row=0, column=1, padx=5,pady=5)

        remove_title_button = tk.Button(self.frame2, text="Poista nimeke", command= lambda: self.data.delete_title_from_books(self.removetitle.get()))
        remove_title_button.grid(row=0, column=2, sticky=tk.E, padx=5, pady=5)

    def queries(self):

        #Query UI for the book database

        self.ui_method.remove_widgets(self.frame, self.frame2, self.frame3)             

        self.tkGetTitle = StringVar(self.root)
        self.tkGetAuthor = StringVar(self.root)
        self.tkGetCategory = StringVar(self.root)
        self.tkGetISBN = StringVar(self.root)
        self.tkGetPrice = StringVar(self.root)

        #QUERY FORMS             

        optionmenu_title_label = tk.Label(self.frame, text="Nimeke:")
        optionmenu_title_label.grid(row=0,column=0, padx=(5,5),pady=0)

        optionmenu_author_label = tk.Label(self.frame, text="Tekijä:")
        optionmenu_author_label.grid(row=1,column=0, padx=(5,5),pady=0)

        optionmenu_category_label = tk.Label(self.frame, text="Kategoria:")
        optionmenu_category_label.grid(row=2,column=0, padx=(5,5),pady=0)

        optionmenu_ISBN_label = tk.Label(self.frame, text="ISBN:")
        optionmenu_ISBN_label.grid(row=3,column=0, padx=(5,5),pady=0)

        optionmenu_price_label = tk.Label(self.frame, text="Hinta:")
        optionmenu_price_label.grid(row=4,column=0, padx=(5,5),pady=0)

        options_label_startdate = tk.Label(self.frame, text="Alkupäivämäärä:")
        options_label_startdate.grid(row=5, column=0, padx=5, pady=5)

        options_label_enddate = tk.Label(self.frame, text="Loppupäivämäärä:")
        options_label_enddate.grid(row=6, column=0, padx=5,pady=5)         

        #tkvar3.set('=')
        #optionmenu_category2_criteria = ttk.OptionMenu(self.frame,tkvar3,options_categories2_criteria[0], *options_categories2_criteria)
        #optionmenu_category2_criteria.grid(row=1,column=1, padx=(5,5),pady=0)
   
        optionmenu_title_entry = tk.Entry(self.frame, width=15, textvariable=self.tkGetTitle)
        optionmenu_title_entry.grid(row=0, column=1)

        optionmenu_author_entry = tk.Entry(self.frame, width=15, textvariable=self.tkGetAuthor)
        optionmenu_author_entry.grid(row=1, column=1)

        optionmenu_category_entry = tk.Entry(self.frame, width=15, textvariable=self.tkGetCategory)
        optionmenu_category_entry.grid(row=2, column=1)

        optionmenu_ISBN_entry = tk.Entry(self.frame, width=15, textvariable=self.tkGetISBN)
        optionmenu_ISBN_entry.grid(row=3, column=1)

        optionmenu_price_entry = tk.Entry(self.frame, width=15, textvariable=self.tkGetPrice)
        optionmenu_price_entry.grid(row=4, column=1)

        optionmenu_startdate_entry = tk.Entry(self.frame, width=15)
        optionmenu_startdate_entry.grid(row=5, column=1)

        optionmenu_enddate_entry = tk.Entry(self.frame, width=15)
        optionmenu_enddate_entry.grid(row=6, column=1)

        options_search_button = tk.Button(self.frame, text="Hae tiedot", command=self.queries_menu)
        options_search_button.grid(row=6, column=2, padx=(5,5))     

        #CHECKBUTTONS

        # options_checkbutton1 = Checkbutton(self.frame, text="tekijä", onvalue = 1, offvalue = 0)
        # options_checkbutton1.select()
        # options_checkbutton1.grid(row=5, column=0, padx=(5,5), pady=5)
     

    def payment_transactions(self):
        #Add payment transactions

        self.tkPayTitleId = StringVar(self.root)
        self.tkPayPrice = StringVar(self.root)
        self.tkPayPostage = StringVar(self.root)
        self.tkPayLocation = StringVar(self.root)
        self.tkPayDate = StringVar(self.root)
        self.tkPayStartDate = StringVar(self.root)
        self.tkPayEndDate = StringVar(self.root)
        self.tkPayTransactionId = StringVar(self.root)      

        self.ui_method.remove_widgets(self.frame, self.frame2, self.frame3)       
  
        self.frame2.grid(row = 2, column = 0, sticky = W+E+N+S,padx=10, pady=10)
        self.frame3.grid(row = 3, column = 0, sticky = W+E+N+S,padx=10, pady=10)

        title_id_label = tk.Label(self.frame, text="Nimeke id:")
        title_id_label.grid(row=0, column=0, padx=5, pady=5)

        title_id_entry = tk.Entry(self.frame, textvariable=self.tkPayTitleId)
        title_id_entry.grid(row=0, column=1, padx=5,pady=5)

        price_date_label = tk.Label(self.frame, text="Hinta:")
        price_date_label.grid(row=1, column=0, padx=5, pady=5)

        price_date_entry = tk.Entry(self.frame,textvariable=self.tkPayPrice)
        price_date_entry.grid(row=1, column=1, padx=5,pady=5)

        postage_label = tk.Label(self.frame, text="Toimituskulut:")
        postage_label.grid(row=2, column=0, padx=5, pady=5)

        postage_entry = tk.Entry(self.frame,textvariable=self.tkPayPostage)
        postage_entry.grid(row=2, column=1, padx=5,pady=5)

        location_label = tk.Label(self.frame, text="Paikkakunta:")
        location_label.grid(row=3, column=0, padx=5, pady=5)

        location_entry = tk.Entry(self.frame,textvariable=self.tkPayLocation)
        location_entry.grid(row=3, column=1, padx=5,pady=5)

        payment_date_label = tk.Label(self.frame, text="Maksupvm:")
        payment_date_label.grid(row=4, column=0, padx=5, pady=5)

        payment_date_entry = tk.Entry(self.frame,textvariable=self.tkPayDate)
        payment_date_entry.grid(row=4, column=1, padx=5,pady=5)

        payment_add_button = tk.Button(self.frame, text="Lisää maksutapahtuma", command= lambda: self.data.add_payment_to_database(self.tkPayTitleId.get(), self.tkPayPrice.get(), self.tkPayPostage.get(), self.tkPayLocation.get(), self.tkPayDate.get()))
        payment_add_button.grid(row=4, column=2, padx=5, pady=5)

        payment_modify_button = tk.Button(self.frame, text="Muokkaa maksutapahtumaa")
        payment_modify_button.grid(row=4, column=3, padx=5, pady=5)        

        #Get payment transactions

        start_date_label = tk.Label(self.frame2, text="Aloitus päivämäärä:")
        start_date_label.grid(row=0, column=0, padx=5, pady=5)

        start_date_id_entry = tk.Entry(self.frame2, textvariable=self.tkPayStartDate)
        start_date_id_entry.grid(row=0, column=1, padx=5,pady=5)

        end_date_label = tk.Label(self.frame2, text="Lopetus päivämäärä:")
        end_date_label.grid(row=1, column=0, padx=5, pady=5)

        end_date_id_entry = tk.Entry(self.frame2, textvariable=self.tkPayEndDate)
        end_date_id_entry.grid(row=1, column=1, padx=5,pady=5)

        get_payments_button = tk.Button(self.frame2, text="Hae maksutapahtumat", command=self.transactions_menu)
        get_payments_button.grid(row=1, column=2, padx=5, pady=5)

        #Delete payment transactions

        transaction_id_label = tk.Label(self.frame3, text="Maksu ID:")
        transaction_id_label.grid(row=0, column=0, padx=5, pady=5)
        
        transaction_id_entry = tk.Entry(self.frame3,textvariable=self.tkPayTransactionId)
        transaction_id_entry.grid(row=0, column=1, padx=5,pady=5)

        payment_delete_button = tk.Button(self.frame3, text="Poista maksutapahtuma", command= lambda: self.data.delete_from_payments(self.tkPayTransactionId.get()))
        payment_delete_button.grid(row=0, column=2, padx=5, pady=5)

        #self.data.delete_from_payments(self.tkPayTransactionId)


#command= lambda: action(someNumber))

#command=self.get_transaction_id)
    
        
        
        
