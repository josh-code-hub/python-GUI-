import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text=f"Result: {result}")
    except:
        output.config(text="Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack()

output = tk.Label(root, text="Result:")
output.pack()

root.mainloop()
