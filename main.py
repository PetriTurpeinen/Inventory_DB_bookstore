from ui_menus import UiMenus


def main():
    #Make an instance of userinterface class and initialize program
    new_ui = UiMenus("Quality Books tietokantasovellus","800x600")
    new_ui.setWindow()
    new_ui.frames()
    new_ui.login_menu()
    new_ui.login_ui()
    new_ui.mainLoop()
    

if __name__ == '__main__':
    main()


#TODO:
#1. Limit the character length for fields i.e Varchar(50).
#2. Add pandas to import/export csv/xlsx/ods files.
#3. Add modification for titles & payment entries.
#4. Fix printing of payment query to include title names.
#5. Remove console when executing main.py file -> pyw
#6. Capital letters for the column names
#7. Maximize tkinter windows by default
#8. Move data instance away from class in ui_menus.py & ui_popupo
#9. Move UI & Menus to different class
#10. Make proper error messageboxes




