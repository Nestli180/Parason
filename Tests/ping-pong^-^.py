from tkinter import *
 import random

WIDTH = 900
HEIGHT = 300
 

 

PAD_W = 10

PAD_H = 100
 

BALL_RADIUS = 30
BALLX_CHANGE = 20
BALLY_CHANGE = 0
BALL_SPEED_UP = 1.05
BALL_SPEED_MAX = 40
BALLX_SPEED = 20
BALLY_SPEED = 20

PAD_SPEED = 20
LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0

right_line_distance()

root = Tk()
root.title("Шульський Назар")
 

c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()
 

 

c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")

c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="white")

c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="white")

 
BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+BALL_RADIUS/2, fill="white")
 
LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="yellow")
 
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, 
                          PAD_H, width=PAD_W, fill="yellow")
 
def move_ball():
    c.move(BALL,BALLX_CHANGE,BALLY_CHANGE)

def move_pads():
    PADS = {LEFT_PAD:LEFT_PAD_SPEED,
            RIGHT_PAD:RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad,0,PADS[pad])
        if c.coords(pad)[1] < 0:
            c.move(pad,0,-c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT: 
            c.move(pad,0,HEIGHT - c.coords(pad)[3])       

def bounce(action):
    global BALLX_SPEED, BALLY_SPEED
    if action == 'strike':
        BALLY_SPEED = random.randrange(-10,10)
        if abs(BALLX_SPEED) < BALL_SPEED_MAX:
            BALLX_SPEED*_ - BALL_SPEED_UP
        else:
            BALLX_SPEED = -BALL_SPEED_UP
    else:
        BALLY_SPEED = -BALLY_SPEED            
def move_ball():
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_centr = (ball_top + ball_bot)/2

    if ball_right + BALLX_SPEED < right_line_distance and ball_left + BALLX_SPEED > PAD_W:
        c.move(BALL, BALLX_SPEED,BALLY_SPEED)
    elif ball_right == right_line_distance==PAD_W:
        if ball_right> WIDTH/2:
            if c.coords(RIGHT_PAD)[1] < ball_centr < c.coords(RIGHT_PAD)[3]:
                bounce('strike')
            else:
                pass
            if c.coords(LEFT_PAD)[1] < ball_centr < c.coords(LEFT_PAD)[3]:
                bounce('strike')
            else:
                pass
        else:
            if ball_right > WIDTH/2:
                c.move(BALL, right_line_distance-ball)

def main():
    move_ball()
    move_pads()
    root.after(30, main)

c.focus_set()

def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == 'w':
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == 's':
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == 'Up':
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == 'Down':
        RIGHT_PAD_SPEED = PAD_SPEED
c.bind('<cKeyPress>')

main()
root.mainloop()    