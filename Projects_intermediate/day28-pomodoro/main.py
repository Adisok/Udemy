from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, checks, timer
    window.after_cancel(timer)
    checks = ""
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checks = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Brake!", fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK!", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Brake!", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checks, timer

    count_mins = int(count/60)
    secs = count % 60

    if secs < 10:
        secs = "0" + str(secs)

    if count_mins == 0:
        count_mins = "00"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{secs}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += "🗸"
            check_marks.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Pomodoro")
window.minsize(width=450, height=450)
window.config(padx=100, pady=50, bg=YELLOW)

# image
tomato = PhotoImage(file="tomato.png")

# canvas
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 125, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)


# label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 26, "bold"))
timer_label.grid(row=0, column=1)

# buttons
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.config(padx=5, pady=5)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.config(padx=5, pady=5)
button_reset.grid(row=2, column=2)

# checkmarks
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
