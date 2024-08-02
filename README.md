# Live-Photo-Copy 
## About 
This tool is used to copy the photos captured in your android phone to your linux machine.

## Working 
On running the script it stores all the photo, video file names which are in DCMI/Camera.
Every 10 second it checks if any new photo/video are captured if it finds any, it will copy those photos/videos to the path which is described in destn_path variable. 

## Instalation 
**Create a folder photo_folder in Desktop**

**Clone the repo**
``` shell 
git clone https://github.com/naikSiddarth/live-photo-copy.git
```
**Move into the project folder**
```shell
cd live-photo-copy
```
**Download the [Wifi FTP Server](https://play.google.com/store/apps/details/WiFi_FTP_Server?id=com.medhaapps.wififtpserver&hl=en_ZA&source=sh/x/srp/wr/m1/2&kgs=4b1f60e3d2374855&pli=1) on your android**
**Set the server root address to DCIM/Camera**
**Start the server and make sure your phone and computer are connected to same network**
**Login into the FTP server from your Linux machine** 
**Run the main file**
```shell
python3 main.py
```
