
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:59:51 2016

@author: cammaman
"""

import mysql.connector
import pandas as pd

#Using a simple test MySQL database

#Define connection
cnx = mysql.connector.connect(user='root', password='your_password',
                              host='127.0.0.1',
                              database='your_schema')

#Define the cursor object (Allows execution against SQL statements)       
                
cursor = cnx.cursor(buffered=True)


query = ("SELECT first_name, last_name FROM employees ")


cursor.execute(query)

#Use the magic of pandas to write directly to a dataframe

df = pd.read_sql(query, cnx)


cursor.close()                                                           
cnx.close()

#Optional
print "YOU DID IT M8"





