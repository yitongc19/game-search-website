'''
    api.py
    Yitong Chen, Megan Zhao, Eva Zhong Feburary 1, 2017

    This API contains routines that queries the database for information.
'''
import flask
from flask import render_template
import json
import sys

@app.route('/search/name/<name>')
def get_search_by_name(name):
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
    return []

@app.route('/search/publisher/<publisher>')
def get_search_by_publisher(publisher):
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
    return []

@app.route('/display/publisher/<publisher>')
def get_display_by_publisher(publisher):
    """ Return a list of dictionaries that are published by the same publisher, each of
    which describes one videogame with keys 'name' and 'platform'.

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales.com/display/publisher/Nintendo
    [{'name':'Wii Sports', 'platform':'Wii'}
    {'name':'Super Mario Bros.', 'platform':'NES'}
    {'name':'Mario Kart Wii', 'platform':'Wii'}...]
    """
    return []

@app.route('/display/genre/<genre>')
def get_display_by_genre(genre):
    """ Return a list of dictionaries that have the same genre, each of which describes
    one videogame with keys 'name' and 'platform'.

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales.com/display/genre/Sports
    [{'name':'Wii Sports', 'platform':'Wii'}
    {'name':'Wii sports Resort', 'platform':'Wii'}
    {'name':'Wii Fit', 'platform':'Wii'}...]
    """
    return []


@app.route('/display/platform/<platform>')
def get_display_by_platform(platform):
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
    return []


@app.route('/display/genre/<genre>')
def get_name_platform_display_by_genre(genre):
    """ Return a list of dictionaries that have the same genre, each of which describes
    one videogame with keys 'name' and 'platform'.

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales.com/display/genre/Sports
    [{'name':'Wii Sports', 'platform':'Wii'}
    {'name':'Wii sports Resort', 'platform':'Wii'}
    {'name':'Wii Fit', 'platform':'Wii'}...]
    """
    return []


@app.route('/display/genre/<genre>')
def get_name_display_by_genre(genre):
    """
    :param genre (String):
    :return name: a list of strings of the names of the games associated with the genre

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales/user/Action
    ['Assassin's Creed III', 'Driver', 'Red Dead Redemption'...]
    """
    return []


@app.route('/display/developer/<developer>')
def get_name_display_by_developer(developer):
    """
    :param developer (String):
    :return name: a list of strings of the names of the games associated with the developer

    Assumption: The input to this routine comes from an internal source and thus
    we assume the input string will be consisting of letters and numbers.

    Example: http://videogamessales/user/Acclaim
    ['Crazy Taxi', 'SX Superstar', 'Turok: Evolution'...]
    """

    return []

@app.route('/user/<account_name>')
def get_password_with_account_name(account_name):
    """
    :param account_name (String):
    :return password: a string of password associated with the given
    account name.

    Assumption: User name should only consist of letters and numbers. If not,
    it will be formatted using a parsing routine.

    Example: http://videogamessales/user/cheny2
    'vic31415@@'
    """
    return ""

@app.route('/user/home/<account_name>')
def get_user_info(account_name):
    """
    :param account_name (String):
    :return: a dictionary that describes the information associated
    with the user with keys 'email_address' and 'favorite_games'.

    Assumption: User name should only consist of letters and numbers. If not,
    it will be formatted using a parsing routine.

    Example: http://videogamessales/user/home/cheny2
    {'email_address':'cheny2@carleton.edu', 'favorite_games':['Halo 3', 'Super Mario Land',
    'Call of Duty: Black Ops 3']}
    """
    return {}

@app.route('/user/retrieve_password/<user_email>')
def get_password_with_email(user_email):
    """
    :param user_email (String):
    :return password: a string of password associated with the given
     email address.

     Assumption: The email address string passed in should be in proper email format.
     Invalid input will return an empty string.

     Example: http://videogamessales/retrieve_password/cheny2@carleton.edu
     'vic31415@@'
    """
    return ""
