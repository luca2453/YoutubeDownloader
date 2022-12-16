#Criar opções para baixar em mp4 ou mp3

from pytube import YouTube

def Download(link):
    
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    
    try:
        youtubeObject.download()
    except:
        print("There has been an error! Please try again!")
    
    print("Download complete!")
    return

link = input("Put your YouTube link here: ")
Download(link)