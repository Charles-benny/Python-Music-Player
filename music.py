from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os
from PIL import Image, ImageTk
from mutagen.mp3 import MP3  

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#000000")
root.resizable(False, False)

mixer.init()

# Functions
def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        playlist.delete(0, END)  
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_songs():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(music_name)
    mixer.music.play()
    music.config(text=music_name[0:-4])
    show_details(music_name)

def stop_music():
    mixer.music.stop()
    music.config(text="")

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def next_song():
    next_song = playlist.curselection()
    next_song = next_song[0] + 1
    next_song_name = playlist.get(next_song)
    mixer.music.load(next_song_name)
    mixer.music.play()
    playlist.selection_clear(0, END)
    playlist.activate(next_song)
    playlist.selection_set(next_song)
    music.config(text=next_song_name[0:-4])
    show_details(next_song_name)

def previous_song():
    previous_song = playlist.curselection()
    previous_song = previous_song[0] - 1
    previous_song_name = playlist.get(previous_song)
    mixer.music.load(previous_song_name)
    mixer.music.play()
    playlist.selection_clear(0, END)
    playlist.activate(previous_song)
    playlist.selection_set(previous_song)
    music.config(text=previous_song_name[0:-4])
    show_details(previous_song_name)

def remove_song():
    selected_song = playlist.curselection()
    playlist.delete(selected_song[0])

def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

def show_details(song):
    file_data = os.path.splitext(song)
    if file_data[1] == '.mp3':
        audio = MP3(song)
        total_length = audio.info.length
    else:
        total_length = mixer.Sound(song).get_length()
    
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    track_duration.config(text="Duration: " + timeformat)

# Icons and Images
icon_image = Image.open("LOGO.jpg")
image_icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, image_icon)

top_image = Image.open("TOP.png")
top_image = top_image.resize((1120, 190))
Top = ImageTk.PhotoImage(top_image)
Label(root, image=Top, bg="#000000").place(x=0, y=0)

logo_image = Image.open("logo.jpg")
logo_image = logo_image.resize((120, 120))
Logo = ImageTk.PhotoImage(logo_image)
Label(root, image=Logo, bg="#000000").place(x=55, y=55)

menu_image = Image.open("DISPLAY.jpg") 
menu_image = menu_image.resize((550, 250))
Menu = ImageTk.PhotoImage(menu_image)
Label(root, image=Menu, bg="#000000").pack(padx=10, pady=120, side=RIGHT)

# Music frame
music_frame = Frame(root, bd=2, relief=RIDGE, bg="#fff")
music_frame.place(x=360, y=220, width=550, height=240)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("verdana", 11), bg="#fff", fg="black", 
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH, expand=True)

# Buttons
Button(root, text="Open Folder", width=15, height=2, font=("verdana", 11, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=700, y=470)

play_image = Image.open("PLAY.png")
play_image = play_image.resize((90, 90))
play_button = ImageTk.PhotoImage(play_image)
Button(root, image=play_button, bg="#000000", bd=0, command=play_songs).place(x=100, y=390)

stop_image = Image.open("STOP.png")
stop_image = stop_image.resize((60, 60))
stop_button = ImageTk.PhotoImage(stop_image)
Button(root, image=stop_button, bg="#000000", bd=0, command=stop_music).place(x=340, y=500)

resume_image = Image.open("RESUME.png")
resume_image = resume_image.resize((90, 90))
resume_button = ImageTk.PhotoImage(resume_image)
Button(root, image=resume_button, bg="#000000", bd=0, command=resume_music).place(x=100, y=520)

pause_image = Image.open("PAUSE.png")
pause_image = pause_image.resize((60, 60))
pause_button = ImageTk.PhotoImage(pause_image)
Button(root, image=pause_button, bg="#000000", bd=0, command=pause_music).place(x=270, y=500)

next_image = Image.open("NEXT.png")
next_image = next_image.resize((60, 60))
next_button = ImageTk.PhotoImage(next_image)
Button(root, image=next_button, bg="#000000", bd=0, command=next_song).place(x=200, y=500)

previous_image = Image.open("PREVIOUS.png")
previous_image = previous_image.resize((60, 60))
previous_button = ImageTk.PhotoImage(previous_image)
Button(root, image=previous_button, bg="#000000", bd=0, command=previous_song).place(x=30, y=500)

remove_image = Image.open("REMOVE.png")
remove_image = remove_image.resize((60, 60))
remove_button = ImageTk.PhotoImage(remove_image)
Button(root, image=remove_button, bg="#000000", bd=0, command=remove_song).place(x=410, y=500)

volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, bg="#000000", fg="white", bd=0, label="Volume", command=set_volume)
volume_slider.set(50)
volume_slider.place(x=500, y=500)

music = Label(root, text="", font=("verdana", 15), fg="white", bg="#000000")
music.place(x=500, y=600, anchor='center')

track_duration = Label(root, text="", font=("verdana", 12), fg="white", bg="#000000")
track_duration.place(x=500, y=630, anchor='center')

# Developed by Akash Label
Label(root, text="Developed by: Akash J", font=("verdana", 8), fg="white", bg="#000000").place(relx=1.0, rely=1.0, anchor='se')

root.mainloop()
