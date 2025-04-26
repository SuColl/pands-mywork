# A program that plots the function y = x^2.
# Author: Susan Collins

# import the NumPy library 
import numpy as np
import matplotlib.pyplot as plt


# set the independent values (x-values)
# x_values = list(range(1,100,1))       #can't use this method as cannot perform multiplication on a standard python list
x_values = np.arange(1,100,1)
print(x_values)

# calculate the y-values (y = x^2)
y_values = x_values * x_values


# generate the plot
plt.plot(x_values, y_values)

# display the plot
plt.show()
