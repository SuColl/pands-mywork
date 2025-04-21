# Create a tuple that stores the months of the year, from that tuple create another tuple with just the summer months (May, June, July), print out the summer months one at a time.
# author: Susan Collins


# create tuple containing all months
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# get summer months
summer = months[4:7]

# print results
for month in summer:
    print(month)


