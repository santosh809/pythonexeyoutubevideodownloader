import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink, on_progress_callback=on_progress)  # Pass the on_progress() function as a callback
        video = ytobject.streams.get_highest_resolution()
        title.configure(text=ytobject.title)
        video.download()
        finishlable.configure(text="Downloaded", text_color="green")
    except:
        finishlable.configure(text="Invalid link or Download error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    byte_download = total_size - bytes_remaining
    cpercentage = byte_download / total_size * 100
    print(cpercentage)
# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Appp frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title(" Download the Youtube video")

# Adding UI Elememt
title = customtkinter.CTkLabel(app, text="Enter the link here")
title.pack(padx = 10, pady = 10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable= url_var)
link.pack()

#finish Downloading
finishlable = customtkinter.CTkLabel(app, text="")
finishlable.pack()

#Progressbar percentage
ppercentage = customtkinter.CTkLabel(app, text = "0%")
ppercentage.pack()
progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx = 10, pady = 10) 



# Download buttom
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady = 10)


# Run appp
app.mainloop()