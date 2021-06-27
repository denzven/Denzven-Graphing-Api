#from flask import Flask, jsonify, request, send_file,render_template,redirect
from flask import *
import matplotlib
matplotlib.use("agg")
import numpy as np
import matplotlib.pyplot as plt
import os
import traceback

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/api')
def api():
    return render_template('about_api.html')

@app.route('/docs')
def examples():
    return render_template('docs.html')

@app.route('/graph', methods=['GET'])
def graph3():
    formula_og = request.args.get('formula')
    contour_level = request.args.get('contour_level')
    plt.style.use('dark_background')
    xlist = np.linspace(-10, 10, num=1000)
    ylist = np.linspace(-10, 10, num=1000)
    theta = np.array([0, np.pi/2, 3*np.pi/2, 2*np.pi])
    X, Y = np.meshgrid(xlist, ylist)
    try:
        formula = formula_og.replace('x', 'X')
        formula = formula.replace('y', 'Y')
        # formula = formula.replace('arcsin', 'np.arcsin')
        # formula = formula.replace('arccos', 'np.arccos')
        # formula = formula.replace('arctan', 'np.arctan')
        formula = formula.replace('sin', 'np.sin')
        formula = formula.replace('cos', 'np.cos')
        formula = formula.replace('tan', 'np.tan')
        formula = formula.replace('ʘ', 'theta')
        formula = formula.replace('√', 'np.sqrt')
        formula = formula.replace('π', 'np.pi')
        chars = ['1','2','3','4','5','6','7','8','9','0',
                #'sin','cos','tan','arcsin','arccos','arctan',
                's','i','n','c','o','t','a','n','r',
                '√','π','%','/','.','!','^','(',')','*','-','**','+',
                'x','y']
        #chars = ['√', 'x', '7', '5', '=', '2', 's', ')', '1', '÷', 'n', 't', '*', '6', 'y', '×', '4', '9', '/', 'a', '8','.', '"','c', '-', 'i', 'o', '^', '0', '3', '+', '(', 'p', 'π','r']
        char_check = ((c in chars) for c in formula_og)
        char_check_final = all(char_check)
        print(formula_og)
        if char_check_final:
            print('passable')
            pass
        else:
            print('not passable')
            #return 'not passable due to not supported characters in formula.. if your formula has a + (plus sign) please replace it with %2B'
            return(traceback.format_exc())
    except Exception as e:
        #return(traceback.format_exc())
        return(e)
    F = eval(formula)
    print(f"{formula_og} {formula}")
    # fig, ax = plt.subplots(
    # plt.plot(xlist,ylist,label=f'graph of {formula_og}')
    # plt.legend()
    # plt.grid(linestyle = '--', linewidth = 0.25)
    # Plot the data

    # Show the major grid lines with dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-')

    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    if contour_level == None or contour_level == 'None':
        plt.contour(X, Y, F, [0], colors='#4c82ca', linestyles='solid')
        pass
    if contour_level != None:
        plt.contour(X, Y, F, [float(contour_level)], colors='#4c82ca', linestyles='solid')
        pass

    ax = plt.gca()
    ax.set_aspect('equal')
    plt.title(f"graphical representation of {formula_og} = 0", color='w', pad=20, fontsize='small')
    # fig.savefig('plot3.png', bbox_inches='tight', dpi=150)
    plt.savefig('plot3.png', bbox_inches='tight', dpi=150)
    filename = 'plot3.png'
    plt.close()
    return send_file(filename)

@app.route('/2d_polar/graph', methods=['GET'])
def polar_graph():
    a = request.args.get('a')
    n = request.args.get('n')
    plt.style.use('dark_background')
    plt.axes(projection='polar')
    a = int(a)
    n = int(n)
    rads = np.linspace(0, 2* np.pi, num=1000)
    for rad in rads:
        r = a * np.cos(n*rad)
        plt.polar(rad, r,'g.')

    plt.title(f"graphical representation of r={a}cos({n}θ)", color='w', pad=20, fontsize='small')
    plt.savefig('polar_plot.png', bbox_inches='tight', dpi=150)
    filename = 'polar_plot.png'
    plt.close()
    return send_file(filename)


@app.route('/reset', methods=['GET'])
def reset():
    passwd = request.args.get('passwd')
    if passwd == 'passwd':
        plt.close('all')
        return 'done'


@app.route('/rickroll')
def rickroll():
    return redirect("https://youtu.be/dQw4w9WgXcQ")

@app.route('/DenzGraphingApi/v1/flat_graph/test/plot', methods=['GET'])
def flat_Graph():
    #https: // denzven.pythonanywhere.com / DenzGraphingApi / v1 / 2dGraph / plot?formula = < formula > & grid = true & plot_style = dark & x_coord = 10 & y_coord = 10
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
    #print('formula_og_input:  ' + formula_og_input)
    #print('grid:  ' + grid)
    #print('plot_style:  ' + plot_style)
    #print('x_coord:  ' + x_coord)
    #print('y_coord:  ' + y_coord)
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
            # chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            #         's', 'i', 'n', 'c', 'o', 't', 'a', 'n', 'r', 'e',
            #         '√', 'π', '%', '/', '.', '!', '^', '(', ')', '*', '-', '**', '+', '=',
            #         'x', 'y']
            # char_check = ((c in chars) for c in formula_og_input)
            # char_check_final = all(char_check)
            # if char_check_final:
            #     print('passable')
            #     pass
            # else:
            #     print('not passable')
            #     return traceback.format_exc()
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
        fig, ax = plt.subplots()
        F = eval(formula)
        ax.contour(X, Y, F, [0])
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
        ax.set_aspect('equal')
        plt.title(f"graphical representation of {formula_og_input} = 0", color='w', pad=20, fontsize='small')
        fig.savefig('D:\\DenzGraphingApi\\plot_test.png', bbox_inches='tight', dpi=150)
        filename = 'D:\\DenzGraphingApi\\plot_test.png'
        plt.close(fig)
        return send_file(filename)

    except Exception as e:
        return f'couldn\'t parse this formula \'{formula}\''


#run
#pythonanywhere
#port = int(os.environ.get('PORT', 5000))
#if __name__ == '__main__':
#    app.run()

#local
#if __name__ == '__main__':
#    app.run(host='localhost', port=8080)

#heroku
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

