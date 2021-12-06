import userinterface

def main():
    #Make an instance of userinterface class and initialize program
    UI = userinterface.UserInterface()
    UI.setRoot()
    UI.login_menu()
    UI.MainLoop()     

if __name__ == '__main__':
    main()


#TODO:
#1. Limit the character length for fields i.e Varchar(50).
#2. Add pandas to import/export csv/xlsx/ods files.
#3. Add modification for titles & payment entries.
#4. Fix printing of payment query to include title names.
#5. Remove console when executing main.py file -> pyw





