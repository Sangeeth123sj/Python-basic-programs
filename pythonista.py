
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}

print "Hello welcome to Tubeloader"
url = raw_input("Enter the URL of the video to download");
print "Your video is downloading   "

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])
