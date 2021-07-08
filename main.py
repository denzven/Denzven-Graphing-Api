# importing stuff
from flask import *
import matplotlib
matplotlib.use("agg")
import numpy as np
import matplotlib.pyplot as plt
import os
import traceback

# importing Blueprints
from api.flat_graph import flat_graph_runner
from api.polar_graph import polar_graph_runner
from api.threeD_graph import threeD_graph_runner

# Loading up the flask app and the blueprints in the /api folder
app = Flask(__name__)
app.register_blueprint(flat_graph_runner)
app.register_blueprint(polar_graph_runner)
app.register_blueprint(threeD_graph_runner)

# Landing page Html in /templates
@app.route('/')
def home():
    return render_template('home_page.html')

# Sub-pages for the "about the api" page in website in /templates
@app.route('/api')
def api():
    return render_template('about_api.html')

# Sub-pages for the "api docs" page in website in /templates
@app.route('/docs')
def examples():
    return render_template('docs.html')

# a in-process thing that enables usage of api using gui
@app.route('/test_form')
def form():
    return render_template('form.html')

# Submitting the robots.txt and sitemap.xml for SEO
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

# A simple safty mechanism if anything goes wrong
@app.route('/reset', methods=['GET'])
def reset():
    passwd = request.args.get('passwd')
    if passwd == 'passwd':
        plt.close('all')
        return 'done'

# When you have a full website you can't leave a chance for a rickroll 🤣
@app.route('/rickroll')
def rickroll():
    return redirect("https://youtu.be/dQw4w9WgXcQ")

#Main portion for running the flask app using diff hosting services
# Run
if __name__ == '__main__':
#    app.run(port=5000)#--------------------------pythonanywhere
    app.run(host='localhost', port=8080)#---------local
#    app.run(host='0.0.0.0', port=8080)#---------replit
#    app.run(debug=True, use_reloader=True)#------heroku
# Join my chill dicord server:
# https://dsc.gg/chilly_place
# 69 Nice