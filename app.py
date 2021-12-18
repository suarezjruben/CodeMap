import flask
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app.static_folder = 'static'


@app.route('/')
def index():  # put application's code here
    return flask.render_template("index.html")

@app.route('/Main')
def search():
    return flask.render_template("Main.html")


@app.route('/hello',methods=["GET", "POST"])
def hello():
    if request.method == 'POST':
        print("Recieved")
        data = (request.get_json()) #parse as Json
        with open('static/newSearch.json', 'w') as json_file:
            json.dump(data, json_file)
        return 'OK', 200


@app.route('/index.html')
def index_page():
    return flask.render_template("index.html")


if __name__ == '__main__':
    app.run()
