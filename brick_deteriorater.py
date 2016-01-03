from tkinter import *
from random import *
from time import *

root = Tk()
screen = Canvas( root, height = 700, width = 1200, background = "black")
screen.pack()

boxsize = 50 

xBall1 = 50 #starting points of the ball
xBall2 = 60
yBall1= 400
yBall2 = 410
xincrement = 1
yincrement = 1

xPlatform1 = 375 #starting points of the platform
xPlatform2 = 425

bricksx = [] #array that will be filled with every pixel in the x plane that touches a brick
bricksy = [] #array that will be filled with every pixel in the y plane that touches a brick

platform = screen.create_rectangle(xPlatform1, 600, xPlatform2, 610, fill = "green") #draws the platform initially

ball = screen.create_oval(xBall1, yBall1, xBall2, yBall2, fill = "green") #draws the ball initially

boxes = [] #array that will the filled with the uppermost and lowermost corners of the individual boxes

x1 = 50 #coordinates of the first box
y1 = 50
x2 = 100
y2 = 100

for z in range (0, 5): #loops through five times so that five rows of boxes are drawn
    x1 = 50 #resets the x positions so that the rows begin from the left hand side of the screen
    x2 = 100
    for i in range (0, 22):  #draws 22 boxes laterally in every row
        box = screen.create_rectangle(x1, y1, x2, y2, fill = "green", outline = "green") #draws the box
        x1 = x1 + boxsize #increases the x position by the boxsize so the boxes are equal
        x2 = x2 + boxsize
        x1la = x1-50 #made a variable for the x corner of the box that can be updated later without changing the position of the box
        for n in range (0, 50): #the length of the box is fifty, loops through for the entire length of each box
            x1la = x1la + 1 #adds one to the previously assigned label
            bricksx.append(x1la) #adds the pixel to the array with every pixel that touches the brick
            boxes.append(box) #adds the corner points of the box into the array that stores the boxes
    y1 = y1 + boxsize #updates the y position of the boxes after an entire row has been drawn
    y2 = y2 + boxsize
    y1la = y1-50 #a variable for the y corner of the box that can be updated without changing box position
    for q in range (0, 50): #height of the box is fifty, loops through for the entire height of the box
        y1la = y1la + 1 #adds one to previously assigned label
        bricksy.append(y1la)#adds the pixel to the array with every pixel that touches the brick

xPlatformNumero2 = xPlatform2 #making a variable that has the same value as the lower right corner of the box
xPlatformNumero = xPlatform1 #making a variable that has the same value as the lower left corner of the box
falt = [] #empty array that will be filled with every pixel that touches the platform ina given frame

def keyPressDetector( event ):
    global xPlatform1, xPlatform2, platform, falt, xPlatformNumero2, xPlatformNumero
    if event.keysym == "Right": #if the right key is pressed
        screen.delete(platform) #delete previoiusly drawn platform
        falt = [] #reset array to empty
        xPlatformNumero2 = xPlatform2 
        for q in range (0, 50): #loops through fifty times for the length of the platform
            xPlatformNumero2 = xPlatformNumero2 - 1 #takes the bottom right hand corner and subtracts one
            falt.append(xPlatformNumero2) #adds the pixel to the array with the platform pixels
        xPlatform1 = xPlatform1 + 10 #updates the x position of the platform to the right
        xPlatform2 = xPlatform2 + 10
        platform = screen.create_rectangle(xPlatform1+10, 600, xPlatform2, 610, fill = "green") #draws the platform
        screen.update()

    if event.keysym == "Left": #if the left key is pressed
        screen.delete(platform)#delete previoiusly drawn platform
        falt = [] #reset array to empty
        xPlatformNumero = xPlatform1
        for y in range (0, 50):#loops through fifty times for the length of the platform
            xPlatformNumero = xPlatformNumero + 1 #takes the bottom left hand corner and adds one
            falt.append(xPlatformNumero) #adds the pixel to the array with the platform pixels
        xPlatform1 = xPlatform1 - 10#updates the x position of the platform to the left
        xPlatform2 = xPlatform2 - 10
        platform = screen.create_rectangle(xPlatform1+10, 600, xPlatform2, 610, fill = "green")#draws the platform
        screen.update()
      
def ClickManager (event):
    global Click
    if event.x > 0 and event.y > 0: #if the mouse is clicked anywhere within the screen
        Click = True #set Click equal to True
    else:
        Click = False

def moveball():
    global xBall1, xBall2, yBall1, yBall2, xincrement, yincrement, ball, Qpressed, v, chibi
    v = 0 #a variable used as a counter or index during a while loop
    while True:
        screen.delete(ball)
        xBall1 = xBall1 + xincrement #updates the position of the ball by the constant increment
        xBall2 = xBall2 + xincrement
        yBall1 = yBall1 + yincrement
        yBall2 = yBall2 + yincrement
        ball = screen.create_oval(xBall1, yBall1, xBall2, yBall2, fill = "green") #draws the ball
        sleep(0.01) #creates a pause between frames so that there is time to react
        screen.update()
        v = (v + 1) % len(boxes) #increases the looping variable by one and finds the remainder when divided by the length of the boxes array
        direction = 0 #creates a variable that will determine which direction of the ball whhen it hits a brick
        if xBall2 > 1200: #if the ball hits the right wall
            xincrement = xincrement*(-1) #return the ball in the opposite direction at the same angle
            direction = 1
            
        if xBall1 < 0: #if the ball hits the left wall
            xincrement = xincrement*(-1) #return the ball in the opposite direction at the same angle
            direction = 1
            
        if yBall2 > 600 and yBall1 < 600 and xBall1 in (falt): #if the ball hits platform by hitting the top of the platform and in the range of the pixels at a certain frame(otherwise it will continue to fall)
            yincrement = yincrement*(-1) #return the ball in the opposite direction at the same angle
            direction = 0
            
        if yBall1 < 0: #if the ball hits the top wall
            yincrement = yincrement*(-1) #return the ball in the opposite direction at the same angle
            direction = 0
            
        if xBall1 in (bricksx) or xBall2 in (bricksx): #if the ball hits the bricks in the x plane
            if yBall1 in (bricksy) or yBall2 in (bricksy): #if the ball hits the bricks in the y plane
                if direction == 1: #if the direction is positive one
                   xincrement = xincrement*(-1) #reverse the x increment
                if direction == 0: #if the direction control is zero
                    yincrement = yincrement*(-1) #reverse the y increment
                screen.delete(boxes[v]) #delete the brick for which the looping variable decides
def EndGame(): #a procedure to end the game
    global platform, ball, boxes
    screen.delete(boxes) #delete every box
    screen.delete(ball) #delete the ball
    screen.delete(platform) #delete the platform
                
def runGame():
    moveball() #calls moveball() procedure
    if Click == True: #if the screen has been clicked
        EndGame() #call EndGame() procedure
        
screen.bind( "<Key>",  keyPressDetector ) #determines if keyboard controls are performed
screen.bind("<Button-1>", ClickManager ) #determined if mouse controls are performed
screen.focus_set()
runGame() #calls the runGame() procedure

screen.pack()
root.mainloop()
