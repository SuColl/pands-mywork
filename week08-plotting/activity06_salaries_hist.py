# A program that makes a list, called salaries, that has random numbers (20000 – 80000), and plots a histogram of the salaries.

# Author: Susan Collins

# import the NumPy library 
import numpy as np
import matplotlib.pyplot as plt

# set parameters for salary generation
salary_min = 20000
salary_max = 100000
n_salaries = 100

# Seed the random number generator, for debugging purposes
np.random.seed(1)

# generate the list of salaries
salaries = np.random.randint(salary_min, salary_max,n_salaries)

'''
print (salaries)

# create list containing salaries increased by 5000
salaries_increased = salaries + 5000
print (salaries_increased)

# create list containing salaries increased by 5%
salaries_percent_increase = salaries * 1.05
print (salaries_percent_increase)
'''
# generate the plot
plt.hist(salaries)

# display the plot
plt.show()

