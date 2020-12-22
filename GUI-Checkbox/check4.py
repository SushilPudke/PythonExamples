#Checkbox Using Application  
import tkinter as tk  
from tkinter import ttk  
win = tk.Tk()  
win.title("Python GUI App")  
#Label Creation  
ttk.Label(win, text="Checkbox status :").grid(column=0,row=0)  
#Create three Checkbox  
#Disabled Checkbox  
chVarDis=tk.IntVar()  
check1=tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')  
check1.select()  
check1.grid(column=0,row=4, sticky=tk.W)  
#Deselected Checkbox  
chVarUn=tk.IntVar()  
check2=tk.Checkbutton(win, text="UnChecked", variable=chVarUn)  
check2.deselect()  
check2.grid(column=1,row=4, sticky=tk.W)  
#Selected Checkbox  
chVarEn=tk.IntVar()  
check3=tk.Checkbutton(win, text="Enabled", variable=chVarEn)  
check3.select()  
check3.grid(column=2,row=4, sticky=tk.W)  
#Calling Main()  
win.mainloop()  