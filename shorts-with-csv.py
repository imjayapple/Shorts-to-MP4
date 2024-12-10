import csv
import os
import pytube
from pytube import YouTube

def create_csv_if_not_exists():
    """Create videos.csv if it doesn't exist and add headers"""
    if not os.path.exists('videos.csv'):
        with open('videos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['url', 'title', 'status'])  # Headers
            # Adding your example videos
            writer.writerow([
                'https://www.youtube.com/shorts/WxNKCVVIWeY',
                'Exercise - Back - Lats and Lat Prayers',
                'pending'
            ])
            writer.writerow([
                'https://www.youtube.com/shorts/ZwzjYFCnjbc',
                'Leg Training - Only Bodybuilders Actually Care',
                'pending'
            ])

def download_videos():
    """Download videos from CSV and update their status"""
    with open('videos.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)  # Convert to list so we can modify it
    
    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    # Process each video
    for row in rows:
        if row['status'] != 'completed':  # Only process pending videos
            try:
                print(f"\nAttempting to download: {row['title']}")
                
                # Create YouTube object
                yt = YouTube(row['url'])
                
                # Get highest resolution stream
                stream = yt.streams.get_highest_resolution()
                
                # Download to downloads folder
                stream.download(
                    output_path='downloads',
                    filename=f"{row['title']}.mp4"  # Use custom title
                )
                
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