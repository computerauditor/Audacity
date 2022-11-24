from pytube import Playlist


def youtube_playlist_downloader():

        usr_inp = input('Enter Playlists URL here:- ')
        yt = Playlist(
                str(usr_inp),
            )

        print(f'\n[+]Title => {yt.title}\n')

        print(f'Downloading Playlist =>  {yt.title}')

        x = 0

        for video in yt.videos:
                x += 1
                print('Video No.' + str(x) + f' of {yt.title} Downloaded')
                video.streams.get_highest_resolution().download()

        print(f'Successfully Downloaded Playlist => {yt.title}')

#To run the function
#youtube_playlist_downloader()