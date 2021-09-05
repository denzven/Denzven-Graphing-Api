# importing stuff
import flask
import config
import matplotlib.pyplot as plt
import asyncio

# importing Blueprints
from api.flat_graph import flat_graph_runner
from api.beta_flat_graph import beta_flat_graph_runner
from api.multi_flat_graph import multiflat_graph_runner
from api.polar_graph import polar_graph_runner
from api.threeD_graph import threeD_graph_runner
from api.derivate_graph import derivative_graph_runner
from api.latex import latex_runner
import matplotlib

matplotlib.use("agg")


# Loading up the flask app and the blueprints in the /api folder
app = flask.Flask(__name__)
app.register_blueprint(flat_graph_runner)
app.register_blueprint(beta_flat_graph_runner)
app.register_blueprint(multiflat_graph_runner)
app.register_blueprint(polar_graph_runner)
app.register_blueprint(threeD_graph_runner)
app.register_blueprint(derivative_graph_runner)
app.register_blueprint(latex_runner)


# Landing page Html in /templates
@app.route("/")
def home():
    """
    Html for the Website HomePage
    """
    asyncio.run(config.SendLogs("someone visited home page"))
    print("hmm")
    return flask.render_template("home_page.html")


# Sub-pages for the "about the api" page in website in /templates
@app.route(config.API_HOMEPAGE_ROUTE)
def api():
    """
    Html for the Api HomePage
    """
    return flask.render_template("about_api.html")


# Sub-pages for the "api docs" page in website in /templates
@app.route(config.API_DOCS_ROUTE)
def docs():
    """
    Html for the Docs HomePage
    """
    return flask.render_template("docs.html")


# Sub-pages for the "api docs" page in website in /templates
@app.route(config.API_ATTRIBUTES_ROUTE)
def attributes():
    """
    Return the Attributes For the Graphs
    """
    attributes = {
        "grid=<1|2|3>": "Adds grids to the graph",
        "plot_style=<0-25>": "Determines the plot_style (boring)",
        "x_coord=<any>": "Fixes the value of the x_coord",
        "y_coord=<any>": "Fixes the value of the y_coord",
        "spine_top=<hex>": "Top-spine color",
        "spine_bottom=<hex>": "Bottom-spine color",
        "spine_left=<hex>": "Left-spine color",
        "spine_right=<hex>": "Right-spine color",
        "line_style=<hex>": "Change the color of the plot line",
        "grid_lines_major=<hex>": "Applies color to major girds",
        "grid_lines_minor=<hex>": "Applies color to minor girds",
        "tick_colors=<hex>": "Applies color to ticks",
        "axfacecolor=<hex>": "Applies color to foreground",
        "figfacecolor=<hex>": "Applies color to background",
        "title_text=<any text>": "Sets title",
    }
    return flask.jsonify(attributes)


# a in-process thing that enables usage of api using gui
@app.route(config.API_FORM_ROUTE)
def form():
    """
    Html for the Using the Api from the website itself (wip)
    """
    return flask.render_template("form.html")


# Submitting the robots.txt and sitemap.xml for SEO
@app.route("/robots.txt")
@app.route("/sitemap.xml")
def static_from_root():
    """
    Returns the Sitemap and robots.txt for the Website
    """
    return flask.send_from_directory(app.static_folder, flask.request.path[1:])


# A simple safty mechanism if anything goes wrong doesnt work tho...
@app.route(config.API_RESET_ROUTE, methods=["GET"])
def reset():
    """
    Supposed to "reset" plots.. idk if it works
    """
    passwd = flask.request.args.get("passwd")
    if passwd == "passwd":
        plt.close("all")
        return "done"


# When you have a full website you can't leave a chance for a rickroll 🤣
@app.route(config.API_RICKROLL_ROUTE)
def rickroll():
    """
    Rickroll
    """
    return flask.redirect("https://youtu.be/dQw4w9WgXcQ")


# Main portion for running the flask app using diff hosting services
# Run
if __name__ == "__main__":
    # app.run(port=5000)#--------------------------------------------------PythonAnywhere
    app.run(host="localhost", port=8080, debug=True, use_reloader=True)  # --Local
    # app.run(host='0.0.0.0', port=8080)#----------------------------------Replit
    # app.run(debug=True, use_reloader=True)#------------------------------Heroku

# Join my chill dicord server:

# https://dsc.gg/chilly_place
