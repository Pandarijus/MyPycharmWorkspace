from pytube import YouTube as yt
from datetime import date
# PASTE URLS IN THE BOTTOM

path = 'C:\\Users\\krott\\Videos\\pythonDownloads'
currDate = str(date.today().strftime("%d-%m-%Y"))



def downloadFromYoutube(url,video):
    try:
        myVid = yt(url)

        if video:
            # myVid.streams.filter(res="480p").first().download()
            i = 0

            # ------------- UNCOMMENT THIS IF YOUR VIDEO DOWNLOAD IS FUCKED -------------
            #for stream in myVid.streams:
              #  print("[",i,"]",stream)
             #   i+=1

            #index = input('select Video')
            # ------------- Till here -------------
            index = 2
            myVid = myVid.streams[index]
            print(myVid)
            print('---Download Started---')
            myVid.download(path+'\\Video\\'+currDate)
            print('------------------------Download END------------------------------')

        else:
            audios = myVid.streams.filter(only_audio=True).first().download(path+'\\Audio\\'+currDate)
            print('------------------------Download END------------------------------')
            # audios.first().download()
    except Exception as e:
        print(e)
        #print("[MY ERROR]This Link Is NOT Valid" +e.)
#

justOneLink = ( input('One Link -> 1  Links From File -> 2\n') == '1' )
wantToDownloadAVideo = ( input('Video -> 1  Audio -> 2\n') == '1' )

if justOneLink:
    if wantToDownloadAVideo:
        urlStart = input('Please Paste The URL Of The Video:')
    else:
        urlStart = input('Please Paste The URL Of The Audio:')

    downloadFromYoutube(urlStart,wantToDownloadAVideo)
else:
    with open("links.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    urls = lines
    count = 0
    length = len(urls)
    for u in urls:
        count = count+1
        print(f'---Download Started:  {count} from {length}  ---')
        downloadFromYoutube(u, wantToDownloadAVideo)

