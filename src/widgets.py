import customtkinter as ctk
import language_change
import technical_functions
from tkinter import messagebox
from customtkinter import CTkFont
import os
from tkinter import filedialog
import threading
class LinkEntry(ctk.CTkFrame):
    
    def __init__(self, master, current_language, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.current_submit_thread = None
        custom_font =CTkFont(None,12)
        self.entry_label = ctk.CTkLabel(self,text=language_change.getStringByID(0,selected_language=current_language), font=custom_font)
        self.link_contents = ctk.StringVar()
        self.link_entry = ctk.CTkEntry(self,textvariable=self.link_contents, width=200,height=40, )
        
        #self.save_path_variable = ctk.StringVar()
        
        
        #self.save_path_variable.set(os.getcwd())
        #self.path_label = ctk.CTkLabel(self,text= language_change.getStringByID(1,selected_language=current_language), font=custom_font)
        #self.save_path = ctk.CTkEntry(self,textvariable=self.save_path_variable, width=200,height=40)
        self.select_path_to_save_to = SelectPathGrid(self,current_language=current_language)

        self.submit_button = ctk.CTkButton(self,text="Submit",command=self.submit)

        self.image_label = ctk.CTkLabel(self,image= None, text = "")
        
        self.entry_label.pack()
        self.link_entry.pack(pady = 3)
        self.select_path_to_save_to.pack()
        
        self.submit_button.pack(pady = 3)
        self.image_label.pack()
        self.pack()
        
    def submit_thread(self):

        path = self.select_path_to_save_to.get_written_path()
        url = self.link_contents.get()
        output = technical_functions.createCVImageFromURL(url,path+"\\CV.png")
        if type(output) == str:
            messagebox.showerror("An error acured when trying to save your CV",output)
        else:
            messagebox.showinfo("Success!",f"Your image has been saved to {path}")
    def submit(self):
        
        if self.current_submit_thread is None or not self.current_submit_thread.is_alive():
            self.current_submit_thread = threading.Thread(target=self.submit_thread)
            self.current_submit_thread.daemon = True
            self.current_submit_thread.start()
        else:
            messagebox.showinfo("Work in progress","Image is being saved... Please wait")
            
        

        
        

class SelectPathGrid(ctk.CTkFrame):
    def __init__(self,master,current_language = "English",*args, **kwargs):
        super().__init__(master,*args,*kwargs)
        custom_font =CTkFont(None,12)
        self.save_path_variable = ctk.StringVar()
        
        
        self.save_path_variable.set(os.getcwd())
        self.path_label = ctk.CTkLabel(self,text= language_change.getStringByID(1,selected_language=current_language), font=custom_font)
        self.grid_system = ctk.CTkFrame(self)
        self.save_path = ctk.CTkEntry(self.grid_system,textvariable=self.save_path_variable, width=170,height=40)
        self.select_path_button = ctk.CTkButton(self.grid_system,width=30 ,height = 30, text="🗎" , command= self.select_path, font = CTkFont(None,25))

        self.path_label.pack()
        self.save_path.grid(column = 0,row= 0)
        self.select_path_button.grid(column=1,row=0,padx = 0)
        self.grid_system.pack()
        


    def select_path(self):
        selected_dir = filedialog.askdirectory()
        self.save_path_variable.set(selected_dir)
    def get_written_path(self):
        return self.save_path_variable.get()
        