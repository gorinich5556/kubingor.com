from distutils.log import debug
from flask import Flask, render_template
from webapp.text_test import *
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
        
    @app.route('/')
    def index ():
        title = 'kubingor.com'
        greetr = text
        return render_template('index.html', page_title=title, greetir=greetr, inf_rubik_assamble=inf_rubik_assamble,)

    @app.route('/index2')
    def index2 ():
        title = 'kubingor.com2'
        greetr = text2
        inf_rubik_assamble = inf_rubik_assamble2
        return render_template('index2.html', page_title=title, greetir=greetr, inf_rubik_assamble=inf_rubik_assamble)

    @app.route('/index3')
    def index3 ():
        return render_template('index3.html')

    @app.route('/index3/kak_assemble_cube_azbuka')
    def kak_assemble_cube_azbuka ():
        return render_template( 'kak_assemble_cube_azbuka.html', text_azbucer=text_azbucc)

    return app





