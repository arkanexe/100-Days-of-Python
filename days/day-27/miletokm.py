from tkinter import *
FACTOR = 1.60934

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * FACTOR
    kilometer_result.config(text=f"{km:.2f}")

def km_to_miles():
    km = float(miles_input.get())
    miles = km / FACTOR
    kilometer_result.config(text=f"{miles:.2f}")

def perform_conversion():
    # Check if an item in the Listbox is actually selected
    try:
        selected_index = option.curselection()[0]
        selected_text = option.get(selected_index)

        if selected_text == "miles to KM":
            miles_to_km()
        else:
            km_to_miles()
    except IndexError:
        # Fallback if user clicked Calculate without highlighting an option
        kilometer_result.config(text="Select mode!")

window = Tk()
window.minsize(width=300, height=200)
window.title("Mile / KM Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Value")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="Result")
kilometer_label.grid(row=1, column=2)

# Listbox for mode selection
option = Listbox(height=2, exportselection=False)
option.insert(END, "miles to KM")
option.insert(END, "KM to miles")
option.grid(column=1, row=3, pady=10)

calculate_button = Button(text="Calculate", command=perform_conversion)
calculate_button.grid(column=1, row=2)

window.mainloop()
