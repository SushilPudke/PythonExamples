# python program demonstrating 
# Combobox widget using tkinter 


import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
# Creating tkinter window 
window = tk.Tk() 
window.title('Combobox') 
window.geometry('500x250') 

def choseEntry(entry):
    print( 'You chose "%s"' % monthchoosen.get())
    messagebox.showinfo(title="Selected Month", message=monthchoosen.get())
    
   
# label text for title 
ttk.Label(window, text = "Axiom TechGuru Pvt. Ltd.", 
		background = 'green', foreground ="white", 
		font = ("Times New Roman", 15)).grid(row = 0, column = 1) 

# label 
ttk.Label(window, text = "Select the Month :", 
		font = ("Times New Roman", 10)).grid(column = 0, 
		row = 5, padx = 10, pady = 25) 


# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 

# Adding combobox drop down list 
monthchoosen['values'] = (' January', 
						' February', 
						' March', 
						' April', 
						' May', 
						' June', 
						' July', 
						' August', 
						' September', 
						' October', 
						' November', 
						' December') 

monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current()
monthchoosen.bind("<<ComboboxSelected>>", choseEntry)
window.mainloop() 
