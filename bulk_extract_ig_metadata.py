import instaloader
import re
import csv

# Initialize Instaloader & Login
L = instaloader.Instaloader()
username = input("Enter your Instagram username: ")
L.interactive_login(username)

# Input and output files
input_file = input("Enter the path to your Instagram URLs file: ")
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
        except Exception as e:
            print(f"Error processing {url}: {e}")