import os
import wave # to export the sound file
import tkinter as tk
import time
import threading
import pyaudio


class VovieRecorder:
    
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.content = tk.Label(text="@recording made by santosh")
        self.content.pack()
        self.buttom = tk.Button(text="⏺", font=("Arial", 120, "bold"), command=self.click_handler)
        self.buttom.pack()
        self.label = tk.Label(text="00:00:00")
        self.label.pack()
        self.recording = False
        self.root.mainloop()
        
    def click_handler(self):
        if self.recording :
            self.recording = False
            self.buttom.config(fg = "black")
        else:
            self.recording = True
            self.buttom.config(fg = "red")
            self.content.config(text="Starting recording", fg="green")
            threading.Thread(target=self.record).start()
    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        start = time.time()
        while self.recording:
            data = stream.read(1024)
            frames.append(data)
            
            passed = time.time() - start
            secs = passed % 60
            mins = passed // 60
            hours = mins // 60
            self.label.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")
            
        stream.stop_stream()
        stream.close()
        self.content.config(text="Recording finished", fg="black")
        audio.terminate()
        
        exists = True
        i = 1
        while exists:
            if os.path.exists(f"recording{i}.wav"):
                i += 1     
            else:
                exists = False
            
        sound_file = wave.open(f"recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()
        
VovieRecorder()