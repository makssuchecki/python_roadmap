import threading
import time
import random

class DownloadThread(threading.Thread):
    """Custom thread class for downloading files with built-in retry logic"""
    
    def __init__(self, url, filename, max_retries=3):
        super().__init__(name=f"Downloader-{filename.split('.')[0]}")
        self.url = url
        self.filename = filename
        self.max_retries = max_retries
        self.result = None
        self.download_time = None
        self.attempts = 0
    
    def run(self):
        """Called when thread.start() runs"""
        print(f"[{self.name}] Starting download: {self.filename}")
        start_time = time.time()
        
        for attempt in range(1, self.max_retries + 1):
            self.attempts = attempt
            try:
                print(f"[{self.name}] Attempt {attempt} for {self.filename}")
                time.sleep(2)  # Simulate download
                
                if attempt == 1 and random.random() < 0.2:  # 20% chance of failure
                    raise Exception("Network timeout")
                
                self.download_time = time.time() - start_time
                self.result = "success"
                print(f"[{self.name}] {self.filename} downloaded in {self.download_time:.1f}s")
                return
            except Exception as e:
                print(f"[{self.name}] Attempt {attempt} failed: {e}")
                if attempt < self.max_retries:
                    time.sleep(0.5)  # brief pause before retry
                else:
                    self.result = "failed"
                    self.download_time = time.time() - start_time
                    print(f"[{self.name}] Permanently failed after {attempt} attempts")

def demonstrate_custom_threads():
    files = [
        ("https://example.com/video.mp4", "video.mp4"),
        ("https://example.com/document.pdf", "document.pdf"),
        ("https://example.com/music.mp3", "music.mp3")
    ]
    
    print("=== Custom Thread Class Downloads ===")
    download_threads = [DownloadThread(url, filename) for url, filename in files]
    
    start_time = time.time()
    for t in download_threads: t.start()
    for t in download_threads: t.join()
    total_time = time.time() - start_time
    
    print("\n=== Download Results ===")
    successful = 0
    for t in download_threads:
        status = "Success" if t.result == "success" else "Failed"
        print(f"{status} - {t.filename}: {t.result} ({t.attempts} attempts, {t.download_time:.1f}s)")
        if t.result == "success": successful += 1
    
    print(f"Total time: {total_time:.1f} seconds")
    print(f"Success rate: {successful}/{len(download_threads)}")

if __name__ == "__main__":
    demonstrate_custom_threads()