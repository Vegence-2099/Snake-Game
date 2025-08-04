import turtle
import random
import time

# ——— Setup screen ———
screen = turtle.Screen()
screen.title('WELCOME TO SNAKE GAME')
screen.setup(width=900, height=650)
screen.bgcolor('turquoise')
screen.tracer(0)

# ——— Draw border ———
border = turtle.Turtle()
border.hideturtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
for _ in range(2):
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
border.penup()

# ——— Game state ———
score = 0
delay = 0.1
old_fruit = []

# ——— Snake head ———
snake = turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color('black')
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# ——— Food ———
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

# ——— Score display ———
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color('black')
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write(f"Score: {score}", align="center", font=("Pattaya-Regular", 24, "bold"))

# ——— Movement functions ———
def go_up():
    if snake.direction != 'down':
        snake.direction = 'up'

def go_down():
    if snake.direction != 'up':
        snake.direction = 'down'

def go_left():
    if snake.direction != 'right':
        snake.direction = 'left'

def go_right():
    if snake.direction != 'left':
        snake.direction = 'right'

def move_snake():
    x, y = snake.xcor(), snake.ycor()
    if snake.direction == 'up':
        snake.sety(y + 20)
    elif snake.direction == 'down':
        snake.sety(y - 20)
    elif snake.direction == 'left':
        snake.setx(x - 20)
    elif snake.direction == 'right':
        snake.setx(x + 20)

# ——— Keyboard bindings ———
screen.listen()
screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_right, 'Right')

# ——— Main game loop ———
game_over = False
while not game_over:
    screen.update()

    # — Food collision — 
    if snake.distance(fruit) < 20:
        # move fruit
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        # update score
        score += 1
        delay = max(0.01, delay - 0.001)
        scoring.clear()
        scoring.write(f"Score: {score}", align="center", font=("Pattaya-Regular", 24, "bold"))
        # grow snake
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape('square')
        new_seg.color('black')
        new_seg.penup()
        old_fruit.append(new_seg)

    # — Move tail segments — 
    for idx in range(len(old_fruit)-1, 0, -1):
        x_prev = old_fruit[idx-1].xcor()
        y_prev = old_fruit[idx-1].ycor()
        old_fruit[idx].goto(x_prev, y_prev)
    if old_fruit:
        old_fruit[0].goto(snake.xcor(), snake.ycor())

    # — Move the snake — 
    move_snake()

    # — Border collision — 
    if (snake.xcor() > 280 or snake.xcor() < -300 or
        snake.ycor() > 240 or snake.ycor() < -240):
        game_over = True

    # — Self collision — 
    for seg in old_fruit:
        if seg.distance(snake) < 20:
            game_over = True
            break

    time.sleep(delay)

# ——— After game over ———
# Hide snake and all segments
snake.hideturtle()
for seg in old_fruit:
    seg.hideturtle()

# Optionally hide the border if you drew it with a turtle named `border`
# border.hideturtle()

# Clear only the score-display turtle
scoring.clear()

# Write Game Over text in the center
scoring.goto(0, 0)
scoring.write(f"GAME OVER\nYour Score: {score}",
              align="center",
              font=("Pattaya-Regular", 24, "bold"))

# Keep the window open
turtle.done()
