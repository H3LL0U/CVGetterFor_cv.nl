import technical_functions
import customtkinter as ctk
import language_change
import widgets
if __name__ == "__main__":
    #Main app configuration

    current_language = "English"
    ctk.set_appearance_mode("System")
    app = ctk.CTk()
    app.minsize(400,400)
    app.title("CVGetter")


    #WIDGETS

    entry = widgets.LinkEntry(app, current_language)
    


    app.mainloop()
    




