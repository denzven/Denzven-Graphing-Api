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
    return render_template('home.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')

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


#port = int(os.environ.get('PORT', 5000))
#if __name__ == '__main__':
#    app.run()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

