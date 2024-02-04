import turtle
import random
import time

# Set up the turtle window
turtle.title("Click the Time-Counter Turtle Game")
turtle.bgcolor("white")
turtle.setup(width=600, height=400)

# Create the time-counter turtle
time_counter = turtle.Turtle()
time_counter.shape("turtle")
time_counter.color("blue")
time_counter.speed(0)
time_counter.penup()
time_counter.goto(0, -150)

# Create the score turtle
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-280, 160)

# Set up the score and time
score = 0
game_time = 30  # seconds

# Function to move the time-counter turtle left
def move_left():
    x = time_counter.xcor()
    x -= 20
    if x < -290:
        x = -290
    time_counter.setx(x)

# Function to move the time-counter turtle right
def move_right():
    x = time_counter.xcor()
    x += 20
    if x > 290:
        x = 290
    time_counter.setx(x)

# Function to handle clicking on the time-counter turtle
def on_click(x, y):
    global score
    if time_counter.distance(x, y) < 20:
        score += 10
        update_score()
        move_time_counter()

# Function to update the score display
def update_score():
    score_turtle.clear()
    score_turtle.write("Score: {}".format(score), align="left", font=("Arial", 16, "normal"))

# Function to move the time-counter turtle to a random position
def move_time_counter():
    x = random.randint(-290, 290)
    y = random.randint(-140, 140)
    time_counter.goto(x, y)

# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

# Mouse click event
turtle.onscreenclick(on_click)

# Initial score display
update_score()

# Main game loop
start_time = time.time()

while time.time() - start_time < game_time:
    turtle.update()

# Display final score
score_turtle.clear()
score_turtle.goto(0, 0)
score_turtle.write("Game Over\nFinal Score: {}".format(score), align="center", font=("Arial", 20, "normal"))
turtle.mainloop()
