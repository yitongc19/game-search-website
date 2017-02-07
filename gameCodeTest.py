'''
    api.py
    Yitong Chen, Megan Zhao, Eva Zhong Feburary 1, 2017

    This API contains routines that queries the database for information.
'''

import flask
from flask import render_template
import json
import sys
import psycopg2

import getpass

app = flask.Flask(__name__)


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


@app.route('/search/name/<name>')
def get_search_by_name():
    """ Return a list of dictionaries that contains the input name, each of which
    describes one videogame with keys 'name', 'platform', 'yearofrelease', 'genre', '
    publisher', 'nasales', 'jpsales', 'othersales', 'globalsales', 'criticscore',
    'criticcount', 'userscore', 'usercount', 'developer', 'rating'.

    Assumption: The input name string only contains letters and numbers. If the
    user input a string that contains any special characters, this routine would call
    a parsing routine to format the name and ignore the special characters.

    Example: http://videogamessales.com/search/name/WiiSports
    [{'name':'Wii Sports', 'platform':'Wii', 'yearofrelease':2006, 'genre':'Sports',
    'publisher':'Nintendo', 'nasales':41.36, 'eusales':28.96, 'jpsales':3.77,
    'othersales':8.45, 'globalsales':82.53, 'criticscore':76,'criticcount': 51,
    'userscore':8, 'usercount':322, 'developer':Nintendo, 'rating':'E'}...]
    """
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM video_game WHERE name='15 Days' ORDER BY name DESC"
        cursor.execute(query)
    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()


    gameList = []
    
    for row in cursor:
       gameList.append(row) 

    # Test what is in the gamelist
    if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)

    #print(cursor.fetchall())
    connection.close()


if __name__ == "__main__":
    #app.run()
    get_search_by_name()
