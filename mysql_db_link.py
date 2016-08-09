# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:59:51 2016

@author: hp
"""


import mysql.connector

cnx = mysql.connector.connect(user='root', password='your_password',
                              host='127.0.0.1',
                              database='your_sql_schema')
                              
cursor = cnx.cursor()

query = ("SELECT * FROM ..... WHERE (SELECT)... ")


cursor.execute(query)

#Optional, good starting point to explore query results
for (first_record_value, second_record_value) in cursor:
  print("{}, {} are values 1 and 2...".format(
    first_record_value, second_record_value))

cursor.close()                                                           
cnx.close()

print "Success"


