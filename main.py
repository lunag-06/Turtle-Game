"""
Program Name: Turtle     
Programmer Name: Luna Gao 
Program Date: June 17, 2023         
Program Description: A turtle game where you try to gain points by reaching targets
Program Input/output:
Input: Pressing arrow keys to move the turtle
Output: A window with a white background
        A green turtle controlled by the player
        A red circle target that moves to a random position when touched by the turtle
        A red X target that moves to a random position when touched by the turtle
        A scoring system where the player gains 1 point when the turtle touches the circle target and loses 1 point when the turtle touches the X target
        A display showing the player's score and the rules of the game
        A message displaying "YOU WIN" if the player reaches a score of 10 and "GAME OVER" if the player's score goes below 0
"""

# Import the turtle module for graphical visualization
import turtle
# Import the random module for generating random positions
import random

# Set up the screen
# Create a turtle screen object
screen = turtle.Screen()
# Set the background color of the screen to white
screen.bgcolor("white")

# Create the turtle
# Create a turtle object called "player"
player = turtle.Turtle()
# Create a turtle object called "player"
player.color("green")
# Set the shape of the player turtle to turtle
player.shape("turtle")

# Create the circle target
# Create a turtle object called "circle_target"
circle_target = turtle.Turtle()
# Set the color of the circle target turtle to red
circle_target.color("red")
# Set the shape of the circle target turtle to circle
circle_target.shape("circle")
# Lift up the turtle's pen to prevent drawing
circle_target.penup()
# Set the position of the circle target turtle to a random position within the given range
circle_target.setpos(random.randint(-200, 200), random.randint(-200, 200))

# Create the X target
# Create a turtle object called "x_target"
x_target = turtle.Turtle()
# Set the color of the x target turtle to red
x_target.color("red")
# Set the shape of the x target turtle to turtle
x_target.shape("turtle")
# Set the size of the x target turtle using shapesize to (1, 1)
x_target.shapesize(1, 1)
# Lift up the turtle's pen to prevent drawing
x_target.penup()
# Set the position of the x target turtle to a random position within the given range
x_target.setpos(random.randint(-200, 200), random.randint(-200, 200))

# Set up the scoring system
# Initialize the score to 0
score = 0
# Create a turtle object called "score_pen"
score_pen = turtle.Turtle()
# Set the speed of the score_pen turtle to 0 (fastest)
score_pen.speed(0)
# Set the color of the score_pen turtle to black
score_pen.color("black")
# Lift up the turtle's pen to prevent drawing
score_pen.penup()
# Hide the turtle icon
score_pen.hideturtle()
# Set the position of the score_pen turtle to (-240, 100)
score_pen.setpos(-240, 100)

# Display rules for player
score_pen.write("Avoid the Red Turtle", font=("Arial", 16, "normal"))

# Define the functions for moving the turtle
# Function to move the player turtle to the left by 30 degrees
def move_left():
    player.left(30)

# Function to move the player turtle to the right by 30 degrees
def move_right():
    player.right(30)

# Function to move the player turtle forward by 50 units
def move_forward():
    player.forward(50)

# Function to move the player turtle backward by 50 units
def move_backward():
    player.backward(50)

# Set up the screen's event handlers
# Set up the event handler for the "Left" key to call the move_left() function
screen.onkeypress(move_left, "Left")
# Set up the event handler for the "Right" key to call the move_right() function
screen.onkeypress(move_right, "Right")
# Set up the event handler for the "Up" key to call the move_forward() function
screen.onkeypress(move_forward, "Up")
# Set up the event handler for the "Down" key to call the move_backward() function
screen.onkeypress(move_backward, "Down")

# Start listening to key events
screen.listen()

# Main game loop
while True:
   # Move the player turtle forward by 1
    player.forward(1)
  # Check if the player turtle has touched the circle target
    if player.distance(circle_target) < 20:
         # Change the color of the circle target to purple
        circle_target.color("purple")
       # Move the circle target to a random position
        circle_target.setpos(random.randint(-200, 200), random.randint(-200, 200))
       # Increment the score by 1
        score += 1
        # Clear the score_pen turtle's drawing
        score_pen.clear()
       # Update the score_pen turtle's text with the new score
        score_pen.write("Score: {}".format(score), font=("Arial", 16, "normal"))

    # Check if the player turtle has touched the X target
    if player.distance(x_target) < 20:
          # Move the X target to a random position
        x_target.setpos(random.randint(-200, 200), random.randint(-200, 200))
      # Decrease the score by 1
        score -= 1
        # Clear the score_pen turtle's drawing
        score_pen.clear()
       # Update the score_pen turtle's text with the new score
        score_pen.write("Score: {}".format(score), font=("Arial", 16, "normal"))

   # Check if the score is equal to 10
    if score == 10:
      # Clear the score_pen turtle's drawing
      score_pen.clear()
        # Display the winning message
      score_pen.write("YOU WIN", font=("Arial", 16, "normal"))
       # End the game loop
      break

    # Check if the score is less than 0
    if score < 0:
      # Clear the score_pen turtle's drawing
      score_pen.clear()
      # Display the losing message
      score_pen.write("GAME OVER", font=("Arial", 16, "normal"))
      # End the game loop
      break

# End the turtle graphics window and terminate the program
turtle.done()
