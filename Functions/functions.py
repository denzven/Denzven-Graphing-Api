from modules.module import renderTeX
import config
import matplotlib.pyplot as plt
import sympy as sp
import discord
import numpy as np

x = sp.symbols("x")


def GetExpression(formula):
    """
    Gets the "symified" version of the input str
    """
    formula = formula.replace("y=", "")
    formula = formula.replace("^", "**")
    formula = formula.replace("e", "E")

    transformations = (
        sp.standard_transformations
        + (sp.implicit_multiplication_application,)
        + (sp.convert_xor,)
    )
    equation = sp.parse_expr(formula, transformations=transformations)

    return


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
