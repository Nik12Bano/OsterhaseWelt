# Turrtle Challange.py

# Import von den Paketen
import turtle
from gturtle import *

#Erweiterte Turtle def
t = turtle.Turtle()

#Definitionen von Gegenstäden:


#Defintition vom Blume
def flower():
    pd()
    setPenColor(color)
    setFillColor(color)
    startPath()
    repeat 6:
        repeat 10:
            back(1)
            right(18)
        left(120)
    fillPath()  
    pu()
    forward(90)

#Defintition vom Baum
def tree():
    pd()
    setLineWidth(15)
    setPenColor("brown")
    forward(75)
    setLineWidth(5)
    setPenColor("ForestGreen")
    setFillColor("ForestGreen")
    startPath()
    repeat 12:
        repeat 30:
            right(6)
            back(1)
        left(150) 
    fillPath()
    pu()

#Definition von Wolke
def cloud():
    pd()
    setPenColor("white")
    dot(60)
    forward(40)
    dot(90)
    forward(40)
    dot(60)
    forward(40)
    pu()

#Definition von Sonne   
def sun():
    pd()
    setPenColor("yellow")
    dot(90)
    repeat 30:
        pu()
        forward(30)
        pd()
        setPenColor("yellow")
        forward(50)
        back(80)
        left(12)

#Definition vom Ei
def egg(r):
    right(90)
    pd()
    startPath()
    turtle.right(45)
    for loop in range(2): 
        turtle.circle(r,90) 
        turtle.circle(r/2,90)
    right(225)
    fillPath()
    pu()

#Definition vom Bau des Osterhasen
def berg():
    setFillColor("green")
    startPath()
    leftArc(150, 45)
    rightArc(225, 90)
    leftArc(150, 45)
    fillPath()
    pu()
    back(252)
    left(90)
    pd()
    setPenColor("brown")
    setFillColor("brown")
    startPath()
    repeat 2:
        forward(40)
        left(90)
        forward(20)
        dot(45)
        forward(20)
        left(90)
    fillPath()
    forward(20)
    setPenColor ("gray")
    dot(10)
    pu()
    forward(20)
    left(90)
    forward(20)
    setPenColor("darkblue")
    dot(20)

#Platzierung aller Eier  
def egg1():
    #Platzierung Ei Nr.1
    left(90)
    forward(30)
    right(90)
    forward(255)
    setFillColor("DarkSlateBlue")
    egg(27)
    
    #Platzierung Ei Nr.2
    back(60)
    setFillColor("LimeGreen")
    egg(42)
    
    #Platzierung Ei Nr.3
    left(22)
    back(45)
    setFillColor("orchid")
    egg(16)
    
    #Platzierung Ei Nr.4
    left(22)
    back(50)
    setFillColor("orange")
    egg(35)
    
    #Platzierung Ei Nr.5
    right(10)
    back(35)
    setFillColor("tomato")
    egg(19)
    
    #Platzierung Ei Nr.6
    right(15)
    back(60)
    setFillColor("maroon")
    egg(48)
    
    #Platzierung Ei Nr.7
    right(10)
    back(45)
    setFillColor("DeepSkyBlue3")
    egg(21)
    
    #Platzierung Ei Nr.8
    right(15)
    back(45)
    setFillColor("MediumTurquoise")
    egg(33)
    
    #Platzierung Ei Nr.9
    right(15)
    back(60)
    setFillColor("grey")
    egg(45)
    
    #Platzierung Ei Nr.10
    right(10)
    back(45)
    setFillColor("LawnGreen")
    egg(18)
    
    #Platzierung Ei Nr.11
    right(10)
    back(45)
    setFillColor("LightGoldenrod")
    egg(39)
    
    #Platzierung Ei Nr.12
    back(20)
    left(41)
    back(55)
    setFillColor("IndianRed")
    egg(25)
    
    #Platzierung Ei Nr.13
    back(65)
    setFillColor("red")
    egg(50)
    
    #Platzierung Ei Nr.14
    back(55)
    setFillColor("peru")
    egg(31)
    
    #Platzierung Ei Nr.15
    back(65)
    setFillColor("GreenYellow")
    egg(46)
    
    #Platzierung Ei Nr.16
    back(42)
    setFillColor("VioletRed")
    egg(22)
    
    #Platzierung Ei Nr.17
    back(35)
    setFillColor("LightSalmon")
    egg(size)
    
    #Platzierung Ei Nr.18
    back(60)
    setFillColor("LightCoral")
    egg(44)
    
    back(45)
    right(90)
    tree()
    back(75)
    left(90)
    setPenColor("black")
    setLineWidth(0.1)
    
    #Platzierung Ei Nr.19
    back(50)
    setFillColor("LightSeaGreen")
    egg(29)
    
    #Platzierung Ei Nr.20
    back(42)
    setFillColor("red")
    egg(24)
    
    #Platzierung Ei Nr.21
    back(35)
    setFillColor("OliveDrab")
    egg(20)
    
    #Platzierung Ei Nr.22
    back(45)
    setFillColor("DarkGoldenrod")
    egg(32)
    
    #Platzierung Ei Nr.23
    back(55)
    setFillColor("RoyalBlue")
    egg(40)
    
    #Platzierung Ei Nr.24
    back(42)
    setFillColor("khaki")
    egg(23)
    
    #Platzierung Ei Nr.25
    back(60)
    setFillColor("sienna")
    egg(41)
    
    #Platzierung Ei Nr.26
    back(55)
    setFillColor("OrangeRed")
    egg(30)
    
    #Platzierung Ei Nr.27
    back(55)
    setFillColor("GreenYellow")
    egg(36)
    
    #Bewegung zur Platzierung der unteren Eier
    right(90)
    back(80) 
    right(90)
    fd(50)
    back(150)
    right(180)
    
    #Platzierung Ei Nr.28
    back(50)
    setFillColor("VioletRed")
    egg(34)
    
    #Platzierung Ei Nr.29
    back(60)
    setFillColor("red")
    egg(43)
    
    #Platzierung Ei Nr.30
    back(55)
    setFillColor("LightSalmon")
    egg(37)
    

#Startet das Programm und kontrolliert die Geschwindigkeit:
makeTurtle()
speed(-1)

#Variablesetzung:
size = 17

#Wilkommens Text:
print("------------------------------------------------------------------------------------------")
print("Turtle-Challenge: Die Heimat des Osterhasen")
print("BY Nikolai & Andrej")
print("Hinweis: Für die Beste Erfahrung, setzte das Programm ins Vollbild!")
print("ACHTUNG: Achte darauf, dass dein Screen im Format 16:9 ist.")
print("d.h.: Bei einem PC / Mac funktioniert es nicht. (bzw. Schließe ein externes Display an!)")
print("------------------------------------------------------------------------------------------")
input("Bitte dieses Programm nicht als Eigenes ausgeben und / oder Fremdem Namen ausgeben. &copy Nikolai und Andrej Falls Sie mit diesen Bedingungen einverstanden sind, drücken Sie ENTER!")

#Hintergrund
setPenColor("SkyBlue")
dot(69420)

#Fläche für das Gras
pu()
left(90)
moveTo(650, -300)
pd()
setLineWidth(300)
setPenColor("green")
forward(1345)

#Platzierung Baum 1
pu()
right(90)
forward(158)
pd()
tree()

#Platzierung der Sonne
forward(300)
right(90)
forward(45)
left(90)
pd()
sun()

#Platzierung des Hügels
pu()
setPenColor("green")
back(400)
right(90)
pd()
berg()
pu()

#Setzt die Farbe der Außenlinie für alle Eier
setPenColor("black")
setLineWidth(0.1)

#Setzt alle Eier
egg1()

#Setzt 2 Wolken
right(90)
forward(400)
left(90)
repeat 3:
    forward(250)
    cloud()
    
#Blumen
left(90)
forward(470)
left(90)
back(400)
repeat 4:
    colors = ["red", "MediumOrchid", "khaki", "DeepPink", "turquoise"]
    for color in colors:
        flower()
        
