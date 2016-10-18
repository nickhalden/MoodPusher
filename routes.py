import Candidate
import flask
from flask import render_template
from flask import request
from flask import Flask,jsonify

from flask import make_response,url_for
from flask import request
from flask import Flask,jsonify,flash




app = Flask(__name__)



def page_index():
    return render_template('index.html',selected_menu_item='index')

def page_about():
    if current_app:
        flash('The application was loaded','info')
        flash('The secret key is {0}'.format(current_app.config['SECRET_KEY'],'info'))
    return render_template('about.html',selected_menu_item='about')

def page_project():
    return render_template('project.html.html',selected_menu_item='project')

def page_experience():
    return render_template('experience.html.html',selected_menu_item='experience')

def page_candidate():
    current_candidates = Candidate(serialize=False)
    return render_template('candidate.html',selected_menu_item='Candidate',candidates=current_candidates)

def init_website_routes(app):
    if app:
        app.add_url_rule('/about','page_about',page_about,methods=["GET"])
        app.add_url_rule('/project','page_project',page_project,methods=["GET"])
        app.add_url_rule('/candidate','page_candidate',page_candidate,methods=["GET"])
        app.add_url_rule('/experience','page_experience',page_experience,methods=["GET"])
        app.add_url_rule('/','page_index',page_index,methods=["GET"])

#define the custom error handlers for the application
def handle_error_404(error):
    flash('Server says {0}'.format(error),'error')
    return render_template('404.html',selected_menu_item=None)

def handle_error_500(error):
    flash('Server says {0}'.format(error),'error')
    return render_template('500.html',selected_menu_item=None)

def init_error_handlers(app):
    if app:
        app.error_handler_spec[None][404]= handle_error_404
        app.error_handler_spec[None][500]= handle_error_500


def list_routes(app):
    result=[]

init_website_routes(app)
if __name__ == '__main__':
    app.run(debug=True)
