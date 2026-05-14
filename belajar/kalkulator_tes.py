import tkinter as tk
from tkinter import ttk

apk = tk.Tk()
apk.configure(background="black",borderwidth=3)
apk.geometry("300x400")
apk.resizable(False,False)
apk.title("kalkulator")

def delete ():
    print("delete")
    
def ac () :
    pass

input_frame=ttk.Frame()
input_frame.pack(padx=20,pady=20,expand=True,fill="both")

output_hasil=ttk.Label(input_frame,text="0",borderwidth='500m',relief="raised",anchor="se",)
output_hasil.pack(padx=10,pady=10,expand=0,fill="x")

delete_fun=ttk.Button(input_frame,text="⌫",command=delete)
delete_fun.pack(padx=5,pady=5,anchor="se",)

ac_fun=ttk.Button(input_frame,text="AC",command=ac)
ac_fun.pack(padx=5,pady=5,anchor="se")



apk.mainloop()