import instaloader
import re
import csv

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

# Count saved posts
total_posts = sum(1 for x in profile.get_saved_posts())
print(f"Total saved posts: {total_posts}")