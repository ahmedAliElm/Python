import time
import msvcrt

RED = "\033[31m"
GREEN = "\033[32m"

def clearConsole():
    print("\033[H\033[J")

def timer(minutes):

    seconds = minutes * 60  
    paused = 0

    mins, secs = divmod(seconds, 60)
    timer_format = '{:02d}:{:02d}'.format(mins, secs)
 
    print(GREEN + timer_format, end='\r')

    key = msvcrt.getch().decode('utf-8')
    # waits for a space key press to start the timer

    if key == ' ':

        while seconds >= 0:

            if msvcrt.kbhit():  # whenever a key is pressed this if condition is true
                key = msvcrt.getch().decode('utf-8') # get the pressed key
                if key == ' ':
                    paused = not paused

            if not paused:
                mins, secs = divmod(seconds, 60) # mins = seconds//60 and secs = seconds%60
                timer_format = '{:02d}:{:02d}'.format(mins, secs)
                print(GREEN + timer_format, end='\r')
                time.sleep(1)
                seconds -= 1

            else:
                mins, secs = divmod(seconds, 60)
                secs += 1
                timer_format = '{:02d}:{:02d}'.format(mins, secs)
                print(RED + timer_format, end='\r')
                time.sleep(1)
        
        clearConsole()

        finish = 0

        while finish != 1:
            # This loop is for when the timer ends, it makes the timer blink in red
            # and if you press the space key, the program ends.

            print(RED + timer_format, end='\r')
            time.sleep(1)
            clearConsole()
            time.sleep(1)

            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8')
                if key == ' ':
                    finish = 1

timer(1)   # Calling the function

