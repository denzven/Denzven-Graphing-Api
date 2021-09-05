#from modules.module import renderTeX
#import config
import matplotlib.pyplot as plt
import sympy as sp
import sympy.parsing.sympy_parser as spr
import discord
import numpy as np
import numexpr as ne

x = sp.symbols('x')
y = sp.symbols('y')


def GetExpression(InputFormula):
    '''
    Gets the "symified" version of the input str
    '''
    if '=' in InputFormula:
        ExpList = InputFormula.split('=')
        InputFormula = ExpList[0] + "-" + "(" + ExpList[::-1][0] + ")"
        print(' Formula Contains =')

    if 'y' not in InputFormula:
        print("Formula doesnt contain y")
        
    if 'x' not in InputFormula:
        print("Formula doesnt contain x")

    if '=0' in InputFormula:
        print("Formula contains =0 which is not needed lmao")

    InputFormula = InputFormula.replace('√', 'sqrt')
    InputFormula = InputFormula.replace('^', '**')
    print(InputFormula)

    transformations = (spr.standard_transformations + (spr.implicit_multiplication_application,) + (spr.convert_xor,))
    equation = spr.parse_expr((InputFormula) , transformations=transformations)

    print(str(equation))
    return equation

def RenderLatex(InputLatex):
    """
    a Function that renders Latex
    """
    plt.rcParams["mathtext.fontset"] = "cm"
    plt.rcParams["font.family"] = "DejaVu Serif"
    fig = plt.figure()
    fig.set_facecolor(config.MAIN_BG_COLOR)
    fig.text(0, 0, InputLatex, color=config.MAIN_COLOR)
    fig.savefig(
        "tex.png", dpi=1000, bbox_inches="tight", pad_inches=0.05, transparent=False
    )
    plt.close()
    return


def GetDerivative(equation):
    """ """
    equation = GetExpression(equation)
    derivative = sp.diff(equation, x)
    renderTeX(f"${sp.latex(derivative)}$")

    return


def GetLimit(equation, x_value):
    """ """
    equation = GetExpression(equation)
    limit = sp.limit(equation, x, x_value)
    if "oo" in str(x_value):
        x_value = x_value.replace("oo", "\infty")

    tex = (
        r"$\lim_{x \rightarrow "
        + str(x_value)
        + "}"
        + f"({sp.latex(equation)}) = {sp.latex(limit)}$"
    )
    RenderLatex(tex)

    return
