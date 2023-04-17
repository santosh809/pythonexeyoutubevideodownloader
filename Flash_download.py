import tkinter as tk
from pytube import YouTube

def onclick_download():
    try:
        message.config(text="Download starting", fg="orange")
        selected_quality = quality_var.get()
        video_url = entrys.get()
        ytobject = YouTube(video_url)
        lable.config(text=ytobject.title)
        video = ytobject.streams.get_by_resolution(selected_quality)
        video.download()
        message.config(text="Successfully downloaded", fg="green")
        
    except:
        message.config(text="invald Link", fg="red")
    
    
    
    
root = tk.Tk()
root.title("This is Flash video Downloder")
lable = tk.Label(root, text="@Brother_YOutube_video_downloder", fg= "orange")
lable.pack()
# lable
lable = tk.Label(root, text="Enter the Link", font=("Helvetica", 20), fg= "black")
lable.pack()

# Enty part
entrys= tk.Entry(root, width=80)
entrys.pack(pady=20)

#Invalid_message
message = tk.Label(root, text="")
message.pack()

# Video Quality
quality_var = tk.StringVar()
quality_var.set("780p")
quality_list = ["144p", "240p", "360p", "780p", "1080p"]
quality = tk.OptionMenu(root, quality_var, *quality_list  )
quality.pack(pady=20)

# Download Buttom
download = tk.Button(root, text="Download", command=onclick_download)
download.pack()
root.mainloop()