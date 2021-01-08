from tkinter import *
import os
from playsound import playsound
import pygame


root = Tk()
root.title("Music Player")
root.geometry("1000x200")

pygame.mixer.init()
track = StringVar()
status = StringVar()

panel = LabelFrame(root, text="controls", width=255, height=110, bg="orange")
panel.place(x=0, y=100, width=605, height=105)

def pause():
    status.set("Paused")
    pygame.mixer.music.pause()


pause_b = Button(panel, text="PAUSE", command=pause, width=10, height=2, bg="white")
pause_b.grid(row=0, column=1, padx=15, pady=8)


def unpause():
    status.set("Unpause")
    pygame.mixer.music.unpause()


unpause_btn = Button(panel, text="UNPAUSE", command=unpause, width=10, height=2, bg="white")
unpause_btn.grid(row=0, column=2, padx=15, pady=8)


def stop():
    status.set("Stopped")
    pygame.mixer.music.stop()


stp_btn = Button(panel, text="STOP", command=stop, width=10, height=2, bg="white")
stp_btn.grid(row=0, column=3, padx=15, pady=8)
frame = LabelFrame(root, text="Song Track", bg="blue")
frame.place(x=0, y=0, width=605, height=105)

songstat = Label(frame, textvariable=status, font="bold", bg="green")
songstat.grid(row=0, column=1, padx=15, pady=8)



sng_lst = LabelFrame(root, text="Song List", width=250, height=200, bg="green")
sng_lst.place(x=600, y=0, width=400, height=200)

scroll = Scrollbar(sng_lst, orient=VERTICAL)

playlist = Listbox(sng_lst, yscrollcommand=scroll.set, selectbackground="gold", selectmode=SINGLE, font="bold")

scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=playlist.yview)
playlist.pack(fill=BOTH)

os.chdir("music")

songtracks = os.listdir()

for track in songtracks:
    playlist.insert(END, track)


def play():

    status.set(playlist.get(ACTIVE))
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()


play_b = Button(panel, text="PLAY", command=play, width=10, height=2, bg="white")
play_b.grid(row=0, column=0, padx=15, pady=8)


root.mainloop()