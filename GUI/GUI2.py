# creating a frame
import tkinter as tk

def bt1_click():
    a=int(tx1.get())
    b=int(tx2.get())
    c=a+b
    label5["text"]=str(c)
    return

window = tk.Tk()

frame = tk.Frame(master=window, width=1000, height=1000,bg="cyan")
frame.pack()


label1 = tk.Label(master=frame, text="Arithmetic Application", bg="red",font='Courier')
label1.place(x=500, y=5)
label2 = tk.Label(master=frame, text="Enter First No", fg="black")
label2.place(x=400, y=50)
tx1=tk.Entry(master=frame)
tx1.place(x=500,y=50)
label3 = tk.Label(master=frame, text="Enter Second No", fg="black")
label3.place(x=400, y=100)
tx2=tk.Entry(master=frame)
tx2.place(x=500,y=100)
bt1=tk.Button(text="Add", fg="black",command=bt1_click)
bt1.place(x=500,y=200)

label4 = tk.Label(master=frame, text="Result", bg="yellow")
label4.place(x=400, y=300)
label5 = tk.Label(master=frame, text=" ", bg="yellow")
label5.place(x=500, y=300)






window.mainloop()