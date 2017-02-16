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
import re

app = flask.Flask(__name__)

database = 'zhonge'
user = 'zhonge'
password = getpass.getpass('Enter PostgreSQL password for user {}: '.format(user))
# Login to the database


# Query the database, leaving you with a "cursor"--an object you can
# use to iterate over the rows generated by your query.

@app.route('/search_result/<myname>')
def get_display_by_name(myname):
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
    if not myname.isalnum():
        myname = parse(myname)

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM video_game WHERE lower(name) LIKE %s"
        cursor.execute(query, ("%"+myname.lower()+"%",))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        myname, myplatform, myyearofrelease, mygenre, mypublisher, mynasales, myeusales, myjpsales, myothersales, myglobalsales, mycriticscore, mycriticcount, myuserscore, myusercount, mydeveloper, myrating = row
        gamedic["platform"] = myplatform
        gamedic["name"] = myname
        gamedic["yearofrelease"] = myyearofrelease
        gamedic["genre"] = mygenre
        gamedic["publisher"] = mypublisher
        gamedic["nasales"] = mynasales
        gamedic["eusales"] = myeusales
        gamedic["jpsales"] = myjpsales
        gamedic["othersales"] = myothersales
        gamedic["globalsales"] = myglobalsales
        gamedic["criticscore"] = mycriticscore
        gamedic["criticcount"] = mycriticcount
        gamedic["userscore"] = myuserscore
        gamedic["usercount"] = myusercount
        gamedic["developer"] = mydeveloper
        gamedic["rating"] = myrating
        gameList.append(gamedic)

    # Test what is in the gamelist
    """
    if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """

    connection.close()
    return gameList


@app.route('/search_result/<myname>')
def get_search_by_name(myname):
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
    if not myname.isalnum():
        myname = parse(myname)

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM video_game WHERE lower(name) LIKE %s"
        cursor.execute(query, ("%"+myname.lower()+"%",))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        myname, myplatform, myyearofrelease, mygenre, mypublisher, mynasales, myeusales, myjpsales, myothersales, myglobalsales, mycriticscore, mycriticcount, myuserscore, myusercount, mydeveloper, myrating = row
        gamedic["platform"] = myplatform
        gamedic["name"] = myname
        gamedic["yearofrelease"] = myyearofrelease
        gamedic["genre"] = mygenre
        gamedic["publisher"] = mypublisher
        gamedic["nasales"] = mynasales
        gamedic["eusales"] = myeusales
        gamedic["jpsales"] = myjpsales
        gamedic["othersales"] = myothersales
        gamedic["globalsales"] = myglobalsales
        gamedic["criticscore"] = mycriticscore
        gamedic["criticcount"] = mycriticcount
        gamedic["userscore"] = myuserscore
        gamedic["usercount"] = myusercount
        gamedic["developer"] = mydeveloper
        gamedic["rating"] = myrating
        gameList.append(gamedic)

    # Test what is in the gamelist
    """
    if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """

    connection.close()
    return gameList

"""
<<<<<<< HEAD
@app.route('/user/change_your_email/<account_name>')
def change_your_email(oldemail, newemail):
    
=======
@app.route('/user/change_your_email/<new_email>')
def change_your_email(oldemail, newemail):

>>>>>>> 8dc791a7182a696f9fa90321010e224435f50f04
    :param oldemail (String):
    :param newemail (String):

    Assumption: The email address string passed in should be in proper email format.
    Invalid input will return an empty string.

    Example: http://videogamessales/change_your_email/cheny2@carleton.edu
<<<<<<< HEAD
    
=======

>>>>>>> 8dc791a7182a696f9fa90321010e224435f50f04


if re.match(r"[^@]+@[^@]+\.[^@]+", newemail) == None:
    print("The email address in invalid")
    raise ValueError

if re.match(r"[^@]+@[^@]+\.[^@]+", oldemail) == None:
    print("The email address in invalid")
    raise ValueError

try:
    accountconnection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print(e)
    exit()

try:
    cursor = accountconnection.cursor()
    query = "UPDATE account_info SET Email=%s FROM account_info WHERE Email=%s" % (oldemail, newemail)

    ## ask what to do with this line
    ##cursor.execute(query, (newemail, oldemail,))
    cursor.execute(query)

except Exception as e:
    print('Cursor error: {}'.format(e))
    accountconnection.close()
    exit()

accountconnection.close()
"""
@app.route('/search/publisher/<mypublisher>')
def get_search_by_publisher(mypublisher):
    """ Return a list of dictionaries that by the same publisher, each of which describes
    one videogame with keys 'name', 'platform', 'yearofrelease', 'genre', '
    publisher', 'nasales', 'jpsales', 'othersales', 'globalsales', 'criticscore',
    'criticcount', 'userscore', 'usercount', 'developer', 'rating'.

    Assumption: The input publisher string only contains letters and numbers. If the
    user input a string that contains any special characters, this routine would call
    a parsing routine to format the publisher and ignore the special characters.

    Example: http://videogamessales.com/search/publisher/Nintendo
    [{'name':'Wii Sports', 'platform':'Wii', 'yearofrelease':2006, 'genre':'Sports',
    'publisher':'Nintendo', 'nasales':41.36, 'eusales':28.96, 'jpsales':3.77,
    'othersales':8.45, 'globalsales':82.53, 'criticscore':76,'criticcount':51,
    'userscore':8, 'usercount':322, 'developer':Nintendo, 'rating':'E'}
    {'name':'Super Mario Bros.', 'platform':'NES', 'yearofrelease':1985, 'genre':'Platform',
    'publisher':'Nintendo', 'nasales':29.08, 'eusales':3.58, 'jpsales':6.81,
    'othersales':0.77, 'globalsales':40.24, 'criticscore':-1,'criticcount':-1,
    'userscore':-1, 'usercount':-1, 'developer':-1, 'rating':-1}
    {'name':'Mario Kart Wii', 'platform':'Wii', 'yearofrelease':2008, 'genre':'Racing',
    'publisher':'Nintendo', 'nasales':15.68, 'eusales':12.76, 'jpsales':3.79,
    'othersales':3.29, 'globalsales':35.52, 'criticscore':82,'criticcount':73,
    'userscore':8.3, 'usercount':709, 'developer':Nintendo, 'rating':E}...]
    """
    if not mypublisher.isalnum():
        mypublisher = parse(mypublisher)

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM video_game WHERE lower(publisher) LIKE %s"
        cursor.execute(query, ('%'+mypublisher.lower()+'%',))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        myname, myplatform, myyearofrelease, mygenre, mypublisher, mynasales, myeusales, myjpsales, myothersales, myglobalsales, mycriticscore, mycriticcount, myuserscore, myusercount, mydeveloper, myrating = row
        gamedic["platform"] = myplatform
        gamedic["name"] = myname
        gamedic["yearofrelease"] = myyearofrelease
        gamedic["genre"] = mygenre
        gamedic["publisher"] = mypublisher
        gamedic["nasales"] = mynasales
        gamedic["eusales"] = myeusales
        gamedic["jpsales"] = myjpsales
        gamedic["othersales"] = myothersales
        gamedic["globalsales"] = myglobalsales
        gamedic["criticscore"] = mycriticscore
        gamedic["criticcount"] = mycriticcount
        gamedic["userscore"] = myuserscore
        gamedic["usercount"] = myusercount
        gamedic["developer"] = mydeveloper
        gamedic["rating"] = myrating
        gameList.append(gamedic)

    connection.close()

    return gameList


@app.route('/display/publisher/<publisher>')
def get_display_by_publisher(mypublisher):
    """ Return a list of dictionaries that are published by the same publisher, each of
    which describes one videogame with keys 'name' and 'platform'.

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales.com/display/publisher/Nintendo
    [{'name':'Wii Sports', 'platform':'Wii'}
    {'name':'Super Mario Bros.', 'platform':'NES'}
    {'name':'Mario Kart Wii', 'platform':'Wii'}...]
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT name, platform FROM video_game WHERE lower(publisher)=%s"
        cursor.execute(query, (mypublisher.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        myname, myplatform = row
        gamedic["platform"] = myplatform
        gamedic["name"] = myname
        gameList.append(gamedic)


    connection.close()

    return gameList

@app.route('/display/genre/<genre>')
def get_display_by_genre(mygenre):
    """ Return a list of dictionaries that have the same genre, each of which describes
    one videogame with keys 'name' and 'platform'.

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales.com/display/genre/Sports
    [{'name':'Wii Sports', 'platform':'Wii'}
    {'name':'Wii sports Resort', 'platform':'Wii'}
    {'name':'Wii Fit', 'platform':'Wii'}...]
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT name, platform FROM video_game WHERE lower(genre)=%s"
        cursor.execute(query, (mygenre.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        myname, myplatform = row
        gamedic["platform"] = myplatform
        gamedic["name"] = myname
        gameList.append(gamedic)


    # Test what is in the gamelist

    """if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """
    connection.close()

    return gameList


@app.route('/display/platform/<platform>')
def get_display_by_platform(myplatform):
    """ Return a list of dictionaries that have the same platform, each of which describes
    one videogame with keys 'name' and 'genre'.
    This routine is called as user chooses to browse games by the main category of platform
    provided on the homepage.

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales.com/display/platform/GC
    [{'name':'Reign of Fire', 'genre':'Shooter'}
    {'name':'Universal Studios Theme Parks Adventure', 'genre':'Misc'}
    {'name':'Rocky', 'genre':'fighting'}...]
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT name, genre FROM video_game WHERE lower(platform)=%s"
        cursor.execute(query, (myplatform.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        myname, mygenre = row
        gamedic["genre"] = mygenre
        gamedic["name"] = myname
        gameList.append(gamedic)


    # Test what is in the gamelist

    """if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """
    connection.close()

    return gameList


@app.route('/display/genre/<genre>')
def get_name_platform_display_by_genre(mygenre):
    """ Return a list of dictionaries that have the same genre, each of which describes
    one videogame with keys 'name' and 'platform'.

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales.com/display/genre/Sports
    [{'name':'Wii Sports', 'platform':'Wii'}
    {'name':'Wii sports Resort', 'platform':'Wii'}
    {'name':'Wii Fit', 'platform':'Wii'}...]
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT name, platform FROM video_game WHERE lower(genre)=%s"
        cursor.execute(query, (mygenre.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        myname, myplatform = row
        gamedic["platform"] = myplatform
        gamedic["name"] = myname
        gameList.append(gamedic)


    # Test what is in the gamelist

    """if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """
    connection.close()

    return gameList


@app.route('/display/genre/<genre>')
def get_name_display_by_genre(mygenre):
    """
    :param mygenre (String):
    :return name: a list of strings of the names of the games associated with the genre

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales/user/Action
    ['Assassin's Creed III', 'Driver', 'Red Dead Redemption'...]
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT name FROM video_game WHERE lower(genre)=%s"
        cursor.execute(query, (mygenre.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        myname = row[0]
        gameList.append(myname)


    connection.close()

    return gameList


@app.route('/display/developer/<developer>')
def get_name_display_by_developer(mydeveloper):
    """
    :param mydeveloper (String):
    :return name: a list of strings of the names of the games associated with the developer

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales/user/Acclaim
    ['Crazy Taxi', 'SX Superstar', 'Turok: Evolution'...]
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT name FROM video_game WHERE lower(developer)=%s"
        cursor.execute(query, (mydeveloper.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        myname = row[0]
        gameList.append(myname)


    # Test what is in the gamelist

    """if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """
    connection.close()

    return gameList

@app.route('/user/<account_name>')
def get_password_with_account_name(myaccountname):
    """
    :param myaccountname (String):
    :return password: a string of password associated with the given
    account name.

    Assumption: User name should only consist of letters and numbers.


    Example: http://videogamessales/user/cheny2
    'vic31415@@'
    """
    # Test bad input
    if not myaccountname.isalnum():
        print("The username contains special characters! Please use another username.")
        raise ValueError

    try:
        accountconnection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = accountconnection.cursor()
        query = "SELECT Password FROM account_info WHERE lower(Name)=%s"
        cursor.execute(query, (myaccountname.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        accountconnection.close()
        exit()
    mypassword=cursor.fetchone()[0]

    # Test what is in the gamelist

    """if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """
    accountconnection.close()

    return mypassword


@app.route('/user/home/<account_name>')
def get_user_info(myaccountname):
    """
    :param myaccountname (String):
    :return: a dictionary that describes the information associated
    with the user with keys 'email_address' and 'favorite_games'.

    Assumption: User name should only consist of letters and numbers.

    Example: http://videogamessales/user/home/cheny2
    {'email_address':'cheny2@carleton.edu', 'favorite_games':['Halo 3', 'Super Mario Land',
    'Call of Duty: Black Ops 3']}
    """
    # Test bad input
    if not myaccountname.isalnum():
        print("The username contains special characters! Please use another username.")
        raise ValueError

    try:
        accountconnection = psycopg2.connect(database=database, user=user, password=password)
        
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = accountconnection.cursor()
        query = "SELECT Email, Favouritegame FROM account_info WHERE lower(Name)=%s"
        cursor.execute(query, (myaccountname.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        accountconnection.close()
        exit()

    accountDic = {}
    myemailaddress, myfavouritegames = cursor.fetchone()
    accountDic["email_address"] = myemailaddress
    accountDic["favorite_games"] = myfavouritegames.split(', ')

    # Test what is in the gamelist

    """if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """
    accountconnection.close()

    return accountDic

@app.route('/user/retrieve_password/<user_email>')
def get_password_with_email(myuseremail):
    """
    :param myuseremail (String):
    :return password: a string of password associated with the given
     email address.

     Assumption: The email address string passed in should be in proper email format.
     Invalid input will return an empty string.

     Example: http://videogamessales/retrieve_password/cheny2@carleton.edu
     'vic31415@@'
    """
    if re.match(r"[^@]+@[^@]+\.[^@]+", myuseremail) == None:
        print("The email address in invalid")
        raise ValueError

    try:
        accountconnection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = accountconnection.cursor()
        query = "SELECT Password FROM account_info WHERE lower(Email)=%s"
        cursor.execute(query, (myuseremail.lower(),))

    except Exception as e:
        print('Cursor error: {}'.format(e))
        accountconnection.close()
        exit()
    mypassword=cursor.fetchone()[0]

    # Test what is in the gamelist

    """if len(gameList) == 0:
            print("nothing is in the list")
    else:
        for item in gameList:
            print(item)
    """
    accountconnection.close()

    return mypassword

def getHighRatings():
    """
    Return the first 100 games with the highest ratings.
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT name, platform FROM video_game ORDER BY User_Score"
        cursor.execute(query)

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []
    
    for row in cursor:
        if row.get("User_Score")!= 'tbd':
            gamedic = {}
            myname, myplatform = row
            gamedic["platform"] = myplatform
            gamedic["name"] = myname
            gameList.append(gamedic)
    
    return gameList[:100]
    
def getHighSaleRecord():
    """
    Return the first 100 games with the highest sale records.
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT name, platform FROM video_game ORDER BY Global_Sales NULLS LAST"
        cursor.execute(query)

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []
    
    for row in cursor:
        gamedic = {}
        myname, myplatform = row
        gamedic["platform"] = myplatform
        gamedic["name"] = myname
        gameList.append(gamedic)
    
    return gameList[:100]


def getAllPublisher():
    """
    Return a list of all publishers.
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT Name FROM video_game"
        cursor.execute(query)

    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    publisherList = []
    for row in cursor:  
        mypublisher = row.get("Publisher")
        publisherList.append(mypublisher)
    
    return publisherList
    
def parse(inputStr):
    """
    Internal facing method that removes all the special characters from the input string
    except for spaces.
    :param inputStr:
    :return: the parsed string
    """
    result_string = ""
    for c in inputStr:
        if allowedChar(c):
            result_string += c
    return result_string

def allowedChar(char):
    if char == " " or char == "." or char == ":" or char == "," or char == "-" or char == "\'" or char.isalnum():
        return True
    else:
        return False

if __name__ == '__main__':
#    print(get_display_by_genre("Sports"))
#    print(get_name_display_by_genre("Sports"))
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

