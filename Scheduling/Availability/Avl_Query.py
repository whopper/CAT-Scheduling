#!/usr/bin/python
import sys, string, MySQLdb

def Display_All_Avail(db_cursor):
  db_cursor.execute("SELECT * FROM deskcat_availability ORDER BY FIELD(day, 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'), hour")
  data = db_cursor.fetchall()
  Display_Header()
  Generate_Output(data)


def Display_Day_Avail(day, db_cursor):
  db_cursor.execute("SELECT * FROM deskcat_availability WHERE day = '%s' ORDER BY hour" % day)
  data = db_cursor.fetchall()
  Display_Header()
  Generate_Output(data)

def Display_DeskcatAvail_ByDay(deskcat, db_cursor):
  db_cursor.execute("SELECT * FROM deskcat_availability WHERE deskcat = '%s' ORDER BY FIELD(day, 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'), hour" % deskcat)
  data = db_cursor.fetchall()
  Display_Header()
  Generate_Output(data)

def  No_Recent_Update(db_cursor):
  print "  +===============+===============+"
  print "  |   Deskcat     |   Last Update |"
  print "  +===============+===============+"
  db_cursor.execute("select distinct deskcat, last_updated from deskcat_availability where last_updated < date_sub(now(), interval 1 month)")
  data = db_cursor.fetchall()
  Generate_Output(data)

def Display_Insufficient_Hours(db_cursor):
  print "+=============+===========+"
  print "|  Num Hours |   Deskcat  |"
  print "+=============+===========+"
  db_cursor.execute("SELECT COUNT(*), deskcat FROM deskcat_availability GROUP BY deskcat HAVING COUNT(*) < 8")
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
      result_string += ("   |  %s   " % str(data[i][y]))
      y = y + 1
    print result_string
    i = i + 1


def Display_Header():
  print "\n"
  print "+====================+============+==================+===========+=========+"
  print "|      Day           |    Hour    |    Last Updated  | Preferred | Deskcat |"
  print "+====================+============+==================+===========+=========+\n"

