# Bobby Williams
# 9/15/2026
# Calculate componets of a circle using pi from math library 

# Get radius from user
import math


radius = float(input("Enter the radius"))

print()

# Calculate diameter
diameter = 2 * radius

# Display the radius using an f-string
print(f"The diameter of the circle is {diameter:.1f}")

# Calculate circumference 
circumference = 2 * math.pi * radius

# Display cirdcumfrence using f-string
print(f"The circumference of the cirlce is {circumference:.2f}")

# Calculate the area
area = math.pi * math.pow(radius, 2)

# Display area with f-string
print(f"The area of the circle is {area:.3f}")