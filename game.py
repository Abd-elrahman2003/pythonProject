import turtle
wind = turtle.Screen() # intialize the screen
wind.title("bing bong boda") # name of game
wind.bgcolor("skyblue") #color of back ground
wind.setup(width=800 , height=600) #width and height of game
wind.tracer(0) # stop update auto

#madrab1
madrab1 = turtle.Turtle() #intializes turtle method
madrab1.speed(0) #speed of game
madrab1.shape("square") #shape of game
madrab1.color("blue")#color of game
madrab1.shapesize(stretch_wid=5 , stretch_len=1)#size of object
madrab1.penup()#stop object from drawing lines
madrab1.goto(-350 , 0)#position of object

#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5 , stretch_len=1)
madrab2.penup()
madrab2.goto(350 , 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("green")
ball.shape("circle")
ball.penup()
ball.goto(0 , 0)
ball.dx = 0.25
ball.dy = 0.25
#scores
score1 = 0
score2 = 0


#score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1: {}  player 2: {}".format(score1 , score2), align="center" , font=("courier" , 24 , "normal"))


#functions
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)


def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

#keyboard binding
wind.listen()
wind.onkeypress(madrab1_up , "w")
wind.onkeypress(madrab1_down , "s")
wind.onkeypress(madrab2_up , "Up")
wind.onkeypress(madrab2_down , "Down")

#main game loop
while True:
    wind.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1



    if ball.xcor() > 390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {}  player 2: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= 1
        score2 += 1
        score.clear()
        score.write("player 1: {}  player 2: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    if (ball.xcor() == madrab1.xcor()+10) and (ball.ycor() <= madrab1.ycor() + 50) and (ball.ycor() >= madrab1.ycor() - 50):
        ball.dx *= -1
    if (ball.xcor() == madrab2.xcor()-10) and (ball.ycor() <= madrab2.ycor() + 50) and (ball.ycor() >= madrab2.ycor() - 50):
        ball.dx *= -1


