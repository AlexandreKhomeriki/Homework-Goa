from turtle import*



#we want to paint a house

#step 1: draw a square
width(7)
color("purple")
      
forward(200) 
left(90)

forward(200)
left(90)

forward(200) 
left(90)

forward(200)
left(90)
 #end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)

forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()
color("red")
begin_fill()

right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

penup()
left(45)
forward(20)
left(75)
forward(20)
pendown()
color("blue")
begin_fill() 
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
right(90)
forward(100)
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
exitonclick() 



#commit change