#!/usr/bin/python

import sys, string, MySQLdb
from Availability import Avl_Query

def main ():

  selection = 0

  # Initialize database connection
  db=MySQLdb.Connection(host="localhost",user="schedule",
                        passwd="",db="availability")
  db_cursor = db.cursor()

  while(int(selection) != 6):
    # To be replaced with fancy curses interface, says monleezy
    print("\n\n+======================================================+")
    print("|               Welcome, Herder of CATS                |")
    print("|  1) Display All Availability in Weekly View          |")
    print("|  2) Display All Availability for a Specific Day      |")
    print("|  3) Display All Availability for a Specific DeskCAT  |")
    print("|  4) Show DeskCATS with < 8 Hours of Availability     |")
    print("|  5) Show DeskCATS Who Haven't Updated Availability   |")
    print("|  6) Exit                                             |")
    print("+======================================================+\n")

    selection = raw_input("Select an Action: ")

    if(int(selection) == 1):
      Avl_Query.Display_All_Avail(db_cursor)

    elif(int(selection) == 2):
      day = raw_input("View all availability for which day?\n")
      Avl_Query.Display_Day_Avail(day, db_cursor)

    elif(int(selection) == 3):
      deskcat = raw_input("View all availability for which Deskcat?\n")
      Avl_Query.Display_DeskcatAvail_ByDay(deskcat, db_cursor)

    elif(int(selection) == 4):
      Avl_Query.Display_Insufficient_Hours(db_cursor)

    elif(int(selection) == 5):
      Avl_Query.No_Recent_Update(db_cursor)


if __name__ == '__main__':
  main()


