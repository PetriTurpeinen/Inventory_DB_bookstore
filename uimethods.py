#import userinterface
from tkinter import messagebox
import databases

class uiMethods():

    def __init__(self):

        self.data = databases.Databases()  
    
    def info_messagebox(self, message):
        info = "Info"
        messagebox.showinfo(info, message)
    
    def showinfo_about(self):
        
        #ABOUT
        
        messagebox.showinfo("About", "© 2021 Petri Turpeinen.  All rights reserved.")

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
