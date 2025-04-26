# A program that makes a list, called salaries, that has random numbers (20000 – 80000); then makes a list called ages that has 100 random values (range:21 to 65), and makes a scatter plot of this data - salary versus age. 

# Author: Susan Collins

# import the NumPy library 
import numpy as np
import matplotlib.pyplot as plt

# set parameters for age generation
age_min = 21
age_max = 65
n_ages= 100

# set parameters for salary generation
salary_min = 20000
salary_max = 100000
n_salaries = 100

# Seed the random number generator, for debugging purposes
np.random.seed(1)

# generate the list of ages
ages = np.random.randint(age_min, age_max,n_ages)
# generate the list of salaries
salaries = np.random.randint(salary_min, salary_max,n_salaries)

# generate the plot
plt.scatter(ages,salaries)

# display the plot
plt.show()

