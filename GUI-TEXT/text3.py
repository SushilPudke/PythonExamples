import tkinter as tk

root = tk.Tk()

text1 = tk.Text(root, height=50, width=70)
photo = tk.PhotoImage(file='Ax1.png')
text1.insert(tk.END, '\n')
text1.image_create(tk.END, image=photo)

text1.pack(side=tk.LEFT)

text2 = tk.Text(root, height=100, width=200)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',
                    foreground='#476042',
                    font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow',
               '<1>',
               lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
text2.insert(tk.END,'\nAxiom TechGuru Pvt.Ltd.\n', 'big')
quote = """
IT Solutions , By IT Masters.
IT Park , Nagpur.-22
"""
text2.insert(tk.END, quote, 'color')
text2.insert(tk.END, 'follow-up\n', 'follow')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()