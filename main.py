from tkinter import *
from turtle import title

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    counter_label.config(text="")
    start_button.config(state = NORMAL) 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    start_button.config(state = DISABLED) 
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer

    min = count // 60
    sec = count % 60
        
    if sec <= 9:
        sec = f"0{sec}" 

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            text += CHECKMARK 
        counter_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas - Leinwand
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) 
photo = PhotoImage(file=r"/home/mikeb15/Development/Python_Projects/100 Days of Code/28-Pomodoro_GUI_App/tomato.png") 
canvas.create_image(101, 112, image=photo)
timer_text = canvas.create_text(101, 130, text="00:00", fill='white', font=(FONT_NAME, 45, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

counter_label =Label(text="", fg=GREEN, bg=YELLOW)
counter_label.grid(column=1, row=3)


window.mainloop()
