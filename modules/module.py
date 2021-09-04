import matplotlib.pyplot as plt  
import pylab
import numexpr as ne
import numpy as np  
import sympy as sp




x = sp.Symbol('x')

from sympy.parsing.sympy_parser import (
  parse_expr, # converts string to sympy expression
  standard_transformations, # eg. 5! = 5*4*3*2*1
  implicit_multiplication_application, # e.g. 2x = 2*x
  convert_xor # e.g. 2^x = 2**x
)



# <--------------[PARSE EXPRESSION]---------------> #

def parseExpression(expression):

  expression = expression.replace('y=', '')
  expression = expression.replace('^', '**')
  expression = expression.replace('e', 'E')
    
  transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
  equation = parse_expr(expression, transformations=transformations)
  
  return equation

# <-----------------[PLOT GRAPH]------------------> #

def plotGraph(equation, lower, upper):

  eq = parseExpression(equation)

  ax = plt.gca()

  x = np.linspace(lower, upper, 100)
  y = ne.evaluate(str(eq))

  ax.plot(
    x, y, 
    label = f"$y={sp.latex(eq)}$", 
    alpha = 0.5 # 50% transparent
  )
  
  ax.legend()
  ax.grid(True, linestyle=':')
  ax.spines['left'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['bottom'].set_position('zero')
  ax.spines['top'].set_color('none')

  plt.xlim(lower, upper)
  plt.savefig('graph.png', dpi=300)
  plt.close()

  return



# <-----------------[RENDER TEX]------------------> #

def renderTeX(text): 
  
  # change math font to Computer Modern
  plt.rcParams['mathtext.fontset'] = 'cm'
  # change normal font to DejaVu Serif
  plt.rcParams['font.family'] = 'DejaVu Serif'
  
  fig = pylab.figure()
  
  fig.text(
    0, 
    0, 
    text,
    color = 'black'
  )

  fig.savefig(
    'tex.png', 
    dpi = 1000,
    bbox_inches = 'tight',
    pad_inches = 0.05,
    transparent = False
  )

  plt.close()

  return



# <-----------------[GET LIMIT]-------------------> #

def getLimit(equation, x_value):

  equation = parseExpression(equation)
  limit = sp.limit(equation, x, x_value)

  if 'oo' in str(x_value):
    x_value = x_value.replace('oo', '\infty')
  
  tex = (
    r'$\lim_{x \rightarrow ' +
    str(x_value) + '}' + 
    f'({sp.latex(equation)}) = {sp.latex(limit)}$'
  )
  renderTeX(tex)

  return



# <---------------[GET DERIVATIVE]----------------> #

def getDerivative(equation):

  equation = parseExpression(equation)
  derivative = sp.diff(equation, x)
  renderTeX(f'${sp.latex(derivative)}$')

  return



# <----------------[GET INTEGRAL]-----------------> #

def getIntegral(equation, lt, ut):

  equation = parseExpression(equation)

  if lt != None and ut != None:

    definite_int = sp.integrate(equation, (x, lt, ut))
    definite_int = sp.latex(definite_int)
    definite_int = definite_int.replace(
      r'\text{NaN}', '\mathtt{undef}'
    )
    tex = (
      r'$\int_{' + str(lt) + '}^{' + str(ut) + '}' +
      '(' + sp.latex(equation) + ') \ dx' + 
      '=' + definite_int + '$'
    )

  else:

    indefinite_int = sp.integrate(equation, x)
    tex = f'${sp.latex(indefinite_int)} + C$'

  renderTeX(tex)

  return



# <----------------[GET SOLUTION]-----------------> #

def getSolution(equation, domain):

  if domain.lower() == 'real':
    domain = sp.S.Reals
  else:
    domain = sp.S.Complexes

  equation = parseExpression(equation)
  sols = sp.solveset(equation, x, domain=domain)

  # equation has certain solutions
  if type(sols) == sp.sets.sets.FiniteSet:
    tex = f'$x={", ".join(sp.latex(s) for s in sols)}$'
  
  # equation has infinite solutions
  elif type(sols) == sp.sets.fancysets.ImageSet:

    tex = sp.latex(sols)
    tex = tex.replace('\left', '')
    tex = tex.replace('\middle', '')
    tex = tex.replace(r'\right', '')
    tex = tex.replace('\;', '')
    tex = tex.replace('\{', '')
    tex = tex.replace('\}', '')
    tex = tex.replace(' |', ',')
    tex = f'$x={tex}$'

  # equation has union solutions
  elif type(sols) == sp.sets.sets.Union:

    tex = sp.latex(sols)
    tex = tex.replace('\left', '')
    tex = tex.replace('\middle', '')
    tex = tex.replace(r'\right', '')
    tex = tex.replace('\;', '')
    tex = tex.replace('\{', '')
    tex = tex.replace('\}', '')
    tex = tex.replace(' |', ',')
    tex = f'$x={tex}$'

  # equation has no solutions
  elif type(sols) == sp.sets.sets.EmptySet:
    tex = 'No solution over ℝ'
    
  renderTeX(tex)

  return



# <---------------[GET EXPANSION]-----------------> #

def getExpansion(expression):

  expression = parseExpression(expression)
  expansion = sp.expand(expression, x)
  renderTeX(f'${sp.latex(expansion)}$')

  return



# <-------------[GET FACTORISATION]---------------> #

def getFactorisation(expression):

  expression = parseExpression(expression)
  factorisation = sp.factor(expression)
  renderTeX(f'${sp.latex(factorisation)}$')

  return



# <-------------[GET SIMPLIFICATION]--------------> #

def getSimplification(expression):

  expression = parseExpression(expression)
  simplification = sp.simplify(expression)
  renderTeX(f'${sp.latex(simplification)}$')

  return



# <--------------[CALC EXPRESSION]----------------> #

def calcExpression(expression):

  expression = parseExpression(expression)
  answer = ne.evaluate(str(expression))

  return answer


print(plotGraph('y=3x','10','-10'))
