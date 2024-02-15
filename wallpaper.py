from bs4 import *
import requests
import os
from subprocess import Popen

url = "https://www.natgeotv.com/ca/photo-of-the-day"
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")
images = soup.findAll('img', alt=True)

#couldnt find a better way to get specifically the newest photo of the day
#first two images are logos, third is newest
imgUrl = str(images[2])
newUrl = imgUrl[imgUrl.find("https"):imgUrl.find("D/")+2]
photoNum = imgUrl[imgUrl.find("D/")+2:imgUrl.find(".T")]
#for some reason, bs.find is finding the thumbnail version
#but the real photo can be found with some string manip
photoNum = str(int(photoNum)-1)
photoNum += ".jpg"
newUrl += photoNum
args = ['wget', '-P', '/home/liam/Pictures/Natgeo-Wallpapers', newUrl]
Popen(args).communicate()
command = "gsettings set org.gnome.desktop.background picture-uri-dark "
path = "'file:///home/liam/Pictures/Natgeo-Wallpapers/%s'" % photoNum
os.system(command+path)
# then we should set the background daily by having os run this script everyday