
Simple_Linear_Regression is a Python program that will use a default list of possible slope and intercept values
to find the best slope and intercept values that fit a given list of data points. To find the best values, the least
total error is used.

The program can be run by calling the best_fit() function, which takes a list of x,y data points as a parameter.
best_fit() will return the best slope and intercept values as well as the smallest error.

Default possible slope (m) values are a range of values from -10 to 10, in increments of 0.1
Default possible intercept (b) values are a range of values from -20 to 20, in increments of 0.1

Example:

datapoints = [(1, 3), (5, 7), (2, 4), (4, 6), (6, 7), (4, 4), (6, 8), (8, 5), (9, 9)]

regr = best_fit(datapoints)

output will be: Best m = 0.7  Best b = 2.7  Smallest error = 7.8

The best slope (m) value, intercept (b) and smallest error will be automatically printed.
