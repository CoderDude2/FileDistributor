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
        self.root.geometry("600x300")

        file_viewer = ttk.Treeview(columns=('case_id', 'name'), show='headings')
        file_viewer.heading("case_id", text="ID")
        file_viewer.heading("name", text="Name")

        file_viewer.insert(parent='',index=tk.END, values=(6311, "PDO-PL-0406311__(NAR-CS-TA14,6311).stl"))

        file_viewer.pack(fill="x")
        
    def new_associate(self) -> None:
        pass
    
    def run(self) -> None:
        self.root.mainloop()