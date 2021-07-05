from flask import *
import matplotlib
matplotlib.use("agg")
import numpy as np
import matplotlib.pyplot as plt
import os
import traceback

polar_graph_runner = Blueprint('polar_graph_runner', __name__)

@polar_graph_runner.route('/DenzGraphingApi/v1/polar_graph/test/plot', methods=['GET'])
def flat_graph():
    formula_og_input = request.args.get('formula')
    grid_value = request.args.get('grid')
    plot_style = request.args.get('plot_style')
    x_coord = request.args.get('x_coord')
    y_coord = request.args.get('y_coord')
    plot_style_list = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast',
                       'fivethirtyeight', 'ggplot','grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
                       'seaborn-dark', 'seaborn-dark-palette','seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted',
                       'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel','seaborn-poster', 'seaborn-talk',
                       'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
    try:
        try:
            if formula_og_input is None:
                return 'formula not provided'
        except Exception as e:
            print('if formula_og_input is None:')
            return e
        try:
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
            print(formula_og_input)
            print(formula)
            print(grid_value)
        except Exception as e:
            print('replacement error')
            return f'couldnt parse this formula {formula}'
        try:
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
            return e

        try:
            if x_coord is None:
                xlist = np.linspace(-10, 10, num=1000)
                pass
            if x_coord is not None:
                x_coord = int(x_coord)
                neg_x_coord = int(np.negative(x_coord))
                xlist = np.linspace(neg_x_coord, x_coord, num=1000)
                pass
        except Exception as e:
            return e

        try:
            if y_coord is None:
                ylist = np.linspace(-10, 10, num=1000)
                pass
            if y_coord is not None:
                y_coord = int(y_coord)
                neg_y_coord = int(np.negative(y_coord))
                ylist = np.linspace(neg_y_coord, y_coord, num=1000)
                pass
        except Exception as e:
            return e

        X, Y = np.meshgrid(xlist, ylist)
        fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
        F = eval(formula)
        ax.contour(X, Y, F, [0],colors='#4c82ca')
        try:
            if grid_value is None:
                plt.minorticks_off()
                plt.grid(b=True, which='major', color='#666666', linestyle='-')
                plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
                print('grid is none')
                pass
            if grid_value is '1':
                plt.minorticks_on()
                plt.grid(b=True, which='major', color='#666666', linestyle='-')
                plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
                print('grid is not none')
                pass
        except Exception as e:
            return e
        plt.title(f"graphical representation of {formula_og_input} = 0", color='w', pad=20, fontsize='small')
        fig.savefig('polar_plot_test.png', bbox_inches='tight', dpi=150)
        print('hmmm?')
        filename = 'polar_plot_test.png'
        print(filename)
        plt.close(fig)
        return send_file(filename)

    except Exception as e:
        print(e)
        return f'couldn\'t parse this formula \'{formula}\''