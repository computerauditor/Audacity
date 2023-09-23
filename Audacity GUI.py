import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from pytube import YouTube, Playlist
import datetime
import re
import tkinter.ttk as ttk

def sanitize_filename(filename):
    # Replace characters that are not allowed in Windows file paths
    invalid_chars = r'[\/:*?"<>|]'
    return re.sub(invalid_chars, '_', filename)

def run_audacity():
    def download_video():
        url = entry.get()
        save_path = filedialog.askdirectory()
        
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            title = yt.title.replace(" ", "_") 
            title = sanitize_filename(title)     # new code to santize title
            print(title)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{title}_{timestamp}.mp4" # new code to rename filename
            print(filename)
            stream.download(output_path=save_path, filename=filename)
            messagebox.showinfo("Download Complete", f"Video '{yt.title}' downloaded successfully.")
        except Exception as e:
            messagebox.showerror("Download Failed", f"Failed to download video. Error: {str(e)}")

    def download_audio():
        url = entry.get()
        save_path = filedialog.askdirectory()
        
        try:
            yt = YouTube(url)
            try:
                print('[+]downloading audio at *ITAG-140...*\n')
                title = yt.title.replace(" ", "_") 
                title = sanitize_filename(title)     # new code to santize title                
                downloader = yt.streams.get_by_itag(140)
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{title}_{timestamp}.mp3"
                downloader.download(output_path=save_path, filename=filename)
            except:
                try:
                    print('\n[+] Audio ITAG-140 not available hence trying ITAG-139... \n')
                    print('[+] Or the user pressed "CTRL+C"... \n')
                    print('[+]downloading audio at *ITAG-139*\n')
                    title = yt.title.replace(" ", "_") 
                    title = sanitize_filename(title)     # new code to santize title      
                    downloader = yt.streams.get_by_itag(139)
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{title}_{timestamp}.mp3"
                    downloader.download(output_path=save_path, filename=filename)
                except:
                    print('\n[+] Audio ITAG-139 not available hence trying ITAG-251... \n')
                    print('[+] Or the user pressed "CTRL+C"... \n')
                    print('[+]downloading audio at *ITAG-251*\n')
                    title = yt.title.replace(" ", "_") 
                    title = sanitize_filename(title)     # new code to santize title 
                    downloader = yt.streams.get_by_itag(251)
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{title}_{timestamp}.mp3"
                    downloader.download(output_path=save_path, filename=filename)
            messagebox.showinfo("Download Complete", f"Audio '{yt.title}' downloaded successfully.")
        except Exception as e:
            messagebox.showerror("Download Failed", f"Failed to download audio. Error: {str(e)}")

    def download_playlist():
        url = entry.get()
        save_path = filedialog.askdirectory()
        
        try:
            playlist = Playlist(url)
            print(f'\n[+]Title => {playlist.title}\n')
            print(f'Downloading Playlist => {playlist.title}')
            x = 1
            for video in playlist.videos:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{video.title}_{timestamp}.mp4"
                video.streams.get_highest_resolution().download(output_path=save_path, filename=filename)
                print(f'Video No. {x} of {playlist.title} Downloaded')
                x += 1
            messagebox.showinfo("Download Complete", f"Playlist '{playlist.title}' downloaded successfully.")
        except Exception as e:
            messagebox.showerror("Download Failed", f"Failed to download playlist. Error: {str(e)}")

    # Create the main window
    window = Tk()
    window.title("Audacity")
    window.geometry("400x250")  # Set the window size (width x height)


    # Apply the Forest theme
    window.tk.call('source', 'themes/forest-dark.tcl')  # Use 'forest-light.tcl' for the light theme
    ttk.Style().theme_use('forest-dark')  # Use 'forest-light' for the light theme

    # URL entry
    url_label = Label(window, text="Enter URL:")
    url_label.pack()

    entry = Entry(window)
    entry.pack()

    # Download buttons
    video_button = ttk.Button(window, text="Download Video", command=download_video, style='Accent.TButton')
    video_button.pack(padx=10, pady=10) 
    video_button.pack()

    audio_button = ttk.Button(window, text="Download Audio", command=download_audio, style='Accent.TButton')
    audio_button.pack(padx=10, pady=10) 
    audio_button.pack()

    playlist_button = ttk.Button(window, text="Download Playlist", command=download_playlist, style='Accent.TButton')
    playlist_button.pack(padx=10, pady=10)
    playlist_button.pack()

    # Status label
    status_label = Label(window, text="", fg="white", bg="black")
    status_label.pack()

    # Run the GUI
    window.mainloop()

# Call the function to run the YouTube downloader GUI
run_audacity()
