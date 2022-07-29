from tkinter import *
from tkinter.ttk import *
from time import *
import pygame


#Creates global variables to change and adjust
second = 0 
minute = 0
hour = 0
pygame.mixer.init()




#Creating clock function
def clock_timer():
    string = strftime("%H:%M:%S %p")
    clock.config(text = string)
    clock.after(1000, clock_timer)


#Creates timer leading up the "alarm"
def countdown():
    global second, minute, hour
    start_button.config(state="disabled")
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
    string = "Time to take a break! Get up!"
    if hour == 1:
        get_up_label.config(text=string, style='my.TLabel')
        alarm_sound()
    get_up_label.after(1000, get_up_alert)


#resets the timer to start over, does not STOP the timer, just resets to zero again
def reset():
    global second, minute, hour, cancel
    root.after_cancel(countdown)
    second = 0 
    minute = 0 
    hour = 0
    get_up_label.config(text="")
    pygame.mixer.music.stop() 

#creates alarm sound when timer is reached
def alarm_sound():
    pygame.mixer.music.load("resources/mixkit-classic-alarm-995.wav")
    pygame.mixer.music.play(loops=3)


#Creating Parent Window
root = Tk()
root.title("Stand Up and Stretch")
root.geometry("500x300")

s = Style()
s.configure('my.TButton', font=(20))
s.configure("my.TLabel", font=('Arial', 25))

#Creating a regular clock to keep track of time in general
clock = Label(root, font=(20))
clock.pack(pady=10)
clock_timer()

#Creates label for the countdown/ stopwatch
timer = Label(root, 
            text=f"{hour}:{minute}:{second}",
            font=(20),
            )
timer.pack(pady=10)

#Creating start and stop buttons to begin timer for reminders
start_button = Button(root, 
                    text="Start",
                    command=countdown,
                    style='my.TButton'
                    )
start_button.pack(pady=10)

#Create button for reseting the timer back to zero
reset_button = Button(root, 
                    text="Reset",
                    command=reset,
                    style='my.TButton'
                    )
reset_button.pack()

#Create label where "Get Up" Alarm/Warning will display
get_up_label = Label(root)
get_up_label.pack(pady=15)
get_up_alert()

root.resizable(False,False)

root.mainloop()







