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
import api

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def homepage():
    return render_template("Home.html")

@app.route('/search_result/name/<myname>')
def searchResultbyName(myname):
    result_list = api.get_search_by_name(myname)
    return render_template("Search_result.html", game_list=result_list)
    
@app.route('/search_result/publisher/<mypublisher>')
def searchResultbyPublisher(mypublisher):
    result_list = api.get_search_by_publisher(mypublisher)
    return render_template("Search_result.html", game_list=result_list)    

@app.route('/account_home/')
def accountHome():
    return render_template('accountHome.html')

@app.route('/browse/')
def browse():
    return render_template('browse.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/change_your_email/')
def changeEmail():
    return render_template('changeEmail.html')

@app.route('/game/<game_name>/')
def product(game_name):
    return render_template('product.html', game_name=game_name)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=int(port))
