
from distutils.log import debug
from flask import Flask, render_template
from webapp.text_test import *
from webapp.timer import *
#from webapp.text_test import text_sostavv, text_azbuc_rr, text_azbucc, inf_rubik_assamble2, inf_rubik_assamble, text2, text
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
        return render_template('index2.html', page_title=title, greetir=greetr, inf_rubik_assamble=inf_rubik_assamble, time=sekund)

    @app.route('/index3')
    def index3 ():
        return render_template('index3.html')

    @app.route('/index3/kak_assemble_cube_azbuka')
    def kak_assemble_cube_azbuka ():
        return render_template( 'kak_assemble_cube_azbuka.html', text_azbucer=text_azbucc, text_r=text_azbuc_rr)


    @app.route('/index3/sostav_cube')
    def sostav_cube ():
        return render_template( 'sostav_cube.html', sostav_cube_det=text_sostavv)

    return app





