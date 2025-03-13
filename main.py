import tkinter as tk

def evaluate(event):
    res.configure(text="Result: " + str(eval(entry.get())))

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root)
entry.bind("<Return>", evaluate)
entry.pack()

res = tk.Label(root)
res.pack()

root.mainloop()