# Event Driven Program

from os import name
from tkinter import *
import math
from tkinter import font
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#For testing purpose comment out the original values for using 
WORK_MIN = 1 #25
SHORT_BREAK_MIN = 1 #5
LONG_BREAK_MIN = 1 #20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    
    window.after_cancel(timer)
    tick_label = Label(bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text,text = "00:00")
    title_label.config(text="Timer",font=(FONT_NAME, 32, "bold"), bg=YELLOW,fg=GREEN)
    tick_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    #If It's the 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text= "Break", fg=RED)
    #If it's the 2nd/4th/6th rep
    if reps % 2 == 0 or reps % 4 == 0 or reps % 6 == 0:
        count_down(short_break_sec)
        title_label.config(text= "Break", fg=RED)
    #If it's the 1st/3rd/5th/7th rep
    else:
        count_down(work_sec)
        title_label.config(text= "Work", fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)    # 1.8 so floor method is used, which gives greatest value <= x
    count_sec = count % 60                # this gives me remaining seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1 )  # 1sec = 1000ms --- method resposible for looping
    else:
      timer()
      marks = ""
      work_sessions = math.floor(reps/2) 
      for _ in range(work_sessions):
          marks += "✔"
      tick_label.config(text=marks)    
# ---------------------------- UI SETUP ------------------------------- #\
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
title_label = Label(text="Timer",font=(FONT_NAME, 32, "bold"), bg=YELLOW,fg=GREEN)
title_label.grid(column=1,row=0)

# Canvas
canvas = Canvas(width=200,height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button

start_button = Button(text="Start",font=(FONT_NAME, 10, "bold"), command= timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Stop",font=(FONT_NAME, 10, "bold"), command= reset_timer)
reset_button.grid(column=2, row=2)

# Tick Label
tick_label = Label(bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=3)


window.mainloop()