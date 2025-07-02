import instaloader
import re
import csv
import time

# Initialize Instaloader & Login
L = instaloader.Instaloader(save_metadata=False, download_comments=False, post_metadata_txt_pattern="")
username = input("Enter your Instagram username: ")
try:
    L.load_session_from_file(username)
    print("Loaded session from file.")
except FileNotFoundError:
    L.interactive_login(username)
    L.save_session_to_file(username)
    print("Logged in and saved session for future reuse.")

# Load your profile
profile = instaloader.Profile.from_username(L.context, username)

# Count saved posts with rate limiting
print("Counting saved posts...")
total_posts = 0
for post in profile.get_saved_posts():
    total_posts += 1
    if total_posts % 10 == 0:  # Rate limiting every 10 posts
        time.sleep(1)
        print(f"Counted {total_posts} posts so far...", end='\r')
        
print(f"\nTotal saved posts: {total_posts}")