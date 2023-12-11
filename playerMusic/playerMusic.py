
from pygame import mixer
from tkinter import *
import os



root = Tk() 
root.title('Music player')

def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()

def pausesong():
    mixer.music.pause()

def stopsong():
    mixer.music.stop()

def resumesong():
    mixer.music.unpause()

mixer.init() 
playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="red", font=('arial', 15), width=40) 
playlist.grid(columnspan=5)
os.chdir = os.listdir()
songs = os.listdir() 

for s in songs: 
    playlist.insert(END, s)

playbtn = Button(root, text="PLAY", command=playsong)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="PAUSE", command=pausesong)
pausebtn.grid(row=1, column=1)

stopbtn = Button(root, text="STOP", command=stopsong)
stopbtn.grid(row=1, column=2)

Resumebtn = Button(root, text="CONTINUER", command=resumesong)
Resumebtn.grid(row=1, column=3)

mainloop() 