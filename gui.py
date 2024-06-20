import tkinter as tk

class App:
    def __init__(self) -> None:
        self.root:tk.Tk = tk.Tk()
        self.root.geometry("300x300")
    
    def run(self) -> None:
        self.root.mainloop()