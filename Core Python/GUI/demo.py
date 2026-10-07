import tkinter as tk

r = tk.Tk()

vars = tk.IntVar()

ch1 = tk.Checkbutton(r, text="I am agree", variable=vars)
ch1.grid(row=4, column=3)

def getDta():
    print(ch1.get())

gender = tk.StringVar()

bt = tk.Button(
    r,
    text="Click me",
    command=getDta,
    bg="yellow"
)
bt.grid(row=3, column=4)

tk.Radiobutton(
    text="Male",
    value="Male",
    fg="red",
    bg="yellow",
    variable=gender
).grid(row=5, column=5)

tk.Radiobutton(
    text="Female",
    value="Female",
    fg="red",
    bg="yellow",
    variable=gender
).grid(row=6, column=5)

def showred():
    # print(gender.get())
    tk.Label(
        r,
        text="radioTEXT " + gender.get()
    ).grid(row=8, column=6)

tk.Button(
    text="check Redio",
    bg="blue",
    fg="yellow",
    font=100,
    command=showred
).grid(row=7, column=5)

r.mainloop()