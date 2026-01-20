import tkinter as tk
from tkinter import ttk, messagebox

# Exchange rates (base: USD)
rates = {
    "USD": 1.2,
    "NGN": 1600.0,
    "EUR": 0.96,
    "GBP": 0.77,
    "JPY": 148.0
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_box.get()
        to_currency = to_currency_box.get()

        # Convert to USD first, then to target currency
        usd_amount = amount / rates[from_currency]
        converted_amount = usd_amount * rates[to_currency]

        result_label.config(
            text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create main window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x300")
window.resizable(False, False)

# Title
title_label = tk.Label(
    window, text="Currency Converter", font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

# Amount
amount_label = tk.Label(window, text="Enter Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack(pady=5)

# From currency
from_label = tk.Label(window, text="From Currency:")
from_label.pack()
from_currency_box = ttk.Combobox(window, values=list(rates.keys()), state="readonly")
from_currency_box.pack()
from_currency_box.set("USD")

# To currency
to_label = tk.Label(window, text="To Currency:")
to_label.pack()
to_currency_box = ttk.Combobox(window, values=list(rates.keys()), state="readonly")
to_currency_box.pack()
to_currency_box.set("NGN")

# Convert button
convert_button = tk.Button(
    window, text="Convert", command=convert_currency
)
convert_button.pack(pady=15)

# Result
result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run app
window.mainloop()
