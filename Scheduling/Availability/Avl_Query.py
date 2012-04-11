#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import sys, string, MySQLdb

def Display_All_Avail(db_cursor):
  db_cursor.execute("SELECT * FROM deskcat_avl2 ORDER BY FIELD(day, 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')")
  data = db_cursor.fetchall()
  Display_Header()
  Generate_Output(data)


def Display_Day_Avail(sub_selection, db_cursor):
  query_day = sub_selection[0:3]
  db_cursor.execute("SELECT * FROM deskcat_avl2 WHERE day = '%s'" % query_day)
  data = db_cursor.fetchall()
  Display_Header()
  Generate_Output(data)

def Display_DeskcatAvail_ByDay(sub_selection, db_cursor):
  db_cursor.execute("SELECT * FROM deskcat_avl2 WHERE deskcat = '%s' ORDER BY FIELD(day, 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')" % sub_selection)
  data = db_cursor.fetchall()
  Display_Header()
  Generate_Output(data)

def  No_Recent_Update(db_cursor):
  print "+===========+===============+"
  print "|   Deskcat |   Last Update |"
  print "+===========+===============+"
  db_cursor.execute("SELECT DISTINCT deskcat, updated FROM deskcat_avl2 WHERE updated < date_sub(now(), interval 1 month)")
  data = db_cursor.fetchall()
  Generate_Output(data)


#====================================================================================+
# The following functions generate the final output resulting from the database query|
#====================================================================================+
def Generate_Output(data):
  num_results    = len(data)  # Total number of results for this day
  result_string  = ""

  i = 0
  y = 0
  while i < int(num_results):
    y = 0
    result_string = ""
    while y < len(data[i]):
      result_string += ("|   %s " % str(data[i][y]))
      y = y + 1
    print result_string
    i = i + 1


def Display_Header():
  print "\n"
  print " _______ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ ______________ _________ "
  print "| Day   |08:00|09:00|10:00|11:00|12:00|13:00|14:00|15:00|16:00|17:00| Last Updated | Deskcat |"
  print " ‾‾‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾  ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ "


