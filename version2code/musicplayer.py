import tkinter as tk
from tkinter.ttk import Progressbar
import customtkinter as ctk
import pygame
from threading import Thread
import json
import sys
import subprocess
import platform

# --- NEW: Get genre from command line argument or default ---
if len(sys.argv) > 1:
    selected_genre = sys.argv[1]
else:
    selected_genre = "tereo"  # fallback genre

# --- NEW: Load music data from JSON ---
def load_music_data():
    with open('data/music_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)['genres']

music_data = load_music_data()
songs = music_data.get(selected_genre, [])
if not songs:
    tk.messagebox.showerror("Error", f"No songs found for genre: {selected_genre}")
    sys.exit()

current_song_index = 0  # Track the current song

# Initialize the window
window = ctk.CTk()
window.title("Music Page")  # title 
window.geometry('540x725')  # dimension
window.resizable(width=0, height=0)  # non-resizable
window.eval('tk::PlaceWindow . center')  # Puts window in center of page
pygame.mixer.init()  # Initialize the mixer module
window.configure(border=10, relief="raised", bg="lightgrey")

# Load images
def get_cover(index):
    try:
        return tk.PhotoImage(file=songs[index]['cover'])
    except Exception:
        return tk.PhotoImage(width=500, height=300)  # fallback blank

coverphoto = get_cover(current_song_index)
LeftArrow = tk.PhotoImage(file="images/app_images/button_leftarrow.png")
DownArrow = tk.PhotoImage(file="images/app_images/button_downarrow.png")
RightArrow = tk.PhotoImage(file="images/app_images/button_rightarrow.png")

# --- NEW: Song and artist labels ---
song_title_var = tk.StringVar()
artist_name_var = tk.StringVar()
def update_labels():
    song = songs[current_song_index]
    song_title_var.set(song.get('title', 'Unknown Title'))
    artist_name_var.set(song.get('artist', {}).get('name', 'Unknown Artist'))

# Functions for Play, Pause, and Song Navigation
def play_song():
    song = songs[current_song_index]
    pygame.mixer.music.load(song['file'])
    pygame.mixer.music.play()
    update_cover()
    update_labels()
    threading_progress_bar()

def pause_song():
    pygame.mixer.music.pause()

def unpause_song():
    pygame.mixer.music.unpause()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song()

def threading_progress_bar():
    t1 = Thread(target=update_progress_bar)
    t1.start()

def update_progress_bar():
    song = songs[current_song_index]
    sound = pygame.mixer.Sound(song['file'])
    duration = sound.get_length()
    def update_progress(i):
        if i < int(duration):
            progress_bar.set(i / duration)
            window.after(1000, update_progress, i + 1)
    update_progress(0)

def set_volume(value):
    pygame.mixer.music.set_volume(float(value))

def update_cover():
    global coverphoto
    coverphoto = get_cover(current_song_index)
    label1.configure(image=coverphoto)
    label1.image = coverphoto

def show_artist_info():
    artist = songs[current_song_index].get("artist", {})
    with open("current_artist.json", "w", encoding="utf-8") as f:
        json.dump(artist, f)
    if platform.system() == "Windows":
        subprocess.Popen(["python", "artistprofile.py"])
    else:
        subprocess.Popen(["python3", "artistprofile.py"])

def return_home():
    window.destroy()
    if sys.platform.startswith("win"):
        subprocess.Popen(["python", "homepage.py"])
    else:
        subprocess.Popen(["python3", "homepage.py"])

# --- UI Layout (unchanged except for dynamic labels and info button) ---
# Return to Home Page Button (top left)
home_button = tk.Button(window, text="Home", command=return_home, bg="lightgrey", fg="blue", font=("Segoe Script", 10, "bold"))
home_button.place(x=10, y=10)

label1 = tk.Label(window, image=coverphoto)
label1.place(x=13, y=80)

# Song title and artist labels
song_title_label = tk.Label(window, textvariable=song_title_var, font=("Segoe Script", 14, "bold"), bg='lightgrey')
song_title_label.place(x=75, y=400)
artist_name_label = tk.Label(window, textvariable=artist_name_var, font=("Segoe Script", 12), bg='lightgrey')
artist_name_label.place(x=75, y=430)
update_labels()

# Arrow Buttons
button1 = tk.Button(window, image=LeftArrow, command=previous_song)
button1.place(x=0, y=450)
label2 = tk.Label(window, text="Previous Song", foreground="Blue", bg='lightgrey', font=("Segoe Script", 10, "bold"))
label2.place(x=30, y=530)

button2 = tk.Button(window, image=DownArrow, command=show_artist_info)
button2.place(x=180, y=450)
label3 = tk.Label(window, text="See More Information", foreground="Blue", bg='lightgrey', font=("Segoe Script", 10, "bold"))
label3.place(x=190, y=530)

button3 = tk.Button(window, image=RightArrow, command=next_song)
button3.place(x=360, y=450)
label4 = tk.Label(window, text="Next Song", foreground="Blue", bg='lightgrey', font=("Segoe Script", 10, "bold"))
label4.place(x=410, y=530)

# Play and Pause Buttons
play_button = tk.Button(window, text="Play", command=play_song, bg="green", fg="white", font=("Segoe Script", 10, "bold"))
play_button.place(x=225, y=585)

pause_button = tk.Button(window, text="Pause", command=pause_song, bg="red", fg="white", font=("Segoe Script", 10, "bold"))
pause_button.place(x=325, y=585)

unpause_button = tk.Button(window, text="Unpause", command=unpause_song, bg="blue", fg="white", font=("Segoe Script", 10, "bold"))
unpause_button.place(x=425, y=585)

# Progress Bar
progress_bar = ctk.CTkProgressBar(window, progress_color="#e44aff", width=400)
progress_bar.place(x=75, y=600)

# Volume Slider
volume_slider = ctk.CTkSlider(window, from_=0, to=1, command=set_volume, width=300)
volume_slider.place(x=135, y=650)

# Start with first song loaded
play_song()

window.mainloop()
