import Candidate
import flask
from flask import render_template
from flask import request
from flask import Flask,jsonify

from flask import make_response,url_for
from flask import request
from flask import Flask,jsonify




app = Flask(__name__)

def page_candidate():
    current_candidates = Candidate(serialize=False)
    return render_template('candidate.html',selected_menu_item='Candidate',candidates=current_candidates)

def page_index():
    return render_template('index.html',selected_menu_item='index')

def page_about():
    return render_template('about.html',selected_menu_item='Candidate')

def page_project():
    return

def page_experience():
    return

def init_website_routes(app):
    if app:
        app.add_url_rule('/about','page_about',page_about,methods=["GET"])
        app.add_url_rule('/project','page_project',page_project,methods=["GET"])
        app.add_url_rule('/candidate','page_candidate',page_candidate,methods=["GET"])
        app.add_url_rule('/experience','page_experience',page_experience,methods=["GET"])
        app.add_url_rule('/','page_index',page_index,methods=["GET"])

def list_routes(app):
    result=[]

init_website_routes(app)
if __name__ == '__main__':
    app.run(debug=True)
