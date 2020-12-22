import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():

    #print(v.get())
	selection = "You selected the option " + str(v.get())
	label.config(text = selection)

tk.Label(root, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


label = tk.Label(root)
label.pack()

root.mainloop()