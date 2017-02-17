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

    for result in result_list:
        if result['name'] is None:
            result['name'] = ""

    return render_template('browse.html', browse_key=browse_key, result_list=result_list)

@app.route('/browse/platform/<browse_key>')
def browse_by_platform(browse_key):
    result_list = api.get_display_by_platform(browse_key)
    return render_template('browse.html', browse_key=browse_key, result_list=result_list)

@app.route('/browse/publisher/<browse_key>')
def browse_by_publisher(browse_key):
    result_list = api.get_display_by_publisher(browse_key)
    return render_template('browse.html', browse_key=browse_key, result_list=result_list)


@app.route('/browseAllPublishers/')
def browse_all_publishers():
    result_list = api.getAllPublisher()
    for result in result_list:
        if result is None:
            result['name'] = ""
    return render_template('browseAllPublishers.html', result_list=result_list)


@app.route('/browseAllPlatforms/')
def browse_all_platforms():
    result_list = api.getAllPlatform()
    for result in result_list:
        if result is None:
            result['name'] = ""
    return render_template('browseAllPlatforms.html', result_list=result_list)

@app.route('/browseHighestRating/')
def browse_highest_rating():
    result_list = api.getHighRatings()
    return render_template('browseHighRatings.html', result_list=result_list)

@app.route('/browseBestSellers/')
def browse_best_sellers():
    result_list = api.getHighSaleRecord()
    return render_template('browseBestSellers.html', result_list=result_list)


@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')
    
@app.route('/readme/')
def readme():
    return render_template('README.html')

'''
@app.route('/change_your_email/')
def changeEmail():
    return render_template('changeEmail.html')
'''

@app.route('/game/<game_name>/<game_platform>')
def product(game_name, game_platform):
    game_info = api.get_display_by_name(game_name)
    target_game = {}
    for game in game_info:
        if game['platform'] == game_platform:
            target_game = game
    game_genre = target_game['genre']
    game_same_genre = api.get_display_by_genre(game_genre)
    similar_game = game_same_genre[:3]
    game_publisher = target_game['publisher']
    game_same_publisher = api.get_display_by_publisher(game_publisher)
    same_publisher = game_same_publisher[:3]
    return render_template('product.html', target_game=target_game, similar_game=similar_game, same_publisher=same_publisher)

#generic search method
@app.route('/search/<generic_search_key>')
def genericSearch(search_key):
    name_result_list = api.get_search_by_name(search_key)
    return render_template("Search_result.html", game_list=name_result_list)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=int(port))
