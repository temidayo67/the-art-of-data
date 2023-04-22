def add_two_numbers(a,b):
    x = a + b
    print(x)
add_two_numbers(10,20)
def area_of_circle(a):
    pi = 3.14
    area = pi * (a*a)
    print(area)
area_of_circle(2)

def add_all_nums(*args):
    sum = 0
    for arg in args:
        if isinstance(arg,(int,float)):
            sum += arg
        else:
            return "All arguments must be numbers"
    return sum
a = add_all_nums(5,4,"k")
print(a)

def convert_celsius_to_fahrenheit(c):
    f = (c * (9/5) + 32)
    print(f)

convert_celsius_to_fahrenheit(50)

def check_season(month):
    if month in ["January","February","December"]:
        return "Winter"
    elif month in ["March","April","May"]:
        return "Spring"
    elif month in ["June","July","August"]:
        return "Summer"
    elif month in ["September","October","November"]:
        return "Autumn"
    else:
        return "Invalid Month"
season = check_season("June")
print(season)
season2 = check_season("November")
print(season2)

def calculate_slope(x1,y1,x2,y2):
    return (y2 - y1)/(x2 - x1)
slope = calculate_slope(2,2,4,6)
print(slope)

import math
def solve_quadratic_equation(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -b /(2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1, x2]

solution_set = solve_quadratic_equation(3,-5,-7)
print(solution_set)
