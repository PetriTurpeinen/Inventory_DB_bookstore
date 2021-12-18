import tkinter as tk
from tkinter import messagebox
from tkinter import *
import databases

class UiMethods():

    #Testing
    #def frame(self, uiObject):        
    #   self.frame = tk.Frame(uiObject)        

    def frames(self):
        self.frame = LabelFrame(self.window)
        self.frame.grid(row=0, column = 0, sticky = W+E+N+S, padx=10,pady=10)
        
        self.frame2 = LabelFrame(self.window)
        self.frame2.grid(row = 2, column = 0, sticky = W+E+N+S,padx=10, pady=10)

        self.frame3 = LabelFrame(self.window)
        self.frame3.grid(row = 3, column = 0, sticky = W+E+N+S,padx=10, pady=10)
    
    def send_login_info(self):
        #Send login info to the server and compare if it's valid
        self.data = databases.Databases()                
        
        if self.data.is_admin(self.user_name_var.get(), self.user_password_var.get()):
            self.empty_menu()
            self.full_menu()
        else:
            #only for testing
            print("something went wrong while logging")
    
    def remove_widgets(self, frame, frame2, frame3):
        
        #Remove widgets so objects aren't placed on top of each others 

        for widget in frame.winfo_children():
            widget.destroy()

        for widget in frame2.winfo_children():
            widget.destroy()
        
        for widget in frame3.winfo_children():
            widget.destroy()

        frame2.grid_forget()
        frame3.grid_forget()
    
    def showinfo_messagebox(self,messagetype, message):

        #Send a messagebox that takes to parameters: Type and Text     
        
        messagebox.showinfo(messagetype,message)

