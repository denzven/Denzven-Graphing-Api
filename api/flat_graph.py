# importing stuff
import flask
import matplotlib
import asyncio
import config
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use("agg")

# Adding a blueprint to start the graph function
flat_graph_runner = flask.Blueprint("flat_graph_runner", __name__)


# Using the Blueprint made with a path
@flat_graph_runner.route(config.FLAT_GRAPH_ROUTE, methods=["GET"])
def flat_graph():
    """
    Function for Getting Flat_Graphs
    """
    # Getting all the parameters from the url
    print(flask.request.args)
    formula_og_input = flask.request.args.get("formula")
    grid_value = flask.request.args.get("grid")
    plot_style = flask.request.args.get("plot_style")
    x_coord = flask.request.args.get("x_coord")
    y_coord = flask.request.args.get("y_coord")
    spine_top = flask.request.args.get("spine_top")
    spine_bottom = flask.request.args.get("spine_bottom")
    spine_left = flask.request.args.get("spine_left")
    spine_right = flask.request.args.get("spine_right")
    line_style = flask.request.args.get("line_style")
    grid_lines_major = flask.request.args.get("grid_lines_major")
    grid_lines_minor = flask.request.args.get("grid_lines_minor")
    tick_colors = flask.request.args.get("tick_colors")
    axfacecolor = flask.request.args.get("axfacecolor")
    figfacecolor = flask.request.args.get("figfacecolor")
    title_text = flask.request.args.get("title_text")
    plot_style_list = [
        "Solarize_Light2",
        "_classic_test_patch",
        "bmh",
        "classic",
        "dark_background",
        "fast",
        "fivethirtyeight",
        "ggplot",
        "grayscale",
        "seaborn",
        "seaborn-bright",
        "seaborn-colorblind",
        "seaborn-dark",
        "seaborn-dark-palette",
        "seaborn-darkgrid",
        "seaborn-deep",
        "seaborn-muted",
        "seaborn-notebook",
        "seaborn-paper",
        "seaborn-pastel",
        "seaborn-poster",
        "seaborn-talk",
        "seaborn-ticks",
        "seaborn-white",
        "seaborn-whitegrid",
        "tableau-colorblind10",
    ]

    # Printing tha values for debugging
    OutputMessage = f"""
    ```py
                                  
       Graph_Type : FlatGraph
 formula_og_input : {formula_og_input}
       grid_value : {grid_value}
       plot_style : {plot_style}
          x_coord : {x_coord}
          y_coord : {y_coord}
        spine_top : {spine_top}
     spine_bottom : {spine_bottom}
       spine_left : {spine_left}
      spine_right : {spine_right}
       line_style : {line_style}
 grid_lines_major : {grid_lines_major}
 grid_lines_minor : {grid_lines_minor}
      tick_colors : {tick_colors}
      axfacecolor : {axfacecolor}
     figfacecolor : {figfacecolor}
    ```
    """
    asyncio.run(config.SendLogs(OutputMessage))
    # Running the funtion in try-execpt blocks to avoid 500 type error
    try:  # Main Try-Execept block

        try:  # Checking for Formula
            if formula_og_input == None:
                return flask.jsonify(
                    error="formula input != provided",
                    error_id="ERROR_NO_FORMULA_INPUT_TRY_BLOCK",
                    fix="!D leave the Formula parameter empty",
                )
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_FORMULA_INPUT_TRY_BLOCK",
                fix="check your formula input again",
            )

        # ---

        try:  # Replacing only some with small letters to work in the eval
            print("hmm")
            pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_FORMULA_REPLACE_TRY_BLOCK",
                fix="Please check your formula again, it contains unsupported characters",
            )

        # ---

        try:  # Replacing only some with small letters to work in the eval
            formula_og_input = str(
                formula_og_input.upper()
            )  # My sole Defence against every single thing
            formula = formula_og_input.replace("x", "X")
            formula = formula.replace("y", "Y")
            formula = formula.replace("e", "math.e")
            formula = formula.replace("SIN", "np.sin")
            formula = formula.replace("COS", "np.cos")
            formula = formula.replace("TAN", "np.tan")
            formula = formula.replace("√", "np.sqrt")
            formula = formula.replace("SQRT", "np.sqrt")
            formula = formula.replace("π", "np.pi")
            formula = formula.replace("PI", "np.pi")
            formula = formula.replace("ABS", "np.absolute")
            formula = formula.replace("MIN", "np.min")
            formula = formula.replace("MAX", "np.max")
            formula = formula.replace("WHERE", "np.where")
            formula = formula.replace("CLAMP", "np.clip")
            formula = formula.replace("LOG", "np.log")
            formula = formula.replace("FLOOR", "np.floor")
            formula = formula.replace("CEIL", "np.ceil")
            formula = formula.replace("ROUND", "np.ceil")
            formula = formula.replace(")(", ")*(")
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_FORMULA_REPLACE_TRY_BLOCK",
                fix="Please check your formula again, it contains unsupported characters",
            )

        # ---
        try:  # Setting plot style
            if plot_style == None:
                plt.style.use("dark_background")
                pass
            if plot_style != None:
                plot_style_choice = int(plot_style)
                try:
                    plot_style = plot_style_list[plot_style_choice]
                except:
                    return f"couldnt use this style {plot_style}"
                plt.style.use(str(plot_style))
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_PLOT_STYLE_TRY_BLOCK",
                fix="change your plot_style to a valid number (between 0-25)",
            )

        # ---

        try:  # Setting x_coord
            if x_coord == None:
                xlist = np.linspace(-10, 10, num=1000)
                pass
            if x_coord != None:
                x_coord = int(x_coord)
                neg_x_coord = int(np.negative(x_coord))
                xlist = np.linspace(neg_x_coord, x_coord, num=1000)
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_X_COORD_TRY_BLOCK",
                fix="x_coord must be a number",
            )

        # ---

        try:  # Setting y_coord
            if y_coord == None:
                ylist = np.linspace(-10, 10, num=1000)
                pass
            if y_coord != None:
                y_coord = int(y_coord)
                neg_y_coord = int(np.negative(y_coord))
                ylist = np.linspace(neg_y_coord, y_coord, num=1000)
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_Y_COORD_TRY_BLOCK",
                fix="y_coord must be a number",
            )

        # ---

        try:  # Core funtion of actually getting the numbers
            X, Y = np.meshgrid(xlist, ylist)
            fig, ax = plt.subplots()
            F = eval(
                formula
            )  # The most Dangerous Eval... !D USE THIS... it jus works for this case
            pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_MAIN_EVAL_TRY_BLOCK",
                fix="Check the formula input again,\n (PS: 2x has to be written as 2*x, please read the docs for further info: \n https://denzven.pythonanywhere.com/docs)",
            )

        # ---

        try:  # setting up Line_style
            if line_style == None:
                ax.contour(X, Y, F, [0], colors="#4c82ca")
                pass
            if line_style != None:
                ax.contour(X, Y, F, [0], colors=f"#{line_style}")
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_LINE_STYLE_TRY_BLOCK",
                fix="check the line_style input it has to be a valid hex color withour #",
            )

        # ---

        try:  # Setting up Grids
            if grid_value == None:
                plt.minorticks_off()
                plt.grid(b=False)
                plt.grid(b=False)
                pass

            if grid_value == "1":
                plt.minorticks_on()
                plt.grid(b=True, which="major", color="#666666", linestyle="-")
                plt.grid(
                    b=True, which="minor", color="#999999", linestyle="-", alpha=0.2
                )
                pass

            if grid_value == "3":
                plt.minorticks_on()
                plt.grid(
                    b=True, which="major", color=f"#{grid_lines_major}", linestyle="-"
                )
                plt.grid(
                    b=True,
                    which="minor",
                    color=f"#{grid_lines_minor}",
                    linestyle="-",
                    alpha=0.2,
                )
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_GRID_VALUE_TRY_BLOCK",
                fix="check the grid input it has to be 1,2 or 3",
            )

        # ---

        try:  # Setting up each axis spine

            try:  # Top-Spine
                if spine_top == None:
                    ax.spines["top"].set_color(f"#ffffff")
                    pass

                if spine_top != None:
                    ax.spines["top"].set_color(f"#{spine_top}")
                    pass
            except Exception as e:
                return flask.jsonify(
                    error=str(e),
                    error_id="ERROR_TOP_SPINE_TRY_BLOCK",
                    fix="check the spine_top input it has to be a valid hex color withour #",
                )

            # ---

            try:  # Bottom-Spine
                if spine_bottom == None:
                    ax.spines["bottom"].set_color(f"#ffffff")
                    pass

                if spine_bottom != None:
                    ax.spines["bottom"].set_color(f"#{spine_bottom}")
                    pass
            except Exception as e:
                return flask.jsonify(
                    error=str(e),
                    error_id="ERROR_BOTTOM_SPINE_TRY_BLOCK",
                    fix="check the spine_bottom input it has to be a valid hex color withour #",
                )
            # ---

            try:  # Left-Spine
                if spine_left == None:
                    ax.spines["left"].set_color(f"#ffffff")
                    pass

                if spine_left != None:
                    ax.spines["left"].set_color(f"#{spine_left}")
                    pass
            except Exception as e:
                return flask.jsonify(
                    error=str(e),
                    error_id="ERROR_LEFT_SPINE_TRY_BLOCK",
                    fix="check the spine_left input it has to be a valid hex color withour #",
                )
            # ---

            try:  # Right-Spine
                if spine_right == None:
                    ax.spines["right"].set_color(f"#ffffff")
                    pass

                if spine_right != None:
                    ax.spines["right"].set_color(f"#{spine_right}")
                    pass
            except Exception as e:
                return flask.jsonify(
                    error=str(e),
                    error_id="ERROR_RIGHT_SPINE_TRY_BLOCK",
                    fix="check the spine_right input it has to be a valid hex color withour #",
                )
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_MAIN_SPINE_TRY_BLOCK",
                fix="please check values of spine again",
            )

        # ---

        try:  # setting up tick_colors
            if tick_colors == None:
                ax.tick_params(colors="#ffffff", which="both")
                pass
            if tick_colors != None:
                ax.tick_params(colors=f"#{tick_colors}", which="both")
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_TICK_COLORS_TRY_BLOCK",
                fix="check the tick_colors input it has to be a valid hex color withour #",
            )

        # ---

        try:  # setting up axfacecolors
            if axfacecolor == None:
                pass
            if axfacecolor != None:
                ax.set_facecolor(f"#{axfacecolor}")
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_AX_FACECOLOR_TRY_BLOCK",
                fix="check the axfacecolor input it has to be a valid hex color withour #",
            )

        # ---

        try:  # setting up figfacecolors
            if figfacecolor == None:
                pass
            if figfacecolor != None:
                fig.set_facecolor(f"#{figfacecolor}")
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_FIG_FACECOLOR_TRY_BLOCK",
                fix="check the figfacecolor input it has to be a valid hex color withour #",
            )

        # ---

        try:  # setting up title
            if title_text == None:
                plt.title(
                    f"graphical representation of {formula_og_input} = 0",
                    color="#ffffff",
                    pad=20,
                    fontsize="small",
                )
                pass
            if title_text != None:
                plt.title(f"{title_text}", color="#ffffff", pad=20, fontsize="small")
                pass
        except Exception as e:
            return flask.jsonify(
                error=str(e),
                error_id="ERROR_TITLE_TEXT_TRY_BLOCK",
                fix="the title contains invalid characters please recheck the title",
            )

        # ---

        try:  # adding title and saving and sending the file
            ax.set_aspect("equal")
            fig.savefig("../flat_plot_test.png", bbox_inches="tight", dpi=150)
            filename = "../flat_plot_test.png"
            plt.close(fig)
            return send_file(filename)
        except Exception as e:
            return flask.jsonify(error=str(e), error_id="ERROR_SAVE_FIG_TRY_BLOCK")
    except Exception as e:
        return flask.jsonify(error=str(e), error_id="ERROR_MAIN_TRY_BLOCK")


# Hope you loved this. feel free to try out and explore this Api at:
# https://denzven.pythonanywhere.com/
# Join my chill server at:
# https://dsc.gg/chilly_place
# pls star this on github it will be a great honour
# https://github.com/denzven/Denzven-Graphing-Api
# Hope yall have a great day! happy Graphing!
# Oh Boy it was a Pain to comment this code, But im sure i!t a pain for you to understand it :) .
