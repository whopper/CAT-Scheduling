#!/usr/bin/python
import sys, string, MySQLdb


def Display_Day_Avail(day, db_cursor):
  db_cursor.execute("SELECT * FROM deskcat_availability WHERE day = '%s'" % day)

  data = db_cursor.fetchall()
  result = str(data)
  print result

