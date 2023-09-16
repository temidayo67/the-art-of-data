import random
from collections import Counter
from statistics import median
from statistics import variance
import psycopg2

# Provided data
days_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
shirt_colors = {
    "MONDAY": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "TUESDAY": ["ASH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
    "WEDNESDAY": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
    "THURSDAY": ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "FRIDAY": ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
}

# 1. Calculate the mean color
all_colors = [color for day_colors in shirt_colors.values() for color in day_colors]
mean_color = max(set(all_colors), key=all_colors.count)
print(" 01. Mean Color:", mean_color)

# 2. Calculate the color mostly worn throughout the week
color_counts = Counter(all_colors)
most_worn_color = color_counts.most_common(1)[0][0]
print("02. Most Worn Color Throughout the Week:", most_worn_color)

# 3. Calculate the median color
color_counts = Counter(all_colors)
median_count = median(color_counts.values())

# Find the color(s) with the median count
median_colors = [color for color, count in color_counts.items() if count == median_count]
print("03. Median Color(s):", median_colors)

# 4. Calculate the variance of the colors
color_variance = variance([all_colors.count(color) for color in set(all_colors)])
print("04. Variance of the Colors:", color_variance)

# 5. Calculate the probability of choosing the color red
red_probability = color_counts["RED"] / len(all_colors)
print("05. Probability of Choosing Red:", red_probability)

# 6. To save the colors and their frequencies in a PostgreSQL database:
# Database connection parameters
db_params = {
    'dbname': 'shirt_color',
    'user': 'postgres',
    'password': '1234567890',
    'host': 'localhost',
    'port': '5432'
}

# Dictionary containing shirt colors data
shirt_frequency = {
    "MONDAY": [("GREEN", 2), ("YELLOW", 2), ("BROWN", 2), ("BLUE", 6),
               ("PINK", 2), ("ORANGE", 4), ("CREAM", 1), ("RED", 2), ("WHITE", 3)],
    "TUESDAY": [("ASH", 1), ("BROWN", 2), ("GREEN", 1), ("BLUE", 6),
                ("BLEW", 1), ("PINK", 1), ("ORANGE", 2), ("RED", 1), ("WHITE", 4)],
    "WEDNESDAY": [("GREEN", 2), ("YELLOW", 2), ("BROWN", 2), ("BLUE", 6),
                   ("PINK", 2), ("RED", 3), ("WHITE", 2)],
    "THURSDAY": [("BLUE", 6), ("GREEN", 1), ("WHITE", 3), ("BROWN", 1),
                  ("PINK", 1), ("YELLOW", 1), ("ORANGE", 2), ("CREAM", 1), ("RED", 2)],
    "FRIDAY": [("GREEN", 2), ("WHITE", 5), ("BROWN", 1), ("BLUE", 6),
               ("BLACK", 1), ("ORANGE", 1), ("RED", 4)]
}

try:
    # Establish a connection to the database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Iterate through the days and colors to execute the SQL statements
    for day, colors in shirt_frequency.items():
        for color, frequency in colors:
            # Define the SQL statement with placeholders
            sql_statement = """
                INSERT INTO shirt_colors (color, frequency)
                VALUES (%s, %s)
                ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency + shirt_colors.frequency;
            """
            
            # Execute the SQL statement with values
            cursor.execute(sql_statement, (color, frequency))
    
    # Commit the changes
    conn.commit()

except psycopg2.Error as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()


# 7. Recursive searching algorithm (binary search)
def recursive_search(arr, target, low, high):
    if low > high:
        return -1  # Element not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # Element found
    elif arr[mid] < target:
        return recursive_search(arr, target, mid + 1, high)
    else:
        return recursive_search(arr, target, low, mid - 1)

# 8. Generate a random 4-digit binary number and convert it to base 10
binary_number = ''.join(random.choice('01') for _ in range(4))
decimal_number = int(binary_number, 2)
print("08. Random 4-Digit Binary Number:", binary_number)
print("08. Converted to Base 10:", decimal_number)

# 9. Sum the first 50 Fibonacci numbers
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

first_50_fibonacci = fibonacci(50)
sum_fibonacci = sum(first_50_fibonacci)
print("09. Sum of the First 50 Fibonacci Numbers:", sum_fibonacci)
