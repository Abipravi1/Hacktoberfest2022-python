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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps

    window.after_cancel(timer)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    status.config(text="Timer", fg=GREEN)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        status.config(text="Break", fg=RED)
        countDown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        status.config(text="Break", fg=PINK)
        countDown(SHORT_BREAK_MIN * 60)
    else:
        status.config(text="Work", fg=GREEN)
        countDown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countDown(count):
    global reps
    global timer

    if count % 60 > 9:
        canvas.itemconfig(timer_text, text=f"{int(count / 60)}:{count % 60}")
    else:
        canvas.itemconfig(timer_text, text=f"{int(count / 60)}:0{count % 60}")

    if count > 0:
        timer = canvas.after(1000, countDown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(int(reps / 2)):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO TIMER")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pic)
timer_text = canvas.create_text(105, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

status = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
status.grid(row=0, column=1)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
check_marks.grid(row=3, column=1)

start = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
