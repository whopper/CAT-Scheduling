#!/usr/bin/python

import sys, string, MySQLdb
from Availability import Avl_Query

def main ():

  selection = 0

  # Initialize database connection
  db=MySQLdb.Connection(host="localhost",user="schedule",
                        passwd="",db="availability")
  db_cursor = db.cursor()

  while(int(selection) != 5):
    # To be replaced with fancy curses interface, says monleezy
    print("\n\n+======================================================+")
    print("|               Welcome, Herder of CATS                |")
    print("|  1) Display All Availability in Weekly View          |")
    print("|  2) Display All Availability for a Specific Day      |")
    print("|  3) Display All Availability for a Specific DeskCAT  |")
    print("|  4) Show DeskCATS with < 8 Hours of Availability     |")
    print("|  5) Exit                                             |")
    print("+======================================================+\n")

    selection = raw_input("Select an Action: ")

    if(int(selection) == 1):
      print("")
    elif(int(selection) == 2):
      day = raw_input("View all availability for which day? ")
      Avl_Query.Display_Day_Avail(day, db_cursor)

    elif(int(selection) == 3):
      print("")
    elif(int(selection) == 4):
      print("")


if __name__ == '__main__':
  main()


