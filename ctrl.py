import curses
    
def main(win):
    while True:
        ch = win.getch()
        if ch == curses.KEY_RIGHT:
        elif ch == curses.KEY_LEFT:
        elif ch == curses.KEY_UP:
        elif ch == curses.KEY_DOWN:
        else:
            pass

curses.wrapper(main)


