import tkinter as tk

def calculator():
    win = tk.Toplevel()
    win.title("Calculator")

    entry = tk.Entry(win)
    entry.pack()

    def calc():
        try:
            result.config(text=eval(entry.get()))
        except:
            result.config(text="Error")

    tk.Button(win, text="Calculate", command=calc).pack()
    result = tk.Label(win, text="")
    result.pack()

def currency():
    win = tk.Toplevel()
    win.title("Currency Converter")

    entry = tk.Entry(win)
    entry.pack()

    def convert():
        result.config(text=float(entry.get()) * 1500)

    tk.Button(win, text="Convert USD to NGN", command=convert).pack()
    result = tk.Label(win, text="")
    result.pack()

def ticket():
    win = tk.Toplevel()
    win.title("Plane Ticket")

    entry = tk.Entry(win)
    entry.pack()

    def price():
        result.config(text=float(entry.get()) * 0.5)

    tk.Button(win, text="Calculate Ticket", command=price).pack()
    result = tk.Label(win, text="")
    result.pack()

root = tk.Tk()
root.title("GUI Project")

tk.Button(root, text="Calculator", command=calculator).pack(pady=5)
tk.Button(root, text="Currency Converter", command=currency).pack(pady=5)
tk.Button(root, text="Plane Ticket", command=ticket).pack(pady=5)

root.mainloop()
