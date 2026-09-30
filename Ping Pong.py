import turtle

wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.penup()
player1.goto(-350,0)
player1.color("red")
player1.shapesize(stretch_wid= 3, stretch_len= 0.5)

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.penup()
player2.goto(350,0)
player2.color("blue")
player2.shapesize(stretch_wid= 3, stretch_len= 0.5)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball.color("white")
ball.shapesize(stretch_wid= 0.5)
ball.dx = 0.1
ball.dy = 0.1

score =turtle.Turtle()
score1 = 0
score2 = 0
score.speed(0)
score.penup()
score.goto(0,260)
score.color("white")
score.hideturtle()
score.write("Player 1: {}      Player 2: {}".format(score1,score2), align= "center", font=("courier", 15, "normal"))



def player1_up():
    y = player1.ycor()
    y += 20
    if y <= 290 and y >= -290:
         player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 20
    if y <= 290 and y >= -290:
        player1.sety(y)

def player2_up():
    y = player2.ycor()  
    y += 20 
    if y <= 290 and y >= -290:
        player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 20
    if y <= 290 and y >= -290:
        player2.sety(y)

wind.listen()
wind.onkeypress(player1_up, "w")
wind.onkeypress(player1_down, "s")
wind.onkeypress(player2_up, "Up")
wind.onkeypress(player2_down, "Down")

while True:
    wind.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {}      Player 2: {}".format(score1,score2), align= "center", font=("courier", 15, "normal"))


    if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score2 += 1
            score.clear()
            score.write("Player 1: {}      Player 2: {}".format(score1,score2), align= "center", font=("courier", 15, "normal"))



    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 20 and ball.ycor() > player2.ycor() -20):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 20 and ball.ycor() > player1.ycor() -20):
        ball.dx *= -1
        ball.setx(-340)

    