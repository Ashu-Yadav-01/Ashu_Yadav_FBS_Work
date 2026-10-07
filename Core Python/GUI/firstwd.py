import tkinter as tk

root = tk.Tk()
root.geometry("600x300")
root.title("My first Tkinter Project")

# lab1 = tk.Label(root, text="This is my first GUI Program")
# lab2 = tk.Label(root, text="I am label 2")

up = tk.Label(root, text="Top")
bot = tk.Label(root, text="Bottom", bg="red", fg="blue")
left = tk.Label(root, text="Left")
right = tk.Label(root, text="Right", bg="red", fg="Blue")

# up.pack(side="top", padx=12, pady=32, fill="x")
# bot.pack(side="bottom")
# left.pack(side="left")
# right.pack(side="right")

# up.grid(row=0, column=1)
# right.grid(row=1, column=2)

#up.grid(row=1, column=1)
#right.grid(row=1, column=2)
#left.grid(row=2, column=1)
#bot.grid(row=2, column=2)
#def hi():
 #   print("Button click")
#btn=tk.Button(root,text="Click me",command=hi, bg="yellow",fg="blue" font=1122).pack(side="bo",padx=) 
#btn=tk.Button(root,text="Click me2", command=hi, bg="yellow",)

ent=tk.Entry(bg="yellow")
ent.insert("Enter the name= ")
ent.pack()
root.mainloop()