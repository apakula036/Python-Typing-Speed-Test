from cgitb import text
import curses
import time
from curses import wrapper
import random 


text_options = [
    "I started learning Python several months ago and want to become a specialist.",
    "The videos like this one motivate me the best!",
    "I am learning so much with your videos!",
    "The playful cat ran through the forest into the stream.",
    "The man is driving the car down the street.",
    "There is no war in Ba Sing Se.",
    "As Dory the fish once said, just keep swimming!",
    "Some of these text options are much harder than the others.",
    "I enjoy writing code in Python but I confuse the syntax often!"
]



def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to start the typing test!", curses.color_pair(2))
    stdscr.addstr("\nPress escape to exit.", curses.color_pair(4))
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0): # =0 will make the paramter optional to pass it in 
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
 


    for i, char in enumerate(current): # enumerate gives element from current text 
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    target_text = random.choice(text_options)
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text: # combines a list to a string with the "" as the seperator
            stdscr.nodelay(False) 
            break

        try:
            key = stdscr.getkey() #checks for value of a key but if you dont enter a key nothing happens 
        except:
            continue # brings us back to the top of the while loop if continue 
        if current_text == []:
            start_time = time.time()


        if ord(key) == 27: #27 is escape key 
            break 
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


# stdscr is the screen use that to manipulate it 
def main(stdscr): # standard output screen 
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # setting color IDs 
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"You completed the game! Press the Q key to reset the game or press ESC to exit.")
        key = stdscr.getkey()
        if ord(stdscr.getkey()) == 27:
            break

wrapper(main)

    