import tkinter as tk
from tkinter import ttk, messagebox

# Sample realistic data (can be expanded)
countries = {
    "Nigeria": {
        "Lagos": 500,
        "Abuja": 450,
        "Port Harcourt": 400
    },
    "United States": {
        "New York": 900,
        "California": 850,
        "Texas": 800
    },
    "United Kingdom": {
        "London": 950,
        "Manchester": 900
    }
}

class_multiplier = {
    "Economy": 1.0,
    "Business": 1.5,
    "First Class": 2.2
}

airport_tax = 120  # realistic airport tax

# GUI window
root = tk.Tk()
root.title("Plane Ticket Booking System")
root.geometry("500x450")

# Variables
from_country = tk.StringVar()
from_state = tk.StringVar()
to_country = tk.StringVar()
to_state = tk.StringVar()
travel_class = tk.StringVar(value="Economy")
trip_type = tk.StringVar(value="One Way")

# Functions
def update_states(event, country_var, state_box):
    state_box['values'] = list(countries[country_var.get()].keys())
    state_box.current(0)

def calculate_fare():
    try:
        base_from = countries[from_country.get()][from_state.get()]
        base_to = countries[to_country.get()][to_state.get()]

        base_fare = base_from + base_to
        class_cost = base_fare * class_multiplier[travel_class.get()]
        total = class_cost + airport_tax

        if trip_type.get() == "Round Trip":
            total *= 1.8  # round-trip discount

        messagebox.showinfo("Ticket Price",
            f"Total Ticket Cost: ${total:.2f}")

    except:
        messagebox.showerror("Error", "Please select all fields")

# Widgets
ttk.Label(root, text="Departure Country").pack(pady=5)
from_country_box = ttk.Combobox(root, textvariable=from_country, values=list(countries.keys()))
from_country_box.pack()
from_country_box.bind("<<ComboboxSelected>>",
    lambda e: update_states(e, from_country, from_state_box))

ttk.Label(root, text="Departure State").pack()
from_state_box = ttk.Combobox(root, textvariable=from_state)
from_state_box.pack()

ttk.Label(root, text="Destination Country").pack(pady=5)
to_country_box = ttk.Combobox(root, textvariable=to_country, values=list(countries.keys()))
to_country_box.pack()
to_country_box.bind("<<ComboboxSelected>>",
    lambda e: update_states(e, to_country, to_state_box))

ttk.Label(root, text="Destination State").pack()
to_state_box = ttk.Combobox(root, textvariable=to_state)
to_state_box.pack()

ttk.Label(root, text="Travel Class").pack(pady=5)
ttk.Combobox(root, textvariable=travel_class,
             values=list(class_multiplier.keys())).pack()

ttk.Label(root, text="Trip Type").pack(pady=5)
ttk.Combobox(root, textvariable=trip_type,
             values=["One Way", "Round Trip"]).pack()

ttk.Button(root, text="Calculate Ticket Price", command=calculate_fare).pack(pady=20)

root.mainloop()
