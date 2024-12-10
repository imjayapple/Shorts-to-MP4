# Import the entire pytube library for YouTube video processing
import pytube
# Import the YouTube class specifically from pytube for direct use
from pytube import YouTube

# Define the URL of the YouTube video to be downloaded
url = "https://www.youtube.com/shorts/WxNKCVVIWeY"

# Create a YouTube object using the URL, which will fetch the video's metadata
yt = YouTube(url)

# Get the highest resolution stream available for the video
stream = yt.streams.get_highest_resolution()

# Set the download path to the current directory ('./' means current directory)
download_path = './'

# Download the video to the specified path
stream.download(output_path=download_path)

# Print a confirmation message showing the video title and where it was saved
print(f"Downloaded '{yt.title}' to {download_path}")