
# Define basic regression formula

def get_y(m, b, x):
    y = m * x + b
    return y


# Calculate error for a data point

def calculate_error(m, b, point):
    x_point, y_point = point
    return abs(get_y(m, b, x_point) - y_point)


# Calculate the total error for all points

def total_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error


# Find best slope (m) and intercept (b) by trial and error

possible_ms = [i * 0.1 for i in range(-100, 100)]
possible_bs = [i * 0.1 for i in range(-200, 200)]

def best_fit(datapoints):
    smallest_error = float('inf')
    best_m = 0
    best_b = 0
    for m in possible_ms:
        for b in possible_bs:
            all_error = total_error(m, b, datapoints)
            if all_error < smallest_error:
                best_m = m
                best_b = b
                smallest_error = all_error
    best_m = round(best_m, 3)
    best_b = round(best_b, 3)
    smallest_error = round(smallest_error, 3)
    print('Best m =', best_m, ' Best b =', best_b, ' Smallest error =', smallest_error)
    return best_m, best_b, smallest_error
