import curses 
from curses import wrapper 


# stdscr is the screen use that to manipulate it 
def main(stdscr): # standard output screen 
    stdscr.clear()
    stdscr.addstr("Hello world!")
    stdscr.refresh()

wrapper(main)
