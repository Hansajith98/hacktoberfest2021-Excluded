import os
from tkinter import *

from tkinter import ttk
from ttkthemes import themed_tk as tk

import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
import time
import threading

root = tk.ThemedTk()

root.get_themes()
root.set_theme("radiance")

mixer.init()  # initializing the mixer
root.title("Melody")
root.iconbitmap(r'images/melody.ico')

statusbar = Label(root, text="Wlcome To Melody", relief=SUNKEN, anchor=W, font="Times 15 italic")
statusbar.pack(side=BOTTOM, fill=X)

filelabel = ttk.Label(root, text='Welcome')
filelabel.pack()

lengthlabel = ttk.Label(root, text='Total Length - --:--')
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(root, text='Current Time - --:--', relief=GROOVE)
currenttimelabel.pack()

menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)

playlist = []


def brows_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)


def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label='Open', command=brows_file)
subMenu.add_command(label='Exit', command=root.destroy)


def About_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music player, build using python tkinter by Sudhanshu Vijay')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label='About Us', command=About_us)

right_frame = Frame(root)
right_frame.pack(side=RIGHT, pady=30)

left_frame = Frame(root)
left_frame.pack(side=LEFT, padx=30, pady=30)

top_frame = Frame(right_frame)
top_frame.pack()

playlistbox = Listbox(left_frame)
playlistbox.pack()

add_btn = ttk.Button(left_frame, text="+ Add", command=brows_file)
add_btn.pack(side=LEFT)


def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)


del_btn = ttk.Button(left_frame, text="- Del", command=del_song)
del_btn.pack(side=LEFT)


def show_details(play_song):
    filelabel['text'] = "Playing" + ' - ' + os.path.basename(play_song)
    file_data = os.path.splitext(play_song)
    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total Length" + ' - ' + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    global paused
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Current Length" + ' - ' + timeformat
            time.sleep(1)
            current_time += 1


def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed..."
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = "Playing Music..." + ' ' + os.path.basename(play_it)
            show_details(play_it)
        except:
            tkinter.messagebox.showerror('File Not Found', 'Melody Could Not Find The File. Please Check It Again')


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped..."


paused = FALSE


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused..."


def rewind_music():
    play_music()
    statusbar['text'] = "Music Rewinded..."


def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)


muted = FALSE


def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.5)
        volumeButton.configure(image=volume_photo)
        scale.set(50)
        muted = FALSE
    else:
        mixer.music.set_volume(0)
        volumeButton.configure(image=mute_photo)
        scale.set(0)
        muted = TRUE


middleframe = Frame(right_frame)
middleframe.pack(pady=30, padx=30)

play_photo = PhotoImage(file='images/play.png')
playButton = ttk.Button(middleframe, image=play_photo, command=play_music)
playButton.grid(row=0, column=0, padx=10)

stop_photo = PhotoImage(file='images/stop.png')
stopButton = ttk.Button(middleframe, image=stop_photo, command=stop_music)
stopButton.grid(row=0, column=1, padx=10)

pause_photo = PhotoImage(file='images/pause.png')
pauseButton = ttk.Button(middleframe, image=pause_photo, command=pause_music)
pauseButton.grid(row=0, column=2, padx=10)

bottomframe = Frame(right_frame)
bottomframe.pack(pady=10)

rewind_photo = PhotoImage(file='images/rewind.png')
rewindButton = ttk.Button(bottomframe, image=rewind_photo, command=rewind_music)
rewindButton.grid(row=0, column=0)

mute_photo = PhotoImage(file='images/mute.png')
volume_photo = PhotoImage(file='images/volume.png')
volumeButton = ttk.Button(bottomframe, image=volume_photo, command=mute_music)
volumeButton.grid(row=0, column=1)

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)
mixer.music.set_volume(0.5)
scale.grid(row=0, column=2, pady=15, padx=30)


def on_closing():
    stop_music()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
