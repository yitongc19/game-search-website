#!/usr/bin/env python3
'''
    example_flask_app.py
    Jeff Ondich, 22 April 2016
	Modified by Eric Alexander, January 2017

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import flask
from flask import render_template
import json
import sys

app = flask.Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Citizen of CS257.'


@app.route('/fancier/')
def itDoesHTML():
    htmlStr = '<html lang="en">' + \
              '<head>' + \
              '  <title>Cool page</title>' + \
              '</head>' + \
              '<body>' + \
              '  <h1>Welcome to CS 257</h1>' + \
              '  <p>Please refrain from feeding the squirrels.</p>' + \
              '</body>' + \
              '</html>'
    return htmlStr

@app.route('/prettier/')
def itDoesBetterHTML():
    return render_template('prettier.html')


@app.route('/authors/<author>')
def get_author(author):
    ''' What a dopey function! But it illustrates a Flask route with a parameter. '''
    if author == 'Twain':
        author_dictionary = {'last_name': 'Twain', 'first_name': 'Mark'}
    elif author == 'Shakespeare':
        author_dictionary = {'last_name': 'Shakespeare', 'first_name': 'William'}
    else:
        author_dictionary = {'last_name': 'McBozo', 'first_name': 'Bozo'}
    return json.dumps(author_dictionary)


@app.route('/genres/<genre>')
def get_genre(genre):
    '''Get the genre from the data set'''
    if genre == 'Sport':
        genre_dictionary = {'genre': 'Sport'}
    elif genre == 'Action':
        genre_dictionary = {'genre': 'Action'}
    else:
        genre_dictionary = {'genre': 'Unknown'}
    return json.dumps(genre_dictionary)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
