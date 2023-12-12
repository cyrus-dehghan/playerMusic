import tkinter as tk
import os
import fnmatch 

from pygame import mixer


canvas=tk.Tk()
canvas.title("playerMusic")
canvas.geometry("500x600")
canvas.config(bg='darkblue')


rootpath ="C:\\Users\cyrus\Music\musique"
pattern ="*.mp3"

mixer.init()

prev_img=tk.PhotoImage(file="prev.png")
stop_img=tk.PhotoImage(file="stop.png")
play_img=tk.PhotoImage(file="play.png")
pause_img=tk.PhotoImage(file="pause.png")
next_img=tk.PhotoImage(file="next.png")

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def suivant():

    next_song =listBox.curselection()
    next_song= next_song[0]+1
    next_song_name=listBox.get(next_song)

    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def precedent():

    prev_song =listBox.curselection()
    prev_song= prev_song[0]-1
    prev_song_name=listBox.get(prev_song)

    label.config(text=prev_song_name)

    mixer.music.load(rootpath+"\\"+prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def pause():
    if pauseButton["text"]== "pause":
        mixer.music.pause()
        pauseButton["text"]= "play"

    else:
        mixer.music.unpause()
        pauseButton["text"]= "pause"




listBox=tk.Listbox(canvas, fg="white", bg="black", width= 100, font=('arial', 12))
listBox.pack(padx=15, pady=15)


label= tk.Label (canvas, text="", bg='darkblue', fg='black')
label.pack(pady=15)


top=tk.Frame(canvas, bg="darkblue")
top.pack (padx=15, pady= 10, anchor='center')


prevButton = tk.Button(canvas, text="prev", image=prev_img, bg='white', command=precedent)
prevButton.pack(pady=15, in_=top, side="left")

stopButton = tk.Button(canvas, text="stop", image=stop_img, bg='white', command=stop)
stopButton.pack(pady=15, in_=top, side="left")

playButton = tk.Button(canvas, text="play", image=play_img, bg='white', command=select)
playButton.pack(pady=15, in_=top, side="left")

pauseButton = tk.Button(canvas, text="pause", image=pause_img, bg='white', command=pause)
pauseButton.pack(pady=15, in_=top, side="left")

nextButton = tk.Button(canvas, text="next", image=next_img, bg='white', command=suivant)
nextButton.pack(pady=15, in_=top, side="left")


for root, dirs, files in os.walk(rootpath):
    
    for filename in fnmatch.filter(files, pattern):

        listBox.insert("end", filename)

canvas.mainloop()