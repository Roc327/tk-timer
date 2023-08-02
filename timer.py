"""

Timer project to continue learning after fundamentals (book, think python2)
using this to also learn and play with tkinter.

"""

import time
import tkinter as tk
from tkinter import *
from time import strftime
from datetime import datetime, timedelta

running = True  #Global flag to exit loop


def current_time():
    """
    Print current time on window
    """
    string = strftime('%H:%M:%S %p')
    printed_time_lbl.config(text=string)
    printed_time_lbl.after(1000, current_time)
    # now = datetime.now()
    # current_time = now.utctime("%H:%M:%S")
    # tk.Label(text=current_time).pack()


def check_type(var):
    """
    Used for debugging
    """
    if var == 'None':
        print(var, '\n', type(var), ' in if')
        return '00'
    elif var is None:
        print('In Elif var is ', type(var))
    else:
        return var


def get_input():
    """
    Get the inputs of the entry boxes once
    the set countdown button is pressed
    """
    hour = entry_hour.get()
    minute = entry_minutes.get()
    second = entry_seconds.get()
    time_string = (hour + ':' + minute + ':' + second)
    ts = datetime.strptime(time_string, '%H:%M:%S')
    time_seconds = ts.second + ts.minute * 60 + ts.hour * 3600
    countdown(time_seconds)
    # tk.Label(text="Time-Up", font=('bold', 20)).place(x=250, y=290)


def countdown(time_seconds):
    """
    The main countdown function. Takes in time in seconds,
    converts the time to a readable format HH:MM:SS,
    then prepares it to be updated to the label then increment the loop
    """
    global running
    running = True    
    while time_seconds:
        window.update()
        if running == True:
            timer = timedelta(seconds=time_seconds)
            timer_label.config(text=timer)
            time.sleep(1)
            time_seconds -= 1
            continue
        else:
            break

    timer_label.config(text="Timer Complete!")


def exit_loop():
    """
    Exits loop if user presses cancel button
    """
    global running
    running = False
    return running 


# Creating a window, setting its size and title,
window = tk.Tk()
window.geometry('600x600')
window.title('Timer')

# create widgets
head = tk.Label(window, text="Countdown clock and Timer", font='Calibri 15')
enter_time_lbl1 = tk.Label(window, text="Enter time in HH:MM:SS", font='bold')
enter_time_lbl2 = tk.Label(window, text="Must be less than 24 hrs.")
entry_hour = tk.Entry(window, width=30)
entry_minutes = tk.Entry(window, width=30)
entry_seconds = tk.Entry(window, width=30)
checkbox_var = tk.StringVar()
checkbox = tk.Checkbutton(window, text='Check for timer complete sound.',
                          onvalue=True, offvalue=False,
                          variable=checkbox_var)  # creating checkbox
button = tk.Button(window, text="Set Countdown", command=get_input,
                   bg='yellow')
current_time_txt = tk.Label(window, text="Current Time:")
printed_time_lbl = Label(font=('calibri', 15, 'bold'))
timer_txt_label = tk.Label(window, text="Coundown timer:")
timer_label = tk.Label(window, font=('calibri', 15, 'bold'))
cancel_button = tk.Button(window, text="Cancel", command=exit_loop)


# place widgets on window
head.pack(pady=20)

enter_time_lbl1.pack()
enter_time_lbl2.pack()

entry_hour.pack()
entry_minutes.pack()
entry_seconds.pack()

checkbox.pack()
button.pack()  # button.place(x=260, y=230)
current_time_txt.pack()
printed_time_lbl.pack()

timer_txt_label.pack()
timer_label.pack()
cancel_button.pack()


current_time()

window.mainloop()
