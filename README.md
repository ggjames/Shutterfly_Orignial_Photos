# Shutterfly_Orignial_Photos

Purpose: It's a batch image downloader that you can auto download from Shutterfly 'My Photos'. If you have Shutterfly Sharesite photo albums you can add You will be able to retreuve the original photos with 'date taken', so that for example when you upload them to your Google Photo, they can be aligned into the correct timing.

Credit: This script is a similar dirty-and-quick approach inspired from kb3wmh https://github.com/kb3wmh/Shutterfly-Auto-Downloader

Step by Step:

0. To have your album download, simply find the album for example from your sharesite album > add to shutterfly account, you will be able to save the full album or selected photos to your account.
1. Login "photos.shutterfly.com", find the album page in a specific shutterfly 'My Photo' album, ex: https://photos.shutterfly.com/album/123456, modify the ALBUM_ID='123456'
2. Zoom in make the thumbnails smallest, scroll up and down, make sure all photos are loaded.abs
3. Use Chrome > Inspect , cursor to the first line <html> > ctrl c to copy the source
4. Paste it to a text editor and save the filename as 'original.txt'
5. Replace and create the output folder as in the code parameters, you will be able to download original photos into this folder then

