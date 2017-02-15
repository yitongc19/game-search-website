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

@app.route('/search_result/name/<search_key>')
def searchResultbyName(search_key):
    result_list = api.get_search_by_name(search_key)
    return render_template("Search_result.html", game_list=result_list)

@app.route('/search_result/publisher/<search_key>')
def searchResultbyPublisher(search_key):
    result_list = api.get_search_by_publisher(search_key)
    return render_template("Search_result.html", game_list=result_list)

@app.route('/account_home/<account_name>')
def accountHome(account_name):
    return render_template('accountHome.html', account_name=account_name)

@app.route('/browse/genre/<browse_key>')
def browse_by_genre(browse_key):
    result_list = api.get_display_by_genre(browse_key)
    return render_template('browse.html', browse_key=browse_key, result_list=result_list)

@app.route('/browse/platform/<browse_key>')
def browse_by_platform(browse_key):
    result_list = api.get_display_by_platform(browse_key)
    return render_template('browse.html', browse_key=browse_key, result_list=result_list)

@app.route('/browse/publisher/<browse_key>')
def browse_by_publisher(browse_key):
    result_list = api.get_display_by_publisher(browse_key)
    return render_template('browse.html', browse_key=browse_key, result_list=result_list)

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/change_your_email/')
def changeEmail():
    return render_template('changeEmail.html')

@app.route('/game/<game_name>/<game_platform>')
def product(game_name, game_platform):
    game_info = api.get_display_by_name(game_name)
    target_game = {}
    for game in game_info:
        if game.getValue("platform") == game_platform:
            target_game = game
    return render_template('product.html', target_game=target_game)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=int(port))
