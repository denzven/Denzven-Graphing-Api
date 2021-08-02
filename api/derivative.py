# importing the library
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
inputvar = input("hmmm: ")
# defining the function
def function(x):
	return eval(inputvar)

# calculating its derivative
def deriv(x):
	return derivative(function, x)

# defininf x-axis intervals
y = np.linspace(-10, 10, num=1000)

# plotting the function
plt.plot(y, function(y), color='purple', label='Function')

# plotting its derivative
plt.plot(y, deriv(y), color='green', label='Derivative')

# formatting
plt.legend(loc='upper left')
plt.grid(True)
plt.show()