# A program that creates a long list of counties, chosed from a short list of five counties. It then makes a pie chart of the counties.


# Author: Susan Collins

# import the NumPy library 
import numpy as np
import matplotlib.pyplot as plt

county_pool = np.array(["Sligo", "Monaghan", "Cork", "Clare", "Waterford"])
county_list_size = 1000

# The NumPy documentation states that the RandomState function used in lectures has be superseded by the Generator method.
# This method taken from https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html
# Seed the random number generator, for debugging purposes
rng = np.random.default_rng(seed=32)

# generate the long list of counties, representing some more than others
county_list = rng.choice(county_pool, size = county_list_size, p =[0.3, 0.25, 0.2, 0.15, 0.1])
# print(county_list)

# loop to count number of instances of each county in the generated county_list
county_frequency = []
for county in county_pool:
    county_sum = 0
    for entry in county_list:
        if entry == county:
            county_sum += 1
    county_frequency.append(county_sum)
# print(county_count_list)

# Generate the plot
plt.pie(county_frequency, labels=county_pool)
plt.title("County Distribution")
plt.show()
