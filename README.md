# tk-timer

Tutorial timer app using tk

Building a timer to further python learning using a suggested project (as an assignment) to complete.
Also using the opportunity to continue learning tkinter.

Bugs and not implemented:

- Check box function to play a sound when done.
- Code could be cleaned up also lots of unused code from trail and error.
- Cancel button takes a second or so to take effect (likely has to iterate through loop/timer).
- Could be made nicer and cleaned up interface, when I started I only knew .pack() grid would be better.
- Need to add default integers (00) for entry boxes as program errors if left blank even if only using seconds.

Update 8/2/2023

- Fixed cancel button response time. (Moved if statement higher in loop and code inside the if)
  - Also moved window.update() before if statment at top of while loop
- Fixed issue where when you canceled a timer it correctly set the global running to false to
  stop loop but never got set back true so wouldnt run again.
