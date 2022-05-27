from tkinter import *

import random
import os

FRAMERATE=20
SCORE=-1

def center(toplevel):
    toplevel.update_idletasks()
    w= toplevel.winfo_screenwidth()
    h= toplevel.winfo_screenheight()
    size=tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y=h/2-size[1]/2-35
    toplevel.geometry("%dx%d+%d+%d" % (size+(x,y)))
main = Tk()
main.resizable(width = False,height= False)

main.title("Flappy Birds")
main.geometry('550x700')

center(main)

BIRD_Y = 200
PIPE_X = 550
PIPE_HOLE = 0

NOW_PAUSE = False
BEST_SCORE = 0

if os.path.isfile("data.dat"):
    scoreFile = open('data.dat')
    BEST_SCORE = int(scoreFile.read())
    scoreFile.clode()
else:
    scoreFile = open('data.dat', 'w')
    scoreFile.write(str(BEST_SCORE))
    scoreFile.close()

w=Canvas(main,width=550, height=700, background='blue',bd=0,hightlightthickness=0)

w.pack()
birdImg=PhotoImage(file = '...')
bird=w.create_image(100,BIRD_Y, image = birdImg)

up_count = 0

endRectangle = endBest = endBest = endScore = None

pipeUp = w.create_rectangle(PIPE_X,0,PIPE_X+100,PIPE_HOLE, fill='green', outline='black')
pipeDown = w.create_rectangle(PIPE_X,PIPE_HOLE+200,PIPE_X+100,700, fill='green', outline='black')

score_w = w.create_text(15,45,text='0', font = 'Impact 60', fill = 'white', anchor=W)

def generatePipeHole():
    global PIPE_HOLE
    global SCORE
    global FRAMERATE
    SCORE +=1
    w.itemconfig(score_w, text=str(SCORE))
    PIPE_HOLE = random.randint(50,500)
    if SCORE +1 % 7 == 0 and SCORE !=0:
        FRAMERATE -=1

main.loop()