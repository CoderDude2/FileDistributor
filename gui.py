import tkinter as tk 
from tkinter import ttk
from dataclasses import dataclass

@dataclass
class Associate:
    name:str
    case_types:list[str]

class App:
    def __init__(self) -> None:
        self.root:tk.Tk = tk.Tk()
        self.root.geometry("400x300")

        file_viewer = ttk.Treeview(columns=('case_id', 'two'), show='headings')
        file_viewer.heading("case_id", text="ID")
        file_viewer.heading("two", text="Two")

        file_viewer.insert(parent='',index=tk.END, values=(1111, "Test"))

        file_viewer.pack()
        
    def new_associate(self) -> None:
        pass
    
    def run(self) -> None:
        self.root.mainloop()