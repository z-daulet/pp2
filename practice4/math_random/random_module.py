import random
import math

# Example 1: Generate a random number between 1 and 10
print("Example 1 - Random number between 1 and 10:")
random_num = random.randint(1, 10)
print(f"Random number: {random_num}")

# Example 2: Calculate square root using math module
print("\nExample 2 - Square root using math module:")
num = 16
sqrt_result = math.sqrt(num)
print(f"Square root of {num}: {sqrt_result}")

# Example 3: Select a random item from a list
print("\nExample 3 - Random choice from list:")
colors = ["red", "blue", "green", "yellow", "purple"]
random_color = random.choice(colors)
print(f"Random color: {random_color}")

# Example 4: Calculate pi and circle area using math module
print("\nExample 4 - Circle area using math.pi:")
radius = 5
circle_area = math.pi * radius ** 2
print(f"Circle area with radius {radius}: {circle_area}")
