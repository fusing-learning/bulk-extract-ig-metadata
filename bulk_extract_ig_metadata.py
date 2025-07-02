import instaloader
import re
import csv
import os
import time
from pathlib import Path

# Initialize Instaloader & Login
L = instaloader.Instaloader()
username = input("Enter your Instagram username: ")
L.interactive_login(username)

# Input and output files with validation
def validate_file_path(file_path):
    """Validate file path for security and existence"""
    try:
        path = Path(file_path).resolve()
        # Check if path exists and is a file
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")
        # Check file extension
        if path.suffix.lower() not in ['.txt', '.csv']:
            raise ValueError(f"Unsupported file type: {path.suffix}")
        return str(path)
    except Exception as e:
        raise ValueError(f"Invalid file path: {e}")

while True:
    try:
        input_file = input("Enter the path to your Instagram URLs file: ").strip()
        input_file = validate_file_path(input_file)
        break
    except ValueError as e:
        print(f"Error: {e}")
        continue

output_file = input_file.rsplit(".", 1)[0] + ".csv"

# Read URLs from file
with open(input_file, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

# Regex to extract shortcode
def extract_shortcode(url):
    match = re.search(r"instagram\.com/(p|reel)/([^/]+)/", url)
    return match.group(2) if match else None

# Open CSV for writing
with open(output_file, "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["URL", "Username", "Created_At"])

    # Loop through URLs
    for url in urls:
        shortcode = extract_shortcode(url)
        if not shortcode:
            print(f"Invalid URL: {url}")
            continue
        try:
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            writer.writerow([url, post.owner_username, post.date_utc])
            # Rate limiting - wait 1-2 seconds between requests
            time.sleep(1)
        except instaloader.exceptions.PostUnavailableException:
            print(f"Post unavailable or private: {url}")
        except instaloader.exceptions.LoginRequiredException:
            print(f"Login required to access: {url}")
        except Exception:
            print(f"Error processing {url} - skipping")