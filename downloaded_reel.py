import requests

# The direct URL to the Instagram Reel video you found
# Step 1. Go to the Network Tab
# Step 2. Filter by 'media'
# Step 3. Under the "Headers" section grab the "Request URL:" (triple click)
# For now this works but I would like to craft a script that scrapes this specific URL automatically
video_url = ''










# Specify the name for the video file to be saved, right now the location is the current directory
download_path = 'downloaded_reel.mp4'

# Perform the request
response = requests.get(video_url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Open a file for writing the binary data of the video
    with open(download_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                file.write(chunk)
    print(f'Video downloaded successfully and saved as {download_path}')
else:
    print(f'Failed to download video. Status code: {response.status_code}')

# Script to scrape the network tab for the 'media' files, and obtain the Request URL
# Learning to use Selenium as the traditional way of webscraping static HTML is not sufficient