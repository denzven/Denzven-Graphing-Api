#from flask import Flask, jsonify, request, send_file,render_template,redirect
from flask import *
import matplotlib
matplotlib.use("agg")
import numpy as np
import matplotlib.pyplot as plt
import os
import traceback
from api.flat_graph import flat_graph_runner
from api.polar_graph import polar_graph_runner
from api.threeD_graph import threeD_graph_runner

app = Flask(__name__)
app.register_blueprint(flat_graph_runner)
app.register_blueprint(polar_graph_runner)
app.register_blueprint(threeD_graph_runner)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/api')
def api():
    return render_template('about_api.html')

@app.route('/rickroll')
def rickroll():
    return render_template('rickroll_pg.html')

@app.route('/docs')
def examples():
    return render_template('docs.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/reset', methods=['GET'])
def reset():
    passwd = request.args.get('passwd')
    if passwd == 'passwd':
        plt.close('all')
        return 'done'

@app.route('/rickroll')
def rickroll_2():
    return redirect("https://youtu.be/dQw4w9WgXcQ")

#run
if __name__ == '__main__':
#    app.run(port=5000)#--------------------------pythonanywhere
#    app.run(host='localhost', port=8080)#---------local
#    app.run(host='0.0.0.0', port=8080)#---------replit
    app.run(debug=True, use_reloader=True)#------heroku