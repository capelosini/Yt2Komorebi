from pytube import YouTube
import requests
import os
import colorama

url=input("\nUrl: ")
name=input("Name: ")

defaultpath="/System/Resources/Komorebi/"+name.strip().lower().replace(" ", "_", 20)+"/"

os.mkdir(defaultpath)

configfilecontent=f"""[Info]
WallpaperType=video
VideoFileName={name+'.mp4'}

[DateTime]
Visible=true
Parallax=false
MarginTop=0
MarginRight=0
MarginLeft=0
MarginBottom=0
RotationX=0
RotationY=0
RotationZ=0
Position=center
Alignment=center
AlwaysOnTop=true
Color=#dd22dd22dd22
Alpha=255
ShadowColor=#dd22dd22dd22
ShadowAlpha=255
TimeFont=Lato Light 30
DateFont=Lato Light 20"""


yt=YouTube(url)

mp4files = yt.streams.filter(file_extension='mp4').order_by('resolution')
  
mp4files.last().download(filename=name+".mp4", output_path=defaultpath)
print(f"\n{colorama.Fore.YELLOW}Downloaded the Video")

r=requests.get(yt.thumbnail_url)
wallpaper=open(defaultpath+"wallpaper.jpg", "ab")
wallpaper.write(r.content)
wallpaper.close()
print("\nDownloaded the thumbnail")

configfile=open(defaultpath+"config", "w+")
configfile.write(configfilecontent)
configfile.close()
print("\nCreated the configuration file")
uninstallpath='/System/Resources/Komorebi/'+name.strip().lower().replace(" ", "_", 20)
print(f"\n{colorama.Fore.GREEN}Success!{colorama.Fore.WHITE}\n\n To uninstall the wallpaper type: 'sudo rm -rf {uninstallpath}'\n")

