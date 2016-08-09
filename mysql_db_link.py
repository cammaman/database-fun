# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:59:51 2016

@author: hp
"""

#import Quandl
import mysql.connector

cnx = mysql.connector.connect(user='root', password='cammaman',
                              host='127.0.0.1',
                              database='test_sql_schema')
                              
cursor = cnx.cursor()

query = ("SELECT first_name, last_name FROM employees ")


cursor.execute(query)

for (first_name, last_name) in cursor:
  print("{}, {} was hired".format(
    last_name, first_name))

cursor.close()                                                           
cnx.close()

print "Success"
#sql_data= Quandl.get(['YAHOO/ASX_FAR_AX','FRED/DCOILBRENTEU'],
#trim_start='2014-10', authtoken='kAvz8yJfRpGdCoH2qRTx')

