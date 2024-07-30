from turtle import*

speed(25)

#we want to paint a castle

#step 1 draw a rectangle

width(6)

color("black")

penup()
right(90)
forward(250)
right(90)
forward(50)
pendown()
right(90)
forward(400)
right(90)
forward(250)
right(90)
forward(400)
right(90)
forward(250)


#drawing a rectangle complete now lets start with the door


penup()
right(180)
forward(100)
pendown()

left(90)
forward(75)
right(45)
forward(40)
right(100)
forward(40)
right(125)
forward(50)

penup()
left(180)
forward(50)
pendown()
right(90)
forward(73)

# drawing the door is complete, now lets start drawing the windows.

penup()
left(180)
forward(250)
pendown()

forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
penup()
forward(100)
right(90)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)


#drawing the windows is complete now lets draw the roof

penup()
right(90)
forward(150)
left(90)
forward(50)
right(90)
pendown()
right(45)
forward(200)
right(98)
forward(170)

# the roof is complete now lets start adding the towers


penup()
left(180)
forward(50)
right(90)
forward(50)
right(35)
pendown()
forward(75)
right(92)
forward(475)
right(90)
forward(80)

penup()
right(90)
forward(475)
right(180)
pendown()
forward(70)
penup()
right(180)
forward(70)
pendown()
right(45)
forward(65)
right(99)
forward(60)

# First tower complete.

penup()

right(90)
forward(400)
right(90)
forward(200)
right(90)
left(85)
right(30)
forward(65)
right(90)
forward(45)
pendown()
forward(65)
right(90)
forward(70)
penup()
forward(400)
right(90)
pendown()
forward(65)
right(90)
forward(470)
right(45)
forward(65)
right(110)
forward(60)

# the towers are complete now lets start with the king and the queen


penup()
right(90)
forward(200)
left(70)
forward(400)
right(90)
forward(150)
right(95)
pendown()
forward(20)
right(20)
forward(20)
left(20)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
penup()
right(180)
forward(50)
right(90)
pendown()
forward(40)
penup()
right(180)
forward(65)
right(90)
pendown()
forward(30)
penup()
right(180)
forward(30)
right(90)
forward(50)
pendown()
circle(20)
penup()
right(180)
forward(30)
right(90)
forward(50)
left(90)
pendown()
forward(20)
right(90)
forward(30)
penup()
right(180)
forward(30)
forward(110)

right(90)
pendown()
forward(80)
right(180)
forward(80)
right(90)
forward(90)
right(90)
forward(40)
right(90)
forward(90)

penup()
right(90)
forward(30)
right(90)
forward(10)
pendown()
# writing Goa on the flag
width(2)

forward(15)
left(180)
forward(15)
left(90)
forward(20)
left(90)
forward(15)
left(90)
forward(10)
left(90)
forward(5)

penup()
right(180)
forward(35)
right(90)
left(180)
pendown()
circle(10)


penup()

right(90)
forward(5)
right(90)
forward(10)
left(90)
forward(2)
pendown()
left(60)
forward(20)
right(120)
forward(20)
left(180)
forward(11)
left(65)
forward(10)
penup()
forward(10000)



exitonclick() 