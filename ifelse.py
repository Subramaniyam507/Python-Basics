print("learning if else statements in python")
import turtle
window=turtle.Screen


subbu=turtle.Turtle()
def squareturtle():
   
    subbu.forward(100)
    subbu.right(90)
    subbu.forward(100)
    subbu.right(90)
    subbu.forward(100)
    subbu.right(90)
    subbu.forward(100)
    
    input("press any key to exit")   
 
elephant_weight=3000
my_weight=68



def checking_blocks():
   if my_weight>elephant_weight:
    squareturtle()
   else:
    subbu.forward(100)

checking_blocks()
input("press any key to exit")
