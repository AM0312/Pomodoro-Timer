import tkinter
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
    global timer, reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN*60
    short_break_seconds = SHORT_BREAK_MIN*60
    long_break_seconds = LONG_BREAK_MIN*60
    if not reps % 2 == 0:
        countdown(work_seconds)
        timer_label.config(text="WORK")
    elif reps % 8 == 0:
        countdown(long_break_seconds)
        timer_label.config(text="LONG BREAK", fg=RED)
    else:
        countdown(short_break_seconds)
        timer_label.config(text="SHORT BREAK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps, timer
    minutes = count//60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        for i in range(reps//2):
            marks += "✔"
        checks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(
    file="C:/Users/anshm/Documents/Python Projects/Pomodoro/_tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN,
                            font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

checks = tkinter.Label(font=(
    FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW)
checks.grid(row=3, column=1)

window.mainloop()
