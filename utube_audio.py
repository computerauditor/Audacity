from pytube import YouTube

def audio_downloader():

        usr_inp = input('Enter URL here:- ')
        yt = YouTube(
                str(usr_inp),
            )

        print(f'\n[+]Title => {yt.title}\n')
        print(f'[+]THUMBNAIL =>  {yt.thumbnail_url}\n')
        
        #aud = list(enumerate(yt.streams.filter(only_audio=True)))
        print('[+]Processing...\n')

        print(f'[+]Downoading audio => {yt.title}\n')

        try:
                print('[+]downloading audio at *ITAG-140...*\n')
                downloader = yt.streams.get_by_itag(140)
                downloader.download()
        except:
                try:
                        print('\n[+] Audio ITAG-140 not available hence trying ITAG-139... \n')
                        print('[+] Or the user pressed "CTRL+C"... \n')
                        print('[+]downloading audio at *ITAG-139*\n')
                        downloader = yt.streams.get_by_itag(139)
                        downloader.download()
                except:
                        print('\n[+] Audio ITAG-139 not available hence trying ITAG-251... \n')
                        print('[+] Or the user pressed "CTRL+C"... \n')
                        print('[+]downloading audio at *ITAG-251*\n')
                        downloader = yt.streams.get_by_itag(251)
                        downloader.download()

        print(f'[+]Successfully downloaded audio {yt.title}\n')

#to call function
#audio_downloader()