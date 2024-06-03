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
from CTkMenuBar import *
class LinkEntry(ctk.CTkFrame):
    
    def __init__(self, master, current_language, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.current_submit_thread = None
        self.current_language = current_language
        custom_font =CTkFont(None,12)
        self.entry_label = ctk.CTkLabel(self,text=language_change.getStringByID(0,selected_language=self.current_language), font=custom_font)
        self.link_contents = ctk.StringVar()
        self.link_entry = ctk.CTkEntry(self,textvariable=self.link_contents, width=200,height=40, )
        

        self.select_path_to_save_to = SelectPathGrid(self,current_language=self.current_language)
        self.select_name = NameFileSelector(self,current_language=self.current_language)
        self.submit_button = ctk.CTkButton(self,text=language_change.getStringByID(2,selected_language = self.current_language) ,command=self.submit)
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
        path_to_new_image = path+f"\\{self.select_name.getEntryVal(4,self.current_language)}"
        url = self.link_contents.get()
        output = technical_functions.createCVImageFromURL(url,path_to_new_image)
        if type(output) == str:
            messagebox.showerror(language_change.getStringByID(7,self.current_language),output)
        else:
            try:
                open_image = Image.open(path_to_new_image)
                created_image = CTkImage(open_image, size=tuple((i//4 for i in open_image.size)))
                self.image_label.configure(image = created_image)
            except Exception as e:
                messagebox.showerror(language_change.getStringByID(4,selected_language=self.current_language),str(e))
            messagebox.showinfo(language_change.getStringByID(5,self.current_language),language_change.getStringByID(6,self.current_language)+path)
    def submit(self):
        
        if self.current_submit_thread is None or not self.current_submit_thread.is_alive() and self.select_name.file_name_entry_var.get():
            self.current_submit_thread = threading.Thread(target=self.submit_thread)
            self.current_submit_thread.daemon = True
            self.current_submit_thread.start()
        elif not self.select_name.file_name_entry_var.get():
            messagebox.showinfo("No name entred","Please select a file name")
        else:
            messagebox.showinfo(language_change.getStringByID(4,self.current_language),language_change.getStringByID(8,self.current_language))
            
        

        
        

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
        self.current_language = current_language
        self.explanation_label = ctk.CTkLabel(self,text=language_change.getStringByID(3,self.current_language))

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

class CustomMenu():
    def __init__(self, master,update_func, *args, **kwargs) -> None:
        self.menu = CTkMenuBar(master=master)
        self.update_func = update_func
        self.language_select = self.menu.add_cascade("Language")
        self.drop_menu_language = CustomDropdownMenu(self.language_select)
        self.drop_menu_language.add_option("English",lambda:self.updateLanguage("English"))
        self.drop_menu_language.add_option("Dutch", lambda:self.updateLanguage("Dutch"))
        self.drop_menu_language.add_option("Russian", lambda:self.updateLanguage("Russian"))
    def updateLanguage(self,new_language):
        global current_language
        self.update_func(new_language)