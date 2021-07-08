#importing stuff
from flask import *
import matplotlib
from matplotlib import *
matplotlib.use("agg")
import numpy as np
import matplotlib.pyplot as plt
import os
import traceback

# Adding a blueprint to start the graph function
polar_graph_runner = Blueprint('polar_graph_runner', __name__)

# Using the Blueprint made with a path
@polar_graph_runner.route('/DenzGraphingApi/v1/polar_graph/test/plot', methods=['GET'])
def polar_graph(): # The Funtion
    # Getting all the parameters from the url
    formula_og_input = request.args.get('formula')
    grid_value       = request.args.get('grid')
    plot_style       = request.args.get('plot_style')
    x_coord          = request.args.get('x_coord')
    y_coord          = request.args.get('y_coord')
    spine_top        = request.args.get('spine_top')
    spine_bottom     = request.args.get('spine_bottom')
    spine_left       = request.args.get('spine_left')
    spine_right      = request.args.get('spine_right')
    line_style       = request.args.get('line_style')
    grid_lines_major = request.args.get('grid_lines_major')
    grid_lines_minor = request.args.get('grid_lines_minor')
    tick_colors      = request.args.get('tick_colors')
    plot_style_list  = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast',
                       'fivethirtyeight', 'ggplot','grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
                       'seaborn-dark', 'seaborn-dark-palette','seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted',
                       'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel','seaborn-poster', 'seaborn-talk',
                       'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

    # Printing tha values for debugging
    print(
        f'''
        +========================================
        | formula_og_input   : {formula_og_input}
        |       grid_value   : {grid_value}
        |       plot_style   : {plot_style}
        |          x_coord   : {x_coord}
        |          y_coord   : {y_coord}
        |        spine_top   : {spine_top}
        |     spine_bottom   : {spine_bottom}
        |       spine_left   : {spine_left}
        |      spine_right   : {spine_right}
        |       line_style   : {line_style}
        | grid_lines_major   : {grid_lines_major}
        | grid_lines_minor   : {grid_lines_minor}
        |      tick_colors   : {tick_colors}
        +========================================
        '''
    )

    try: # Running the funtion in try-execpt blocks to avoid 500 type error

        try: # Checking for Formula
            if formula_og_input is None:
                return 'formula not provided'
        except Exception as e:
            return str(e)

        try: # Replacing only some with small letters to work in the eval
            formula_og_input = str(formula_og_input.upper())
            formula = formula_og_input.replace('x', 'X')
            formula = formula.replace('y', 'Y')
            formula = formula.replace('e', 'math.e')
            formula = formula.replace('SIN', 'np.sin')
            formula = formula.replace('COS', 'np.cos')
            formula = formula.replace('TAN', 'np.tan')
            formula = formula.replace('√', 'np.sqrt')
            formula = formula.replace('SQRT', 'np.sqrt')
            formula = formula.replace('π', 'np.pi')
            formula = formula.replace('PI', 'np.pi')
            formula = formula.replace('ABS', 'np.absolute')
            formula = formula.replace('MIN', 'np.min')
            formula = formula.replace('MAX', 'np.max')
            formula = formula.replace('WHERE', 'np.where')
            formula = formula.replace('CLAMP', 'np.clip')
            formula = formula.replace('LOG', 'np.log')
            formula = formula.replace('FLOOR', 'np.floor')
            formula = formula.replace('CEIL', 'np.ceil')
            formula = formula.replace('ROUND', 'np.ceil')
        except Exception as e:
            return str(e)

        try: # Setting plot style
            if plot_style is None:
                plt.style.use('dark_background')
                pass
            if plot_style is not None:
                plot_style_choice = int(plot_style)
                try:
                    plot_style = (plot_style_list[plot_style_choice])
                except:
                    return f'couldnt use this style {plot_style}'
                plt.style.use(str(plot_style))
                pass
        except Exception as e:
            return str(e)

        try: # Setting x_coord
            if x_coord is None:
                xlist = np.linspace(-10, 10, num=1000)
                pass
            if x_coord is not None:
                x_coord = int(x_coord)
                neg_x_coord = int(np.negative(x_coord))
                xlist = np.linspace(neg_x_coord, x_coord, num=1000)
                pass
        except Exception as e:
            return str(e)

        try: # Setting y_coord
            if y_coord is None:
                ylist = np.linspace(-10, 10, num=1000)
                pass
            if y_coord is not None:
                y_coord = int(y_coord)
                neg_y_coord = int(np.negative(y_coord))
                ylist = np.linspace(neg_y_coord, y_coord, num=1000)
                pass
        except Exception as e:
            return str(e)
  
        try: # Core funtion of actually getting the numbers
            X, Y = np.meshgrid(xlist, ylist)
            fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
            F = eval(formula)
            pass
        except Exception as e:
            return str(e)

        try: #setting up Line_style
            if line_style is None:
                ax.contour(X, Y, F, [0],colors='#4c82ca')
                pass
            if line_style is not None:
                ax.contour(X, Y, F, [0],colors=line_style)
                pass
        except Exception as e:
            return str(e)

        try: # Setting up Grids
            if grid_value is None:
                plt.minorticks_off()
                plt.grid(b=False)
                plt.grid(b=False)
                pass
            if grid_value is '1':
                plt.minorticks_on()
                plt.grid(b=True, which='major', color='#666666', linestyle='-')
                plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
                pass

            if grid_value is '3':
                plt.minorticks_on()
                plt.grid(b=True, which='major', color=grid_lines_major, linestyle='-')
                plt.grid(b=True, which='minor', color=grid_lines_minor, linestyle='-', alpha=0.2)
                pass
        except Exception as e:
            return str(e)

        try: #setting up tick_colors
            if tick_colors is None:
                ax.tick_params(colors='#ffffff', which='both')
                pass
            if tick_colors is not None:
                ax.tick_params(colors=tick_colors, which='both')
                pass
        except Exception as e:
            return str(e)

        #ax.set_facecolor('#1d1925')

        try: #adding title and saving and sending the file
            ax.set_aspect('equal')
            plt.title(f"graphical representation of {formula_og_input} = 0", color='#ffffff', pad=20, fontsize='small')
            fig.savefig('polar_plot_test.png', bbox_inches='tight', dpi=150)
            filename = 'polar_plot_test.png'
            plt.close(fig)
            return send_file(filename)
        except Exception as e:
            return str(e)

    except Exception as e:
        return str(e)

# Hope you loved this. feel free to try out and explore this Api at:
# https://denzven.pythonanywhere.com/
# Join my chill server at:
# https://dsc.gg/chilly_place
# pls star this on github it will be a great honour
# https://github.com/denzven/Denzven-Graphing-Api
# Hope yall have a great day! happy Graphing!