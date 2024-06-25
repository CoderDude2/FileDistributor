import tkinter as tk 
from tkinter import ttk
from dataclasses import dataclass
import os

@dataclass
class Associate:
    name:str
    case_types:list[str]

class FileList(tk.Frame):
    def __init__(self, master=None, title:str=None, file_path:str=None) -> None:
        super().__init__(master=master)

        self.title:str = title
        self.items:tk.StringVar = tk.StringVar(value=[])
        if(file_path):
            self.items.set(value=os.listdir(file_path))

        self.filelist_label:tk.Label = tk.Label(self, text=self.title)     
        self.filelist_lb:tk.Listbox = tk.Listbox(self, listvariable=self.items, selectmode='extended')
        self.filelist_scrollbar:tk.Scrollbar = tk.Scrollbar(self)

        self.filelist_label.pack(fill="x")
        self.filelist_lb.pack(expand=1, fill="both", side="left")
        self.filelist_scrollbar.pack(fill="y", side="right", )
        self.filelist_lb.config(yscrollcommand=self.filelist_scrollbar.set)
        self.filelist_scrollbar.config(command=self.filelist_lb.yview)

class App:
    def __init__(self) -> None:
        # Window Init
        self.root:tk.Tk = tk.Tk()
        self.root.geometry("600x300")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Element Definitions
        self.DS_file_list:FileList = FileList(self.root, title="DS")
        self.ASC_file_list:FileList = FileList(self.root, title="ASC")
        self.TL_AOT_file_list:FileList = FileList(self.root, title="TL/AOT")
        
        # Layout
        self.DS_file_list.grid(row=0, column=0, sticky='ew', padx=10)
        self.ASC_file_list.grid(row=0, column=1, sticky='ew', padx=10)
        self.TL_AOT_file_list.grid(row=0, column=2, sticky='ew', padx=10)
        
    def new_associate(self) -> None:
        pass
    
    def run(self) -> None:
        self.root.mainloop()