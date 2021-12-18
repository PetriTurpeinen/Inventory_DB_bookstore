import tkinter as tk
from tkinter import *

class UserInterface():

    def __init__(self,title,resolution):        
        self.title = title
        self.resolution = resolution
        
    
    def mainLoop(self):
        self.window.mainloop()

    def setWindow(self):
        self.window = tk.Tk() 
        self.window.title(self.title)      
        self.window.geometry(self.resolution)
    
    def gridConfigure(self):
        self.window.grid_columnconfigure(0, weight = 1)
        self.window.grid_rowconfigure(0, weight = 1)

        
        
