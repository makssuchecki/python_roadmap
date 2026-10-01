import time

def download_file(url, filename):
    """Simulate downloading a file"""
    print(f"Starting downloading a file")
    time.sleep(2)
    print("Completed: {filename}")
    return filename

def main():
    """Download files one by one (sequential)"""
    files = [
        ("https://example.com/video.mp4", "video.mp4"),
        ("https://example.com/document.pdf", "document.pdf"),
        ("https://example.com/music.mp3", "music.mp3")
    ]

    print("=== Sequential Downloads ===")
    start_time = time.time()

    for url, filename in files:
        download_file(url, filename)

    total_time = time.time() - start_time
    print(f"Total time: {total_time:.1f} seconds")

if __name__ == "__main__":
    main()