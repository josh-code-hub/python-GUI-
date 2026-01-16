import tkinter as tk

def ticket_price():
    distance = float(entry.get())
    price = distance * 0.5  # example rate
    result.config(text=f"Ticket Price: ${price}")

root = tk.Tk()
root.title("Plane Ticket System")

tk.Label(root, text="Distance (km)").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate Price", command=ticket_price).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()
