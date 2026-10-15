# Bobby Williams
# 10/15/2026
# Use a for loop and a while loop to create a tiny house

import turtle

# Set up the window and drawing object (turtle)
window = turtle.Screen()
luther = turtle.Turtle()

luther.pensize(3)
luther.pencolor("black")

# for loop tp deaw a square
for side in range(4):
    luther.forward (200)
    luther.right(90)

# while loop that draws a triangle 
num = 1
while num <= 3: 
    # Draw a side
    luther.forward(200)
    luther.left(120)
    # Increment num
    num = num + 1 


# keep window open
window.mainloop()