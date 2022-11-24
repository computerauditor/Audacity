from utube_audio import audio_downloader
from utube_playlist import youtube_playlist_downloader
from utube_video import video_downloader

print('\n[+]What would you like to download?')
print('\n1)Video\n2)Audio/Music\n3)Playlist\n')
print('[+]Kindly type the serial number "eg: for video type: 1"\n')

user_input = input('[+]INPUT: ')

if user_input.strip().isdigit():
    print(f'\n[+]User input is {user_input}\n')
    if user_input == str(1):
    	print('[+]Okay! Running Video Downloader\n')
    	video_downloader()
    elif user_input == str(2):
    	print('[+]Okay! Running Audio Downloader\n')
    	audio_downloader()
    elif user_input == str(3):
    	print('[+]Okay! Running Playlist Downloader\n')
    	youtube_playlist_downloader()

else:
	print("[+]Kindly type a number from 1 to 3\n")
	