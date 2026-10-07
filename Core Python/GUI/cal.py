import tkinter as tk
root=tk.Tk()
root.title("Simple Calculator ")
root.geometry("500x300")
root.config(bg="black")
disply=tk.Entry(root,font=("Goudy Stout",26),bg="white" ,fg="black")
disply.pack(padx=20,pady=20,fill='x')
def click(values):
    disply.insert(tk.END,values)
def cleare():
    disply.delete(0,tk.END)
def calculate():
    try:
        result=eval(disply.get())
        disply.delete(0,tk.END)
        disply.insert(0,result)
    except:
        disply.delete(0,tk.END)
        disply.insert(0,"Errr")
frame=tk.Frame(root,bg="red")
frame.pack()
buttons=[
    ("7",0,0),
    ("8",0,1),
    ("9",0,2),
    ("/",0,3),
    
    ("4",1,0),
    ("5",1,1),
    ("6",1,2),
    ("*",1,3),
    
    ("1",2,0),
    ("2",2,1),
    ("3",2,2),
    ("-",2,3),
    
    ("0",3,0),
    (".",3,1),
    ("+",3,2)]
for text,row,column in buttons:
    if text in "+-*/":
        color="orange"
    else:
        color="gray"
    tk.Button(frame,text=text,font=("Goudy Stout",18,"bold",),bg=color,fg="white",command=lambda x=text:click(x)).grid(row=row,column=column)
    
# Clear Button
tk.Button(
    frame,
    text="C",
    font=("Arial", 18, "bold"),
    bg="red",
    fg="white",
    width=5,
    height=2,
    command=cleare
).grid(
    row=3,
    column=3,
    padx=5,
    pady=5
)


# Equal Button
tk.Button(
    root,
    text="=",
    font=("Arial", 20, "bold"),
    bg="green",
    fg="white",
    width=20,
    height=2,
    command=calculate
).pack(pady=15)
root.mainloop()
root.mainloop()
