from flask import render_template, url_for, flash, redirect, Blueprint
from datetime import datetime
from flaskapp.main.models import Team
from flask_cors import cross_origin

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
@main.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route("/analysis", methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content-Type'])
def analysis():
    return render_template('dashboard.html')

@main.route("/eda", methods=['GET'])
def eda():
    return render_template("eda.html")

@main.route("/about", methods=['GET', 'POST'])
def about():
    image_files = {
        'gracex': Team.query.filter_by(name='gracex').first().image_file,
        'alisonbeer': Team.query.filter_by(name='alisonbeer').first().image_file,
        'jacobsussmilch': Team.query.filter_by(name='jacobsussmilch').first().image_file
    }
    return render_template('about.html', image_files=image_files)