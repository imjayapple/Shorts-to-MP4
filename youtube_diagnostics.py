import csv
import os
import pytube
from pytube import YouTube
import sys

def test_url_connection(url):
    """Test if we can connect to a single URL"""
    try:
        print(f"\nTesting connection to: {url}")
        yt = YouTube(url)
        print("✓ Successfully created YouTube object")
        
        print("Attempting to fetch video details...")
        print(f"Title: {yt.title}")
        print(f"Available streams: {len(yt.streams.all())}")
        
        stream = yt.streams.get_highest_resolution()
        print(f"✓ Successfully got highest resolution stream: {stream.resolution}")
        
        return True
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        return False

def test_csv_reading():
    """Test if we can properly read the CSV file"""
    try:
        print("\nTesting CSV reading...")
        with open('videos.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            print(f"✓ Successfully read CSV file. Found {len(rows)} videos")
            return rows
    except Exception as e:
        print(f"✗ Error reading CSV: {str(e)}")
        return None

def run_diagnostics():
    """Run a series of tests to diagnose issues"""
    print("=== Starting Diagnostics ===")
    
    # Test 1: Check pytube version
    print(f"\nPytube version: {pytube.__version__}")
    
    # Test 2: Check CSV
    rows = test_csv_reading()
    if not rows:
        return
    
    # Test 3: Test first URL
    first_row = rows[0]
    success = test_url_connection(first_row['url'])
    
    if not success:
        print("\nPossible solutions:")
        print("1. Your pytube version might need updating. Try:")
        print("   pip install --upgrade pytube")
        print("2. YouTube might have updated their system. Check if there's a newer pytube version available.")
        print("3. The URL might be invalid or the video might be private/deleted.")

if __name__ == "__main__":
    run_diagnostics()