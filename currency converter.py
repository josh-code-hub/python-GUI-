import tkinter as tk

def convert():
    amount = float(entry.get())
    rate = 1500  # Example: USD to NGN
    result.config(text=f"{amount * rate} NGN")

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount in USD").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Convert", command=convert).pack()
result = tk.Label(root, text="Result")
result.pack()

root.mainloop()
