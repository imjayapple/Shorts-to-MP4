import csv
import os
import pytube
from pytube import YouTube
import re

def convert_shorts_url(url):
    """Convert YouTube Shorts URL to regular YouTube URL"""
    print(f"Original URL: {url}")
    
    # Extract video ID using regex
    video_id = None
    patterns = [
        r'youtube.com/shorts/([a-zA-Z0-9_-]+)',
        r'youtu.be/([a-zA-Z0-9_-]+)',
        r'youtube.com/watch\?v=([a-zA-Z0-9_-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            break
    
    if video_id:
        converted_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"Converted URL: {converted_url}")
        return converted_url
    else:
        print("Could not extract video ID")
        return url

def test_url_connection(url):
    """Test if we can connect to a single URL with detailed error handling"""
    try:
        print(f"\nTesting connection to: {url}")
        
        # Convert URL if it's a Shorts URL
        converted_url = convert_shorts_url(url)
        
        # Create YouTube object with more detailed error handling
        try:
            yt = YouTube(converted_url)
            print("✓ Successfully created YouTube object")
        except Exception as e:
            print(f"✗ Error creating YouTube object: {str(e)}")
            return False

        # Try to access various properties with individual try-except blocks
        try:
            print(f"Title: {yt.title}")
        except Exception as e:
            print(f"✗ Error accessing title: {str(e)}")
        
        try:
            print(f"Available streams: {len(yt.streams.all())}")
        except Exception as e:
            print(f"✗ Error accessing streams: {str(e)}")
        
        try:
            stream = yt.streams.get_highest_resolution()
            print(f"✓ Successfully got highest resolution stream: {stream.resolution}")
        except Exception as e:
            print(f"✗ Error getting highest resolution stream: {str(e)}")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        return False

def run_diagnostics():
    """Run a series of tests to diagnose issues"""
    print("=== Starting Diagnostics ===")
    print(f"Pytube version: {pytube.__version__}")
    
    # Test with your specific URL
    url = "https://www.youtube.com/shorts/WxNKCVVIWeY"
    success = test_url_connection(url)
    
    if not success:
        print("\nTroubleshooting steps:")
        print("1. Verify the video is still available by opening it in a browser")
        print("2. Try clearing your Python package cache:")
        print("   pip cache purge")
        print("   pip install --no-cache-dir --upgrade pytube")
        print("3. If issues persist, we might need to try an alternative library")

if __name__ == "__main__":
    run_diagnostics()