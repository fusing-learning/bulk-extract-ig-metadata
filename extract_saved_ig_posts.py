import instaloader
import re
import csv
import webbrowser
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

# Output file with validation
def validate_username(username):
    """Validate username for security"""
    if not username or not username.strip():
        raise ValueError("Username cannot be empty")
    # Remove potentially dangerous characters
    safe_username = re.sub(r'[^a-zA-Z0-9._-]', '', username.strip())
    if not safe_username:
        raise ValueError("Username contains only invalid characters")
    return safe_username

safe_username = validate_username(username)
output_file = f"{safe_username}_saved_posts.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Username","post_url", "date_local", "caption", "accessibility_caption"])

    saved_posts = list(profile.get_saved_posts())
    total_posts = len(saved_posts)
    print(f"Total saved posts: {total_posts}")

    open_posts = input("Do you want to open the saved posts in your browser? (y/n): ").strip().lower()

    for idx, post in enumerate(saved_posts, start=1):
        shortcode = post.shortcode
        post_url = f"https://www.instagram.com/p/{shortcode}/"
        writer.writerow([
            post.owner_username,
            post_url,
            post.date_local.strftime("%Y-%m-%d %H:%M:%S") if post.date_local else "N/A",
            post.caption,
            post.accessibility_caption if post.accessibility_caption else "N/A"
        ])

        if open_posts == "y":
            webbrowser.open(post_url)
            # Rate limiting when opening browser tabs
            time.sleep(2)

        # [Optional] Download saved posts
        # L.download_post(post, target="saved_posts")

        print(f"Processed {idx}/{total_posts} posts", end='\r') # \r moves the cursor back to the start of the line, so the next print will overwrite the same line.
        
        # Rate limiting - wait 1 second between requests
        time.sleep(1)
    
print(f"Saved posts metadata written to {output_file}")