from tkinter import *

# Create the root window
root = Tk()
root.title("Calculator")
root.configure(bg="#2e3f4f")

# Add an entry widget for the display
display = Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify="right", bg="#243447", fg="white")
display.grid(row=0, column=0, columnspan=4, pady=15, padx=10, ipady=10)

# Define button click functions
def button_click(value):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, END)
        display.insert(0, "Error")

# Button styles and colours
button_config = {
    "font": ("Arial", 18),
    "width": 5,
    "height": 2,
    "relief": "raised",
    "borderwidth": 2,
}

button_colors = {
    "default": "#4e5d6c",
    "hover": "#7289a1",
    "operator": "#ff9f43",
    "clear": "#d9534f",
    "equal": "#5cb85c",
    "text": "white",
}

# Add buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    color = button_colors["default"]
    if text in ("+", "-", "*", "/"):
        color = button_colors["operator"]
    elif text == "C":
        color = button_colors["clear"]
    elif text == "=":
        color = button_colors["equal"]

    btn = Button(
        root,
        text=text,
        bg=color,
        fg=button_colors["text"],
        activebackground=button_colors["hover"],
        activeforeground="white",
        **button_config,
    )

    # Assign functions to buttons
    if text == "C":
        btn.config(command=clear_display)
    elif text == "=":
        btn.config(command=calculate)
    else:
        btn.config(command=lambda t=text: button_click(t))

    # Place buttons on the grid
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()