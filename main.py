import tkinter as tk
from PIL import Image, ImageTk
import sounddevice as sd
from scipy.io.wavfile import write, read
import numpy as np
import os   
import tempfile
import time

# Constants
IMAGE_PATH = "a.jpg"
SAMPLERATE = 44100  # Audio sample rate
DURATION = 5  # Recording duration in seconds

# Function to record audio
def record_audio():
    print("Recording started...")
    audio_data = sd.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=2, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        write(temp_audio_file.name, SAMPLERATE, audio_data)  # Save as WAV file
        temp_audio_path = temp_audio_file.name
    print(f"Recording saved temporarily as {temp_audio_path}")
    
    # Play the recorded audio
    print("Playing the recorded audio...")
    _, audio_data = read(temp_audio_path)
    sd.play(audio_data, SAMPLERATE)
    sd.wait()  # Wait until playback is finished
    
    # Wait for 5 seconds before deleting the file
    time.sleep(5)
    
    # Delete the temporary file
    os.remove(temp_audio_path)
    print(f"Temporary file {temp_audio_path} deleted")

# GUI Setup
root = tk.Tk()
root.title("Talking Tom")

# Load image
image = Image.open(IMAGE_PATH)
image = image.resize((300, 300))  # Resize image if needed
photo = ImageTk.PhotoImage(image)

# Create button with image
button = tk.Button(root, image=photo, command=record_audio, borderwidth=0)
button.pack()

# Run GUI loop
root.mainloop()