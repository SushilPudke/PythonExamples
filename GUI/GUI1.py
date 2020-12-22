# constructing window 
import tkinter as tk
def bt1_click():
    print("Button CLicked")

    return 



window=tk.Tk()
lb1=tk.Label(text="Wel Come to Axiom TechGuru Pvt. Ltd.",fg='red',bg='blue',width=100,height=10,font="Courier")
lb1.pack()
bt1=tk.Button(text="Click Me",width=30,height=3, command=bt1_click)
bt1.pack()
tx1=tk.Entry(width=50)
tx1.pack()

window.mainloop()
