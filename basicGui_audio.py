from tkinter import *   #Imports all Tkinter GUI classes
import pygame  #For audio Playback
from tkinter import filedialog  #Import file dialog tool which let user select a file from system
import os 

BG_COLOR="#121212"    # Main dark background
CARD_COLOR = "#272626"    # Panels /Cards
ACCENT = "#2CFF05"    #Neon Green
TEXT_COLOR = "#FFFFFF"
MUTED_TEXT = "#B3B3B3"

pygame.mixer.init()    #initilize audio mixer

songs=[]

def add_songs():    #Function to add songs in list
    files = filedialog.askopenfilenames()    # Select multiple files to be added
    for file in files:  # File is address of selected file
        songs.append(file)    # Adding full address of each file in songs list
        playlist.insert(END, os.path.basename(file))    # Add file name(NOT address) into the listbox in application
def play_song():    #Function to load and play the song
    index = playlist.curselection()[0]    # curselection returns a tuple of selected indices [0] is used to select only first input 
    pygame.mixer.music.load(songs[index])    #Load the selected song into memory(Does not play it)
    pygame.mixer.music.play()   #Starts playing the loaded song (In background) Play song from start everytime
def pause_song():
    pygame.mixer.music.pause()
def resume_song():
    pygame.mixer.music.unpause()
def stop_song():
    # Pause the playing audio and resets it to 0 seconds
    pygame.mixer.music.stop()
def set_volume(val):
    volume = float(val)/100  # convert 0-100 -> 0.0-1.0
    pygame.mixer.music.set_volume(volume)

def button_style(parent, text, cmd):    # defining button style
    return Button(parent, text = text, command = cmd, bg = CARD_COLOR, fg = TEXT_COLOR, activebackground = ACCENT, activeforeground="black", relief = FLAT, font=("Segoe UI", 11), width=10, padx=5, pady=5)

root = Tk()    #Creates the main application window

root.configure(bg=BG_COLOR)
root.title("🎵 Music Player")    #Sets the window title
root.geometry("480x640")
# root.resizable(False, False)

top_frame = Frame(root, bg="#121212")
control_frame = Frame(root, bg="#121212")
volume_frame = Frame(control_frame, bg=BG_COLOR)
playlist_frame = Frame(root, bg = "#121212")

playlist = Listbox(playlist_frame, bg = CARD_COLOR, fg=TEXT_COLOR, selectbackground=ACCENT, font=("Segoe UI", 11), highlightthickness=0,borderwidth=0)
playlist.pack(fill = BOTH, expand=True, padx=20, pady=10)

top_frame.pack(fill = X)
playlist_frame.pack(fill=BOTH, expand =True)
control_frame.pack(pady = 10)

Label(top_frame, text = "Audio Player", bg=BG_COLOR, fg=ACCENT, font=("Seoge UI", 22, "bold")).pack(pady=20)


volume_slider = Scale(volume_frame, from_= 100, to = 0, orient = VERTICAL, bg=BG_COLOR, fg=TEXT_COLOR,troughcolor=CARD_COLOR, highlightthickness=0,showvalue=True, length = 120, command = set_volume)
volume_slider.set(70)
volume_slider.pack()
Label(volume_frame, text = "Volume", bg=BG_COLOR, fg=MUTED_TEXT, font=("Seoge UI", 10)).pack(pady=(5,0))

#Button(root(Parent window), text(text on button command), (function to run when clicked )).pack() ( places the button in window) 
button_style(control_frame, "Load", add_songs).grid(row=0, column=0, padx = 8)    #Function are written without parenthesis because tkinter calls the function only when called.  
button_style(control_frame, "Play", play_song).grid(row=-0, column=1, padx = 8)
button_style(control_frame, "Pause", pause_song).grid(row=0, column=2, padx = 8)
button_style(control_frame, "Resume", resume_song).grid(row=1, column=0, padx = 8)
button_style(control_frame, "Stop", stop_song).grid(row=1, column=1, padx = 10)

volume_frame.grid(row=0, column = 3, rowspan = 2, padx = 15)
#keeps window open 
# listens for button clicks mouse actions keyboard input
# Without this window will open and closes instantly
root.mainloop()