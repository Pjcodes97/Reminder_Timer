from tkinter import *
from tkinter import *
from time import *

#Creates global variables to change and adjust
countdown = False
second = 0 
minute = 0
hour = 0

#Creating clock function
def clock_timer():
    string = strftime("%H:%M:%S %p")
    clock.config(text = string)
    clock.after(1000, clock_timer)

#Creates timer leading up the "alarm"
def countdown():
    global second, minute, hour
    second += 1
    if second == 60:
        minute = 1 
        second = 0
        if minute == 60:
            hour = 1
            minute = 0
    timer.config(text=f"{hour}:{minute}:{second}")
    timer.after(1000, countdown)

root = Tk()
root.title("Stand Up and Stretch")
root.geometry("500x500")

#Creating a regular clock to keep track of time in general
clock = Label()
clock.pack()
clock_timer()


timer = Label(text=f"{hour}:{minute}:{second}")
timer.pack()
countdown()

#Creating start and stop buttons to begin timer for reminders
start_button = Button(text="Start")
start_button.pack()

stop_button = Button(text="Stop")
stop_button.pack()


root.mainloop()





