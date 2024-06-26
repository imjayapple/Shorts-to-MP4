# Set the download path to './' to get the video in the current directory
# Use Relative Path to download to keep downloaded files out of the project
import pytube
from pytube import YouTube

url = ""

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

download_path = './'

stream.download(output_path=download_path)

print(f"Downloaded '{yt.title}' to {download_path}")