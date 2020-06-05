# Shutterfly My Photos Downloader
#
# Purpose: It's a batch image downloader that you can auto download from Shutterfly 'My Photos'. You will be able to retreuve the original photos with 'date taken', so that for example when you upload them to your Google Photo, they can be aligned into the correct timing.
# Credit: This script is a similar dirty-and-quick approach inspired from kb3wmh https://github.com/kb3wmh/Shutterfly-Auto-Downloader

import urllib.request
import time
from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 

#How to: Step by Step
# 0. To have your album download, simply find the album for example from your sharesite album > add to shutterfly account, you will be able to save the full album or selected photos to your account.
# 1. photos.shutterfly.com, find the album page in a specific shutterfly 'My Photo' album, ex: https://photos.shutterfly.com/album/123456, modify the ALBUM_ID='123456'
# 2. Zoom in make the thumbnails smallest, scroll up and down, make sure all photos are loaded.abs
# 3. Use Chrome > Inspect , cursor to the first line <html> > ctrl c to copy the source
# 4. Paste it to a text editor and save the filename as 'original.txt'
# 5. Replace and create the output folder as in the code parameters, you will be able to download original photos into this folder then

# This is the folder to place the copy html file 'Original.html'
ALBUM_HTML_SOURCE_PATH = "/Users/nygg/pycode/shutterfly" 
# This is the folder that will collect the auto downloaded photos, make sure to create this folder first
ALBUM_SAVED_FOLDER = ALBUM_HTML_SOURCE_PATH + "/original/"
# This is exactly what you seen on the album url: ex:  https://photos.shutterfly.com/album/{ALBUM_ID}
ALBUM_ID='123456'
#set 3 second interval between each download to prevent blocking
DL_SleepTime=3

# ===== Two refresh parameters below=====

# Refresh 1: The URL with Token prefix (approximately every hour) 
# Where can I find? Enlarge any photo and click the built-in 'Download' button, You will find the full url including the token In the Chrome Inspector > 'Console' tab
# As said, once the token expired,you will get HTTP 400 error msg, then you simply replace with a new token.
url_template= "https://io.thislife.com/download?accessToken=eyJraWQiOiJpY1A4WExhT3B3cVlxQkdOXC9Bd1V1TFwvRU9BQVFHXC9Ic0hpSGZCMjFBbERFPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0MjhjYjU1MC04MjkyLTQyNmUtYTE4Yy1jNDI3MjdmZTMxYWUiLCJjb2duaXRvOmdyb3VwcyI6WyJDb2duaXRvTmV3U2lnbnVwIl0sImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX1RtSHpvUTY5aiIsImNvZ25pdG86dXNlcm5hbWUiOiI0MjhjYjU1MC04MjkyLTQyNmUtYTE4Yy1jNDI3MjdmZTMxYWUiLCJnaXZlbl9uYW1lIjoiQ2hpbGluIiwiYXVkIjoidDhvaWlmNTJtZWNlNmJsZWVhczJwb2YwbiIsImV2ZW50X2lkIjoiY2Y0NTI1MWUtYTUzZi00ZTQ3LWI3NTktMGJlZTBmZTVkNTgyIiwic2ZseV91aWQiOiIwMjMwNjk0MzkzNjgiLCJ0b2tlbl91c2UiOiJpZCIsInNjb3BlIjoicHJvZmlsZSB1c2VyIiwiYXV0aF90aW1lIjoxNTkwNjQ4ODc4LCJleHAiOjE1OTEyMjMyMTMsImlhdCI6MTU5MTIxOTYxMywiZmFtaWx5X25hbWUiOiJKYW4iLCJlbWFpbCI6ImphbWVzZGFzdGFyZEBnbWFpbC5jb20ifQ.LB2YN1NDx46ZtL8ERl6JIXELkiLhgRuPKdHllh1E-xn-1NpegNLxCUzqpJn23A3N_8bw3WDA28CyP4PPQ1DfZqIzzCjAjTVBKY4e3FCbNaU7YAuDfEVkSDdGWwRc623vEnj0ZQOKh-XtQpzFZ568tBSsgOSXuuf0vEUtqMYJONdqIjwZTX8eqTnjPcKpZ8CVNNNHUcmQhUcXmHhOjoYFd71w-EInmR2QVocxhuKhBUJfOhnr7NLsyQZ9ax94ZojNfK7dOsDbOS_EWlzxwvTIc4kdYk42AIguUyzpf3WB7_C1s-4IPW2qwJ7IFAb72xBOKgWlsAhxM2sz_Prqm5c4CQ&momentId="

# Refresh 2: Continue from the latest download. If you already downloaded photo 2385, put 2386.
continueID=0

def downloadImage(url, id):
    try:
        #filepath, _ =urllib.request.urlretrieve(url, ALBUM_HTML_SOURCE_PATH + "/original2/" + str(id) + ".jpg",_progress)
        filepath, _ =urllib.request.urlretrieve(url, ALBUM_SAVED_FOLDER + str(id) + ".jpg")
    except:
        print(filepath)
        return

if __name__ == "__main__":        
    thumbURLs = []
    photoURLs = []
    id = 0
    uids=[]

    #This assumes that the album HTML is saved with the name original.html
    album = open(ALBUM_HTML_SOURCE_PATH + "/original.html")
    albumAsString = album.read()    
    soup = BeautifulSoup(albumAsString,'html.parser')
    moments = soup.find_all("div", class_="moment scalable")   

    for moment in moments:
        uids.append(moment.get("data-uid"))
        
    for uid in uids:        
        #incase the download stop, jump to a new start number
        print('scanning...',id)
        #Keep changing this id every time you refresh the token url, so we can continue from the latest download
        if(id>=continueID):
            url= url_template + uid+ '&source=FMV&storyUid='+ALBUM_ID
            downloadImage(url, id)
            #to evade a possible IP ban
            time.sleep(DL_SleepTime)
        id += 1   