import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
	tur.pu(80)
    elif letter == "A":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.right(180)
	tur.pu()
    elif letter == "B":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(60)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.left(180)
        tur.forward(30)
        tur.left(90)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(60)
        
    elif letter == "C":
	tur.pu()
        tur.fd(5)
        tur.fd(5)
        tur.pd()
        tur.right(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(60)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(20)
    elif letter == "D":
        tur.pu()
        tur.left(90)
        tur.fd(5)
        tur.fd(5)
        tur.pd()
        tur.fd(60)
        tur.right(90)
        tur.circle(-30,180)
        tur.pu()
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(50)
    elif letter == "E":
        tur.pu()
        tur.left(90)
        tur.fd(5)
        tur.fd(5)
        tur.pd()
        tur.fd(60)
        tur.right(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(30)
    elif letter == "F":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.right(180)
        tur.fd(60)
        tur.right(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.pu()
        tur.right(180)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(60)
    elif letter == "G":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.circle(-60,300)
        tur.pu()
        tur.left(30)
        tur.fd(60)		
    elif letter == "H":
	tur.right(90)
        tur.fd(80)
        tur.right(180)
        tur.fd(40)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(40)
        tur.right(180)
        tur.fd(80)
	tur.pu()
    elif letter == "I":
        tur.fd(70)
        tur.right(180)
        tur.fd(35)
        tur.right(270)
        tur.fd(80)
        tur.right(90)
        tur.fd(35)
        tur.right(180)
        tur.fd(70)
	tur.pu()
    elif letter == "J":
        tur.fd(70)
        tur.right(180)
        tur.fd(35)
        tur.right(270)
        tur.fd(80)
        tur.right(45)
        tur.fd(10)
        tur.right(45)
        tur.fd(15)
        tur.right(45)
        tur.fd(15)
	tur.pu()
    elif letter == "K":
	tur.right(90)
        tur.fd(80)
        tur.right(180)
        tur.fd(40)
        tur.right(45)
        tur.fd(60)
        tur.right(180)
        tur.fd(60)
        tur.right(-90)
        tur.fd(60)
	tur.pu()
    elif letter == "L":
	tur.right(90)
        tur.fd(120)
        tur.right(-90)
        tur.fd(80)
	tur.pu()
    elif letter == "M":
	tur.right(270)
        tur.fd(80)
        tur.right(180)
        tur.right(-45)
        tur.fd(40)
        tur.right(-90)
        tur.fd(40)
        tur.right(135)
        tur.fd(80)
	tur.pu()
    elif letter == "N":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(50)
        tur.pd()
        tur.right(180)
        tur.fd(40)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(40)
        tur.pu()
        tur.right(180)
        tur.fd(50)
        tur.right(90)
    elif letter == "O":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.pu()
        tur.right(90)
        tur.fd(50)
        tur.right(90)
    elif letter == "P":
      
        tur.pd()
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(180)
        tur.fd(80)
        tur.pu()
        tur.right(180)
        tur.fd(80)
        tur.right(90)
        tur.fd(50)
    elif letter == "Q":
       
        tur.pd()
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(180)
        tur.fd(40)
        tur.left(90)
        tur.fd(55)
    elif letter == "R":
	 tur.pu()
        tur.right(90)
        tur.fd(60)
        tur.left(90)
        
        tur.pd()
        tur.left(90)
        tur.fd(80)
        tur.right(90)  #
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.left(140)
        tur.fd(60)
        tur.left(180)
        tur.fd(60)
        tur.right(50)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.pu()
	    
    elif letter == "S":
	tur.pu()
        tur.fd(60)
        tur.right(180)
        tur.pd()
        tur.fd(40)
        tur.left(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(180)
        tur.fd(40)
        tur.left(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        tur.pu()

    elif letter == "T":
	tur.pu()
        tur.fd(60)
   
        tur.pd()
        tur.left(180)
        tur.fd(40)
        tur.left(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(80)
        tur.left(180)
        tur.fd(80)
        tur.right(90)
        tur.fd(20)
        tur.pu()
	   
    elif letter == "U":
	tur.pu()
        tur.fd(20)
        tur.right(90)
       
        tur.pd()
        tur.fd(80)
        tur.left(90)
        tur.fd(60)
        tur.left(90)
        tur.fd(80)
        tur.right(90)
        tur.pu()
	   
    elif letter == "V":
	tur.pu()
        tur.fd(20)

        tur.pd()
        tur.right(60)
        tur.fd(90)
        tur.left(120)
        tur.fd(90)
        tur.right(60)
	    
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
