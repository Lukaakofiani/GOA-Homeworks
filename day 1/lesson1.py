from turtle import * 


#we want to paint a house


#step 1: draw a square
speed(30)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(70) 

color("green")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(150, 150)
pendown()

color("brown")
begin_fill()
right(60)
forward(15)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(20)
end_fill()

penup()
goto(62, 180.5)
pendown()
begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

penup()
goto(-475, -150)
pendown()
begin_fill()
color("lightgreen")
right(90)
forward(945)
right(90)
forward(245)
right(90)
forward(945)
right(90)
forward(245)
end_fill()

color("brown")
penup()
goto(-260, -200)
pendown()
begin_fill()
forward(160)
right(90)
forward(77)
right(90)
forward(160)
right(90)
forward(77)
end_fill()
color("green")
penup()
goto(-260, -35)
pendown()
begin_fill()
forward(75)
right(90)
forward(150)
right(90)
forward(230)
right(90)
forward(150)
right(90)
forward(75)
end_fill()







exitonclick()