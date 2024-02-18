import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import shutil
import subprocess
from PIL import Image, ImageSequence

class BuilderApp:
    def __init__(self, master):
        assets_folder = "./Output/assets"
        shutil.rmtree(assets_folder, ignore_errors=True)
        os.makedirs(assets_folder)
        self.master = master
        self.master.title("Builder App")
        self.master.geometry("500x600")
        self.master.configure(bg="#333333")  # Set dark grey background

        # Asset paths
        self.music1_path = tk.StringVar()
        self.music2_path = tk.StringVar()
        self.icon_path = tk.StringVar()
        self.background_path = tk.StringVar()
        self.gif_path = tk.StringVar()
        self.terminate_processes_var = tk.BooleanVar(value=False)


        # Configure style for themed widgets
        style = ttk.Style()
        style.configure("TFrame", background="#333333")  # Dark grey background
        style.configure("TButton", background="gold", bordercolor="gold", foreground="#E1D9D1")  # Gold button with gold border
        style.map("TButton", background=[("active", "#555555")])  # Darker background on button press
        style.configure("TLabel", background="#333333", foreground="white")  # Dark grey label
        style.configure("TEntry", fieldbackground="#555555", foreground="white")  # Darker grey entry field

        # Entry fields for asset paths
        tk.Label(self.master, text="Music 1:", bg="#333333", fg="white").pack()
        self.music1_entry = tk.Entry(self.master, textvariable=self.music1_path, bg="#555555", fg="#E1D9D1")
        self.music1_entry.pack(pady=5)

        tk.Label(self.master, text="Music 2:", bg="#333333", fg="white").pack()
        self.music2_entry = tk.Entry(self.master, textvariable=self.music2_path, bg="#555555", fg="#E1D9D1")
        self.music2_entry.pack(pady=5)

        tk.Label(self.master, text="Icon:", bg="#333333", fg="white").pack()
        self.icon_entry = tk.Entry(self.master, textvariable=self.icon_path, bg="#555555", fg="#E1D9D1")
        self.icon_entry.pack(pady=5)

        tk.Label(self.master, text="Background Image:", bg="#333333", fg="white").pack()
        self.background_entry = tk.Entry(self.master, textvariable=self.background_path, bg="#555555", fg="#E1D9D1")
        self.background_entry.pack(pady=5)

        tk.Label(self.master, text="GIF:", bg="#333333", fg="white").pack()
        self.gif_entry = tk.Entry(self.master, textvariable=self.gif_path, bg="#555555", fg="#E1D9D1")
        self.gif_entry.pack(pady=5)
               
               
        tk.Checkbutton(self.master, text="Terminate taskmanager process", variable=self.terminate_processes_var).pack()


        # Buttons
        self.upload_music1_button = tk.Button(self.master, text="Upload Music 1", command=self.upload_music1, bg="gold", fg="black")
        self.upload_music1_button.pack(pady=5)

        self.upload_music2_button = tk.Button(self.master, text="Upload Music 2", command=self.upload_music2, bg="gold", fg="black")
        self.upload_music2_button.pack(pady=5)

        self.upload_icon_button = tk.Button(self.master, text="Upload Icon", command=self.upload_icon, bg="gold", fg="black")
        self.upload_icon_button.pack(pady=5)

        self.upload_background_button = tk.Button(self.master, text="Upload Background", command=self.upload_background, bg="gold", fg="black")
        self.upload_background_button.pack(pady=5)

        self.upload_gif_button = tk.Button(self.master, text="Upload GIF", command=self.upload_gif, bg="gold", fg="black")
        self.upload_gif_button.pack(pady=5)

        self.start_button = tk.Button(self.master, text="Build", command=self.start_program, bg="gold", fg="black")
        self.start_button.pack(pady=10)

    def upload_music1(self):
        file_path = filedialog.askopenfilename(title="Select Music 1 File", filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            # Move the file to the ./assets folder
            dest_path = os.path.join('./Output/assets', os.path.basename(file_path))
            shutil.copy(file_path, dest_path)
            dest_path = os.path.join('.', 'assets', os.path.basename(file_path))

            self.music1_path.set(dest_path)

    def upload_music2(self):
        file_path = filedialog.askopenfilename(title="Select Music 2 File", filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            # Move the file to the ./assets folder
            dest_path = os.path.join('./Output/assets', os.path.basename(file_path))
            shutil.copy(file_path, dest_path)
            dest_path = os.path.join('.', 'assets', os.path.basename(file_path))

            self.music2_path.set(dest_path)

    def upload_icon(self):
        file_path = filedialog.askopenfilename(title="Select Icon File", filetypes=[("Icon Files", "*.ico")])
        if file_path:
            # Move the file to the ./assets folder
            dest_path = os.path.join('./Output/assets', os.path.basename(file_path))
            shutil.copy(file_path, dest_path)
            

            self.icon_path.set(dest_path)
            

    def upload_background(self):
        file_path = filedialog.askopenfilename(title="Select Background Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            # Move the file to the ./assets folder
            dest_path = os.path.join('./Output/assets', os.path.basename(file_path))
            shutil.copy(file_path, dest_path)
            dest_path = os.path.join('.', 'assets', os.path.basename(file_path))

            self.background_path.set(dest_path)
            

    def upload_gif(self):
        file_path = filedialog.askopenfilename(title="Select GIF File", filetypes=[("GIF Files", "*.gif")])
        if file_path:
            # Move the file to the ./Output/assets folder
            dest_path = os.path.join('./Output/assets', os.path.basename(file_path))
            shutil.copy(file_path, dest_path)

            # Resize the GIF to 80x80 pixels
            resized_gif_path = os.path.join('./Output/assets', f"resized_{os.path.basename(file_path)}")
            self.resize_gif(dest_path, resized_gif_path, 80, 80)
            resized_gif_path = os.path.join('.', 'assets', os.path.basename(f"resized_{os.path.basename(file_path)}"))

            self.gif_path.set(resized_gif_path)

    def resize_gif(self, input_path, output_path, width, height):
        try:
            original = Image.open(input_path)
            frames = []

            for frame in ImageSequence.Iterator(original):
                resized_frame = frame.resize((width, height), Image.LANCZOS)
                frames.append(resized_frame)

            frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=original.info['duration'])

        except Exception as e:
            print(f"Error resizing GIF: {e}")
    
    
    def compile_loader(self):
        try:
            icon_path = self.icon_path.get()  # Retrieve the selected icon path
            output_folder = "./Output"  # Specify the output folder

            options = ["--onefile", "--noconsole", f"--distpath={output_folder}"]  # Add options for one-file, no console, and specify output folder
            if icon_path:
                options.extend(["--icon", icon_path])  # Add the icon option if provided

            subprocess.run(["pyinstaller"] + options + ["loader.py"])
            print("Compilation successful!")

        except Exception as e:
            print(f"Error during compilation: {e}")
    def start_program(self):
        # Retrieve the selected asset paths
        music1_path = self.music1_path.get()
        print(music1_path)
        music2_path = self.music2_path.get()
        print(music2_path)
        icon_path = self.icon_path.get()
        background_path = self.background_path.get()
        gif_path = self.gif_path.get()
        code = f"""#Loadfiles
short_audio_path = "./assets/{os.path.basename(music1_path)}"  # Replace with your short audio file
lol_audio_path = "./assets/{os.path.basename(music2_path)}"  # Replace with e
image_filename = './assets/{os.path.basename(background_path)}'
gif_path = "./assets/{os.path.basename(gif_path)}"
#stop"""


        termination_code = """#hhh
import psutil
import time
import threading

def terminate_process_by_name(process_name, duration):
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                pid = process.info['pid']
                
                p = psutil.Process(pid)
                p.terminate()
                print(f"Terminated process '{process_name}' with PID {pid}")
        
        # Adjust the sleep interval as needed
        time.sleep(1)  # Sleep for 1 second before checking again

def terminate_after_timeout(process_name, timeout):
    time.sleep(timeout)
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            pid = process.info['pid']
            try:
                p = psutil.Process(pid)
                p.terminate()
                print(f"Terminated process '{process_name}' with PID {pid}")
            except psutil.NoSuchProcess:
                print(f"Process '{process_name}' with PID {pid} not found")


# Create threads for each function
spawn2 = threading.Thread(target=terminate_process_by_name, args=('Taskmgr.exe',3000))
spawn2.start()


#hxh"""
            
        paw_path = "./loader.py"
        with open(paw_path, 'r') as paw_file:
            paw_contents = paw_file.read()

        # Find the markers for code replacement
        start_marker = "#Loadfiles"
        end_marker = "#stop"
        start_marker2 = "#hhh"
        end_marker2 = "#hxh"

        # Ensure the markers are present in the file
        if start_marker not in paw_contents or end_marker not in paw_contents or start_marker2 not in paw_contents or end_marker2 not in paw_contents:
            raise ValueError("Markers not found in the loader.py file")

        # Replace the code in loader.py
        new_paw_contents = paw_contents.replace(
            paw_contents[paw_contents.index(start_marker):paw_contents.index(end_marker, paw_contents.index(start_marker)) + len(end_marker)],
            code
        ).replace(
            paw_contents[paw_contents.index(start_marker2):paw_contents.index(end_marker2, paw_contents.index(start_marker2)) + len(end_marker2)],
            termination_code if self.terminate_processes_var.get() else """#hhh
#hxh"""
        )

        # Write the updated content back to loader.py
        with open(paw_path, 'w') as paw_file:
            paw_file.write(new_paw_contents)





        # Write the generated code into loader.py
        

        print("Starting program with custom assets...")
        print(f"Music 1: {music1_path}")
        print(f"Music 2: {music2_path}")
        print(f"Icon: {icon_path}")
        print(f"Background Image: {background_path}")
        print(f"GIF: {gif_path}")
        # Include logic to start the main program with the specified assets
        self.compile_loader()
        


if __name__ == "__main__":
    root = tk.Tk()
    app = BuilderApp(root)
    root.mainloop()