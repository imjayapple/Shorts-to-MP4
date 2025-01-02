import csv
import os
import yt_dlp  
# yt_dlp = We'll use this instead of pytube

def create_csv_if_not_exists():
    """Create videos.csv if it doesn't exist and add headers"""
    if not os.path.exists('videos.csv'):
        with open('videos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['url', 'title', 'status'])
            writer.writerow([
                'https://www.youtube.com/shorts/WxNKCVVIWeY',
                'Exercise - Back - Lats and Lat Prayers',
                'pending'
            ])

def download_videos():
    """Download videos from CSV and update their status"""
    with open('videos.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best',  # Get best quality
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Output template
        'quiet': False,  # Show progress
        'no_warnings': False,
        'ignoreerrors': True  # Continue on error
    }
    
    for row in rows:
        if row['status'] != 'completed':
            try:
                print(f"\nAttempting to download: {row['title']}")
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([row['url']])
                
                row['status'] = 'completed'
                print(f"Successfully downloaded: {row['title']}")
                
            except Exception as e:
                row['status'] = 'failed'
                print(f"Error downloading {row['title']}: {str(e)}")
    
    # Write updated statuses back to CSV
    with open('videos.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['url', 'title', 'status'])
        writer.writeheader()
        writer.writerows(rows)

def main():
    """Main function to run the program"""
    print("YouTube Shorts Downloader Starting...")
    create_csv_if_not_exists()
    download_videos()
    print("\nDownload process completed!")

if __name__ == "__main__":
    main()