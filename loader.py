import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random
import time
import pygame
import subprocess
import threading
import struct
import ctypes
import os
import psutil


# Initialize pygame
pygame.init()
pygame.mixer.init()



#Loadfiles
short_audio_path = "./assets/"  # Replace with your short audio file
lol_audio_path = "./assets/"  # Replace with e
image_filename = './assets/'
gif_path = "./assets/"
#stop







short_audio_sound = pygame.mixer.Sound(short_audio_path)
short_audio_sound.set_volume(1)
lol_audio_sound = pygame.mixer.Sound(lol_audio_path)
lol_audio_sound.set_volume(0.5)

# Create threads for playing audio
def play_short_audio():
    short_audio_sound.play()
    time.sleep(10)  # Play for 10 seconds
    short_audio_sound.stop()

def play_lol_audio():
    lol_audio_sound.play(-1)  # Play on repeat

short_audio_thread = threading.Thread(target=play_short_audio)
lol_audio_thread = threading.Thread(target=play_lol_audio)

# Start the audio threads
short_audio_thread.start()
short_audio_thread.join()
lol_audio_thread.start()

SPI_SETDESKWALLPAPER = 20

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64

def changeBG(path):
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)

# Get the absolute path of the image in the same directory as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, image_filename)

changeBG(image_path)
# Initialize the tkinter window
root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations
root.attributes('-transparentcolor', 'white')  # Make white background transparent


# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create a canvas to display the animated GIF
canvas = tk.Canvas(root, width=110, height=120, highlightthickness=0, bg='black')  # Set canvas background to black
canvas.pack()
# Load the GIF animation using PIL


rickroll_animation = Image.open(gif_path)
frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(rickroll_animation)]

# Create a label to display the GIF frames
gif_label = tk.Label(canvas, image=frames[0], background='black')  # Set label background to black
gif_label.pack()


# Set the movement interval
initial_movement_interval = 0.5  # in seconds
movement_interval = initial_movement_interval

SPI_SETDESKWALLPAPER = 20

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64

def changeBG(path):
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)

# Get the absolute path of the image in the same directory as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, image_filename)

changeBG(image_path)
def update_gif():
    global frame_index  # Declare frame_index as a global variable
    frame_index = (frame_index + 1) % len(frames)
    gif_label.config(image=frames[frame_index])
    root.after(30, update_gif)

def move_window():
    global movement_interval
    while True:
        window_x = random.randint(0, screen_width - 110)
        window_y = random.randint(0, screen_height - 120)
        
        # Generate random background color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        canvas_color = f'#{r:02x}{g:02x}{b:02x}'
        
        canvas.config(bg=canvas_color)
        root.geometry(f"+{window_x}+{window_y}")
        
        root.update()  # Update the window to apply the new background color
        time.sleep(movement_interval)
        
        # Increase speed every 10 seconds
        if time.time() % 10 == 0:
            movement_interval *= 1.5  # Increase





def bring_to_front():
    while True:
        root.lift()
        root.attributes('-topmost', 1)
        time.sleep(0.1)

# Start updating the GIF
frame_index = 0
update_gif()

# Create threads for moving the window and bringing it to front
move_thread = threading.Thread(target=move_window)

bring_to_front_thread = threading.Thread(target=bring_to_front)
# Start the threads
move_thread.start()

bring_to_front_thread.start()
def resize_gif(gif_path2, max_width, max_height):
    gif = Image.open(gif_path2)
    
    # Calculate new dimensions while preserving the aspect ratio
    original_width, original_height = gif.size
    aspect_ratio = original_width / original_height
    
    if aspect_ratio > 1:
        # Landscape orientation
        new_width = min(original_width, max_width)
        new_height = int(new_width / aspect_ratio)
    else:
        # Portrait or square orientation
        new_height = min(original_height, max_height)
        new_width = int(new_height * aspect_ratio)
    
    resized_gif = gif.resize((new_width, new_height), Image.LANCZOS)  # Use Image.LANCZOS for resizing
    return ImageTk.PhotoImage(resized_gif)
def spawn_duplicate_with_delay(gif_path2, delay, new_width, new_height):
    time.sleep(delay)
    resized_gif = resize_gif(gif_path2, new_width, new_height)
    spawn_duplicate_window(resized_gif)
    

def spawn_duplicate_window(duplicate_gif):
    duplicate_window = tk.Toplevel(root)
    duplicate_window.overrideredirect(True)
    duplicate_window.attributes('-transparentcolor', 'white')
    
    duplicate_canvas = tk.Canvas(duplicate_window, width=110, height=120, highlightthickness=0, bg='black')
    duplicate_canvas.pack()
   
    duplicate_gif_label = tk.Label(duplicate_canvas, image=duplicate_gif, background='black')
    duplicate_gif_label.pack()
    
    duplicate_movement_interval = initial_movement_interval

    def update_duplicate_gif():
        nonlocal frame_index
        frame_index = (frame_index + 1) % len(frames)  # Use the frames list
        duplicate_gif_label.config(image=frames[frame_index])  # Use frames here
        duplicate_window.after(30, update_duplicate_gif)
    
    def move_duplicate_window(interval):
        while True:
            window_x = random.randint(0, screen_width - 110)
            window_y = random.randint(0, screen_height - 120)
        
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            canvas_color = f'#{r:02x}{g:02x}{b:02x}'
        
            duplicate_canvas.config(bg=canvas_color)
            duplicate_window.geometry(f"+{window_x}+{window_y}")
        
            duplicate_window.update()
            time.sleep(interval)
        
            if int(time.time()) % 10 == 0:
                interval *= 1.5
    
    frame_index = 0
    update_duplicate_gif()
    def bring_to_front():
        while True:
            duplicate_window.lift()
            duplicate_window.attributes('-topmost', 1)
            time.sleep(0.1)
    bring_to_front_thread = threading.Thread(target=bring_to_front)
    bring_to_front_thread.start()

# Start updating the GIF
    
    duplicate_move_thread = threading.Thread(target=move_duplicate_window, args=(duplicate_movement_interval,))
    duplicate_move_thread.start()


def spawn_duplicate_threads():
    while True:
        for _ in range(2):
            duplicate_thread = threading.Thread(target=spawn_duplicate_with_delay, args=(gif_path, 5, 50, 60))
            duplicate_thread.start()
        time.sleep(10)  # Wait for 10 seconds before starting the next iteration

# Call the function to start the loop
spawn = threading.Thread(target=spawn_duplicate_threads)

terminate_threads = []  # List to keep track of termination threads

# Create a thread for termination and duplicate threads
terminate_and_duplicate_thread = threading.Thread(target=lambda: [thread.start() for thread in terminate_threads] + [spawn.start()])

# Start the termination and duplicate thread
terminate_and_duplicate_thread.start()

#hhh
#hxh


root.mainloop()
