from pytube import YouTube

def video_downloader():

        usr_inp = input('Enter URL here:- ')
        yt = YouTube(
                str(usr_inp),
            )

        #prints title
        print(f'\n[+]Title => {yt.title}\n')
        #prints thumbnail
        print(f'[+]THUMBNAIL =>  {yt.thumbnail_url}\n')

        try:

                print('[+]Processing...')
                stream = yt.streams.get_highest_resolution()
                print(f'\n[+]Downloading video:- [{yt.title}] in highest possible quality\n')
                stream.download()
                print(f'[+]Successfully downloaded video {yt.title}\n')
        except:
                print(f'\n[+]Sorry! We could not download the video:-************ [{yt.title}] *************\n')
                print('[+]Try to re-run the script')

#To run the video_downloader function
#video_downloader()
