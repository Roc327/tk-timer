#!/usr/bin/env python3
"""
Simple Timer project to continue learning after fundamentals, using this to also learn and play with tkinter.


    Copyright (C) <2023>  <Nathan Van Valkenburg>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
    Contact at: github.com/Roc327

"""

import time
import tkinter as tk
from tkinter import *

RUNNING = True  # Global to exit loop


def get_input():
    """
    Get the inputs of the entry boxes once
    the set countdown button is pressed
    """
    if entry_hours.get() == "":
        hours = 0
    else:
        hours = int(entry_hours.get())
    if entry_minutes.get() == "":
        minutes = 0
    else:
        minutes = int(entry_minutes.get())
    if entry_seconds.get() == "":
        seconds = 0
    else:
        seconds = int(entry_seconds.get())
    countdown(hours, minutes, seconds)


def countdown(hours, minutes, seconds):
    """
    The main countdown function. Takes in time in seconds,
    then increment the loop
    """
    global RUNNING
    RUNNING = True

    time_seconds = seconds + (minutes * 60) + (hours * 3600)

    while time_seconds:
        display_timer(time_seconds)
        window.update()
        time_seconds -= 1
        if RUNNING:
            time.sleep(1)
            continue
        else:
            break

    if RUNNING:
        timer_label.config(text="Timer Complete!")
    else:
        timer_label.config(text="Timer has been canceled.")


def display_timer(time_seconds):
    """
    Convert time in seconds that is passed into function
    into hours, minutes, seconds then display on screen
    """
    minutes, seconds = divmod(time_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    time_str = f"{hours:d}:{minutes:02d}:{seconds:02d}"

    timer_label.config(text=time_str)


def exit_loop():
    """
    Exits loop if user presses cancel button
    """
    global RUNNING
    RUNNING = False
    return RUNNING


# Creating a window, setting its size and title,
window = tk.Tk()
window.geometry("600x600")
window.title("Timer")

# create widgets
head = tk.Label(window, text="Countdown clock and Timer", font="Calibri 15")
enter_time_lbl1 = tk.Label(window, text="Enter time in HH:MM:SS", font="bold")
entry_hours = tk.Entry(window, width=30)
entry_minutes = tk.Entry(window, width=30)
entry_seconds = tk.Entry(window, width=30)
checkbox_var = tk.StringVar()
checkbox = tk.Checkbutton(
    window,
    text="Check for timer complete sound.",
    onvalue=True,
    offvalue=False,
    variable=checkbox_var,
)  # creating checkbox
button = tk.Button(window, text="Set Countdown", command=get_input, bg="yellow")
current_time_txt = tk.Label(window, text="Current Time:")
printed_time_lbl = Label(font=("calibri", 15, "bold"))
timer_txt_label = tk.Label(window, text="Coundown timer:")
timer_label = tk.Label(window, font=("calibri", 15, "bold"))
cancel_button = tk.Button(window, text="Cancel", command=exit_loop)


# place widgets on window
head.pack(pady=20)

enter_time_lbl1.pack()

entry_hours.pack()
entry_minutes.pack()
entry_seconds.pack()

checkbox.pack()
button.pack()  # button.place(x=260, y=230)
printed_time_lbl.pack()

timer_txt_label.pack()
timer_label.pack()
cancel_button.pack()


window.mainloop()
