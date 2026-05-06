import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(background="black")
window.geometry("500x300")
window.resizable(False,False)
window.title("hello world")

input_frame= ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True,)

nama_depan_label = ttk.Label(input_frame,text="ayam",compound="center")
nama_depan_label.pack(padx=10,pady=10,fill="x",expand=True,)
window.mainloop()