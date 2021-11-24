import userinterface

def main():
    #Make an instance of UI class and initialize program
    UI = userinterface.UserInterface()
    UI.setRoot()
    UI.login_menu()
    UI.MainLoop()     

if __name__ == '__main__':
    main()




