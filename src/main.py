import technical_functions
import customtkinter as ctk
import language_change
import widgets
def update_pages(new_language = None):
    global current_language
    global main_page
    if new_language:
        current_language = new_language
    main_page.forget()
    main_page = widgets.LinkEntry(app,current_language)
current_language = "English"
if __name__ == "__main__":
    #Main app configuration

    
    ctk.set_appearance_mode("System")
    app = ctk.CTk()
    app.minsize(400,400)
    app.title("CVGetter")
    menu = widgets.CustomMenu(app,update_func = update_pages)



    #PAGES

    main_page = widgets.LinkEntry(app, current_language)
    


    app.mainloop()
    




