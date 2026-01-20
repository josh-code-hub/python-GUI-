import tkinter as tk
import math

# Main window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x520")
window.resizable(False, False)

# Entry field
expression = ""

entry = tk.Entry(
    window,
    font=("Arial", 20),
    borderwidth=5,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill="x", padx=10, pady=10)

# Function to update expression
def press(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Clear all
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Delete last character
def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Calculate result
def calculate():
    global expression
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Scientific functions
def sin():
    global expression
    result = math.sin(math.radians(float(expression)))
    clear()
    press(result)

def cos():
    global expression
    result = math.cos(math.radians(float(expression)))
    clear()
    press(result)

def tan():
    global expression
    result = math.tan(math.radians(float(expression)))
    clear()
    press(result)

def log():
    global expression
    result = math.log10(float(expression))
    clear()
    press(result)

def sqrt():
    global expression
    result = math.sqrt(float(expression))
    clear()
    press(result)

def square():
    global expression
    result = float(expression) ** 2
    clear()
    press(result)

# Button frame
btn_frame = tk.Frame(window)
btn_frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

# Create numeric buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(
            btn_frame, text=text, width=8, height=2,
            command=calculate
        ).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(
            btn_frame, text=text, width=8, height=2,
            command=lambda t=text: press(t)
        ).grid(row=row, column=col, padx=5, pady=5)

# Scientific buttons
tk.Button(btn_frame, text="C", width=8, height=2, command=clear).grid(row=5, column=0)
tk.Button(btn_frame, text="⌫", width=8, height=2, command=backspace).grid(row=5, column=1)
tk.Button(btn_frame, text="√", width=8, height=2, command=sqrt).grid(row=5, column=2)
tk.Button(btn_frame, text="x²", width=8, height=2, command=square).grid(row=5, column=3)

tk.Button(btn_frame, text="sin", width=8, height=2, command=sin).grid(row=6, column=0)
tk.Button(btn_frame, text="cos", width=8, height=2, command=cos).grid(row=6, column=1)
tk.Button(btn_frame, text="tan", width=8, height=2, command=tan).grid(row=6, column=2)
tk.Button(btn_frame, text="log", width=8, height=2, command=log).grid(row=6, column=3)

# Pi button
tk.Button(
    btn_frame, text="π", width=8, height=2,
    command=lambda: press(str(math.pi))
).grid(row=7, column=0, columnspan=4)

window.mainloop()
