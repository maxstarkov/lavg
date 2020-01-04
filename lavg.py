#!/usr/bin/env python

import os
import curses


def print_info(stdscr):

    stdscr.clear()

    loadavg = os.getloadavg()
    cpu_count = open('/proc/cpuinfo').read().count('processor\t:')

    max_loadavg = max(loadavg)
    if max_loadavg < cpu_count * 0.85:
        idx = 1
    elif max_loadavg < cpu_count * 1.5:
        idx = 2
    else:
        idx = 3

    stdscr.attron(curses.color_pair(idx))
    stdscr.addstr(5, 5, "Load avearage: " + str(os.getloadavg()) + ", number of processors: " + str(cpu_count))
    stdscr.attroff(curses.color_pair(idx))    
    
    stdscr.addstr(10, 5, "Press 'u' for update, or any key for exit")

    stdscr.refresh()


def main(stdscr):

    curses.curs_set(0)
    
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK) 

    print_info(stdscr)

    while 1:
        key = stdscr.getch()
        if key == 117:
            print_info(stdscr)
        else:
            break


curses.wrapper(main)
