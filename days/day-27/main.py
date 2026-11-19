from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height=300)
window.config(padx=100, pady=200)


my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# my_label.pack()

# changing label
# my_label["text"] = "My name is AbdulRahman"
# my_label.config(text = "My name is changed")


# Buttton

def button_clicked():
    print("i got clicked!")
    my_label.config(text=f"{entry.get()}")

button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="New Me!", command=button_clicked)
button.grid(column=3, row=0)

# Entry
entry = Entry(width=10)
entry.insert(END, string="Some text goes here.")
entry.grid(column=2, row=3)


# text area


# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "what goes here.")
# print(text.get("1.0", END))
# text.pack()

# # SpinBox
# def spinbox_used():
#     print(spinbox.get())

# spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox_used)
# spinbox.pack()

# def scale_used(value):
#     print(value)

# scale = Scale(from_=0, to=100, command=scale_used)

# scale.pack()

# # checkbox

# def checkbox_usd():
#     print(checkbox_state.get())

# checkbox_state = IntVar()
# check_button = Checkbutton(text="Is On?" ,variable=checkbox_state, command=checkbox_usd)

# check_button.pack()

# def radio_used():
#     print(radio_state.get())

# radio_state = IntVar()
# radio1 = Radiobutton(text="option 1", variable=radio_state, command=radio_used, value=1)
# radio2 = Radiobutton(text="option 2", variable=radio_state, command=radio_used, value=2)
# radio1.pack()
# radio2.pack()

# def show_selected(event):
#     print(listbox.get(listbox.curselection()))


# listbox = Listbox(height=4)
# listbox.insert(END, "Python")
# listbox.insert(END, "Java")
# listbox.insert(END, "C++")
# listbox.pack()
# listbox.bind("<<ListboxSelect>>", show_selected)
window.mainloop()
