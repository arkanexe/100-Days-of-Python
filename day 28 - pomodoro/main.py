from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Consolas"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
# ---------------------------- TIMER MECHANISM ------------------------------- #
# Keep track of paused state
is_paused = False
current_count = 0

def start_timer():
    global reps, timer, is_paused, current_count

    # If we are resuming from a pause, use the saved current_count!
    if is_paused:
        is_paused = False
        count_down(current_count)
        return

    # Otherwise, it's a brand new session start
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

def count_down(count):
    global current_count, timer
    current_count = count  # Constantly save the active second

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # ... completion logic ...

def pause_timer():
    global timer, is_paused
    if timer is not None:
        window.after_cancel(timer)  # Freeze the loop
        is_paused = True            # Mark that we are paused
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50 , bg = YELLOW)
window.title("Pomodoro")



title_label = Label(text="Timer")
title_label.config(font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset=Button(text="Reset", highlightthickness=0 ,command = reset_timer)
reset.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

pause_button = Button(text="Pause", highlightthickness=0, command=pause_timer)
pause_button.grid(row=2, column=1) # Place it wherever fits your layout

window.mainloop()
