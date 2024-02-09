import requests
from bs4 import BeautifulSoup
import re
import json

def download_reel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Attempt to find the script tag containing the video information
        scripts = soup.find_all('script')
        for script in scripts:
            if 'shortcode_media' in script.text:
                json_data = re.search(r'window\._sharedData = (.*);</script>', script.string)
                if json_data:
                    json_data = json.loads(json_data.group(1))
                    # Navigate through the JSON structure to find the video URL
                    video_url = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['video_url']
                    # Download the video
                    video_response = requests.get(video_url)
                    if video_response.status_code == 200:
                        filename = url.split('/')[-1] + '.mp4'
                        with open(filename, 'wb') as f:
                            f.write(video_response.content)
                        print(f'Download complete: {filename}')
                    return
    print('Failed to download video.')

# Example usage
url = 'https://www.instagram.com/reel/C2eLdgQImLD/?igsh=YnE3OTl6encxeXo4'
download_reel(url)
