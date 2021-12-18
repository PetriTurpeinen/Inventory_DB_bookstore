from uimethods import UiMethods
from databases import Databases
import tksheet
from tkinter import *
import tkinter as tk

class UiPopUp():
    def query_ui(self, title,author,category,isbn,price):

        data = Databases()               

        #Pop menu for queries
        queryUi = tk.Tk()
        queryUi.title('Kyselyn tulos')     
        queryUi.grid_columnconfigure(0, weight = 1)
        queryUi.grid_rowconfigure(0, weight = 1)
        frame = tk.Frame(queryUi)
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_rowconfigure(0,weight=1)

        print(price)
                     
  
        table = data.query_from_database(title,author,category,isbn,price)

        sheet = tksheet.Sheet(queryUi)

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
  
        queryUi.mainloop()
    
    def transactions_menu (self,startDate,endDate):

        data = Databases()
    
        transactions_ui = tk.Tk()
        transactions_ui.title('Kyselyn tulos')     
        transactions_ui.grid_columnconfigure(0, weight = 1)
        transactions_ui.grid_rowconfigure(0, weight = 1)
        frame = tk.Frame(transactions_ui)
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_rowconfigure(0,weight=1)             
  
        table = data.get_payment_transactions(startDate, endDate)

        sheet = tksheet.Sheet(transactions_ui)

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
  
        transactions_ui.mainloop()



