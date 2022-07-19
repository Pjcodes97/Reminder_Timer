from tkinter import *
from tkinter.ttk import *
from time import *

#Creates global variables to change and adjust
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
        minute += 1 
        second = 0
        if minute == 60:
            hour += 1
            minute = 0
    timer.config(text=f"{hour}:{minute}:{second}")
    timer.after(1000, countdown)


#Creates Alert Label when the set time has passed
def get_up_alert():
    global second, minute, hour
    string = "Get the fuck up"
    if hour == 1 and minute == 30:
        get_up_label.config(text=string)
    get_up_label.after(1000, get_up_alert)


#resets the timer to start over, does not STOP the timer, just resets to zero again
def reset():
    global second, minute, hour, cancel
    root.after_cancel(countdown)
    second = 0 
    minute = 0 
    hour = 0
    get_up_label.config(text="") 


#Creating Parent Window
root = Tk()
root.title("Stand Up and Stretch")
root.geometry("500x400")

#Creating a regular clock to keep track of time in general
clock = Label(root)
clock.pack()
clock_timer()

#Creates label for the countdown/ stopwatch
timer = Label(root, 
            text=f"{hour}:{minute}:{second}"
            )
timer.pack()


#Creating start and stop buttons to begin timer for reminders
start_button = Button(root, 
                    text="Start", 
                    command=countdown
                    )
start_button.pack()

#Create button for reseting the timer back to zero
reset_button = Button(root, 
                    text="Reset", 
                    command=reset
                    )
reset_button.pack()

#Create label where "Get Up" Alarm/Warning will display
get_up_label = Label(root)
get_up_label.pack()
get_up_alert()


root.mainloop()







