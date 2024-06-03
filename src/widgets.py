import customtkinter as ctk
import language_change
import technical_functions
from tkinter import messagebox
from customtkinter import CTkFont
import os
from tkinter import filedialog
import threading
from PIL import Image
from customtkinter import CTkImage
class LinkEntry(ctk.CTkFrame):
    
    def __init__(self, master, current_language, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.current_submit_thread = None
        custom_font =CTkFont(None,12)
        self.entry_label = ctk.CTkLabel(self,text=language_change.getStringByID(0,selected_language=current_language), font=custom_font)
        self.link_contents = ctk.StringVar()
        self.link_entry = ctk.CTkEntry(self,textvariable=self.link_contents, width=200,height=40, )
        

        self.select_path_to_save_to = SelectPathGrid(self,current_language=current_language)
        self.select_name = NameFileSelector(self,current_language=current_language)
        self.submit_button = ctk.CTkButton(self,text=language_change.getStringByID(2,selected_language = current_language) ,command=self.submit)
        self.image_label = ctk.CTkLabel(self,image= None, text = "")
        
        self.entry_label.pack()
        self.link_entry.pack(pady = 3)
        self.select_path_to_save_to.pack()
        self.select_name.pack()
        self.submit_button.pack(pady = 3)
        self.image_label.pack(pady=5)
        self.pack()
        
    def submit_thread(self):
        
        path = self.select_path_to_save_to.get_written_path()
        path_to_new_image = path+f"\\{self.select_name.getEntryVal()}"
        url = self.link_contents.get()
        output = technical_functions.createCVImageFromURL(url,path_to_new_image)
        if type(output) == str:
            messagebox.showerror("An error acured when trying to save your CV",output)
        else:
            try:
                open_image = Image.open(path_to_new_image)
                created_image = CTkImage(open_image, size=tuple((i//4 for i in open_image.size)))
                self.image_label.configure(image = created_image)
            except Exception as e:
                messagebox.showerror("An error acured",str(e))
            messagebox.showinfo("Success!",f"Your image has been saved to {path}")
    def submit(self):
        
        if self.current_submit_thread is None or not self.current_submit_thread.is_alive() and self.select_name.file_name_entry_var.get():
            self.current_submit_thread = threading.Thread(target=self.submit_thread)
            self.current_submit_thread.daemon = True
            self.current_submit_thread.start()
        elif not self.select_name.file_name_entry_var.get():
            messagebox.showinfo("No name entred","Please select a file name")
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

class NameFileSelector(ctk.CTkFrame):
    def __init__(self,master,current_language = "English",*args, **kwargs):
        super().__init__(master,*args,*kwargs)

        self.explanation_label = ctk.CTkLabel(self,text=language_change.getStringByID(3,current_language))

        self.main_grid = ctk.CTkFrame(self)
        
        self.file_name_entry_var = ctk.StringVar()
        self.file_name_entry_var.set("CV")
        self.file_name_entry = ctk.CTkEntry(self.main_grid,width=150, height=40, textvariable=self.file_name_entry_var)

        self.selection = (
            ".png",
            )
        self.file_extension_selector = ctk.CTkComboBox(self.main_grid,height=30,values=self.selection,command = self.resizeFunc, width=70)
        self.file_name_entry.grid(column = 0,row= 0, padx = 5)
        self.file_extension_selector.grid(column=1, row = 0)
        self.explanation_label.pack()
        self.main_grid.pack()
    def resizeFunc(self,*k):
        newLen = len(self.file_extension_selector.get())
        self.file_extension_selector.configure(width=newLen+10)
    def getEntryVal(self)-> str:
        return self.file_name_entry_var.get() + self.file_extension_selector.get()
    