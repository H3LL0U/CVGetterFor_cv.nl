import customtkinter as ctk
import language_change
import technical_functions
from tkinter import messagebox
from customtkinter import CTkFont
import os
class LinkEntry(ctk.CTkFrame):
    
    def __init__(self, master, current_language, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        custom_font =CTkFont(None,12)
        self.entry_label = ctk.CTkLabel(self,text=language_change.getStringByID(0,selected_language=current_language), font=custom_font)
        self.link_contents = ctk.StringVar()
        self.link_entry = ctk.CTkEntry(self,textvariable=self.link_contents, width=200,height=40, )
        self.save_path_variable = ctk.StringVar()
        self.save_path_variable.set(os.getcwd())
        self.path_label = ctk.CTkLabel(self,text= language_change.getStringByID(1,selected_language=current_language), font=custom_font)
        self.save_path = ctk.CTkEntry(self,textvariable=self.save_path_variable, width=200,height=40)

        self.submit_button = ctk.CTkButton(self,text="Submit",command=self.submit)

        self.image_label = ctk.CTkLabel(self,image= None, text = "")
        
        self.entry_label.pack()
        self.link_entry.pack(pady = 3)
        self.path_label.pack()
        self.save_path.pack(pady = 3)
        
        self.submit_button.pack(pady = 3)
        self.image_label.pack()
        self.pack()
        
    def submit(self):
        path = self.save_path_variable.get()
        url = self.link_contents.get()
        output = technical_functions.createCVImageFromURL(url,path)
        if type(output) == str:
            messagebox.showerror("An error acured when trying to save your CV",output)
        else:
            messagebox.showinfo("Success!",f"Your image has been saved to {path}")

        
        

    