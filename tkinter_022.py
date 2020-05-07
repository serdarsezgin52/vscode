import tkinter as tk
from tkinter import ttk

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

# class Aplication(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widget()

#     def create_widget(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(Cilic Me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root=tk.Tk()
# app=Aplication(master=root)
# app.mainloop()