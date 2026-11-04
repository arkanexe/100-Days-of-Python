from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Consolas"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50 , bg = YELLOW)
window.title("Pomodoro")



heading = Label(text="Timer")
heading.config(font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
heading.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image = tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white",font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start = Button(text="Start", highlightthickness=0)
start.grid(row=2, column=0)

reset=Button(text="Reset", highlightthickness=0)
reset.grid(column=2, row=2)
 
checkmark = Label(text="✔")
checkmark.config(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
