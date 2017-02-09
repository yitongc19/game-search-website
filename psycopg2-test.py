#!/usr/bin/env python3
'''
    psycopg2-demo.py
    Jeff Ondich, 23 April 2016
    Modifed by Eric Alexander, 1 February 2017

    A very short demo of how to use psycopg2 to connect to and
    query a PostgreSQL database. This demo assumes an "earthquakes"
    table including fields like quakedate, quaketime, mag, etc.
    (These can of course be changed to relate to your particular dataset.)

    You might also want to consult the official psycopg2 tutorial
    at https://wiki.postgresql.org/wiki/Psycopg2_Tutorial.
'''
import psycopg2

# Storing your user name and password directly in your code
# is easiest:
#
#   database = 'yourdatabasename'
#   user = 'yourusername'
#   password = 'yourdatabasepassword'
#
# However, this introduces potential security problems.
# One common mitigation of these dangers is to put the data
# in a separate module that's in the Python import path,
# but not in the web server's file tree.
import getpass
database = 'cheny2'
user = 'cheny2'
password = getpass.getpass('Enter PostgreSQL password for user {}: '.format(user))

# Login to the database
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print(e)
    exit()

# Query the database, leaving you with a "cursor"--an object you can
# use to iterate over the rows generated by your query.
try:
    cursor = connection.cursor()
    query = 'SELECT quakedate, quaketime, latitude, longitude FROM earthquakes WHERE longitude<0 ORDER BY longitude DESC'
    cursor.execute(query)
except Exception as e:
    print('Cursor error: {}'.format(e))
    connection.close()
    exit()

# We have a cursor now. Iterate over its rows to print the results.
list = []

for row in cursor:
    list.append(row)

for item in list:
    print(item)

# Don't forget to close the database connection.
connection.close()
