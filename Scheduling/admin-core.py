#!/usr/bin/python

import sys, string, MySQLdb, curses
from Availability import Avl_Query

def main ():

  selection = 0

  # Initialize database connection
  db=MySQLdb.Connection(host="localhost",user="schedule",
                        passwd="",db="availability")
  db_cursor = db.cursor()


  while selection != ord('5'):

    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Welcome, Herder of CATS")
    screen.addstr(4, 4, "1) Display All Availability in Weekly View")
    screen.addstr(5, 4, "2) Display All Availability for a Specific Day")
    screen.addstr(6, 4, "3) Display All Availability for a Specific DeskCAT")
    screen.addstr(7, 4, "4) Show DeskCATS Who Haven't Updated Availability")
    screen.addstr(8, 4, "5) - Exit")
    screen.addstr(9, 4, "\n")
    screen.addstr(9, 4, "Select an Action: ")
    screen.addstr(9, 4, "\n")
    screen.refresh()

    selection = screen.getch()

    if selection == ord('1'):
         Avl_Query.Display_All_Avail(db_cursor)
         curses.endwin()

    elif selection == ord('2'):
      while sub_selection != "back":
        sub_selection = get_param("\nView all availability for which day? (\"back\" to return to menu)\n")

        if sub_selection != "back":
          Avl_Query.Display_Day_Avail(sub_selection, db_cursor)

      curses.endwin()

    elif selection == ord('3'):
      while sub_selection != "back":
        sub_selection = get_param("\nView all availability for which Deskcat? (\"back\" to return to menu)\n")
        if sub_selection != "back":
          Avl_Query.Display_DeskcatAvail_ByDay(sub_selection, db_cursor)

      curses.endwin()

    elif selection == ord('4'):
      Avl_Query.No_Recent_Update(db_cursor)
      curses.endwin()

  curses.endwin()


def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input





if __name__ == '__main__':
  main()


