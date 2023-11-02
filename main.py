from tkinter import *
import math
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
timer_seq = None
check_text = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer_seq)
    my_canvas.itemconfig(timer, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    s_break_sec = SHORT_BREAK_MIN * 60
    l_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(l_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(s_break_sec)
    else:
        timer_label.config(text="Work")
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer_seq
    global check_text
    count_min = math.floor(count / 60)
    count_sec = count % 60
    my_canvas.itemconfig(timer, text =f"{count_min}:{count_sec}")
    if count > 0:
        timer_seq = window.after(1000, countdown, count - 1)
        if count_sec == 0 or count_sec < 10:
            my_canvas.itemconfig(timer, text=f"{count_min}:0{count_sec}")
    else:
        if reps % 2 == 0:
            check_text += "✔"
            check_label.config(text=check_text)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Application")
window.config(padx=100, pady=100, bg=YELLOW)
my_pic = PhotoImage(file="tomato.png")
check_text = ""
my_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_canvas.create_image(100, 112, image=my_pic)
timer = my_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
my_canvas.grid(column=2, row=2)
check_label = Label(font=(FONT_NAME, 15), bg=YELLOW, fg=GREEN, highlightthickness=0)
check_label.grid(column=2, row=4)
timer_label = Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer_label.grid(column=2, row = 0)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column = 1, row = 3)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)
window.mainloop()