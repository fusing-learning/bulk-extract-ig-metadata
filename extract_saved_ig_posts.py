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

    saved_posts = profile.get_saved_posts()
    print("Processing saved posts...")
    
    urls_to_open = []
    processed_count = 0
    
    for post in saved_posts:
        processed_count += 1
        shortcode = post.shortcode
        post_url = f"https://www.instagram.com/p/{shortcode}/"
        writer.writerow([
            post.owner_username,
            post_url,
            post.date_local.strftime("%Y-%m-%d %H:%M:%S") if post.date_local else "N/A",
            post.caption,
            post.accessibility_caption if post.accessibility_caption else "N/A"
        ])

        urls_to_open.append(post_url)

        # [Optional] Download saved posts
        # L.download_post(post, target="saved_posts")

        print(f"Processed {processed_count} posts", end='\r')
        
        # Rate limiting - wait 1 second between requests
        time.sleep(1)
    
    print(f"\nTotal saved posts: {processed_count}")
    
    open_posts = input("Do you want to open all saved posts in your browser? (y/n): ").strip().lower()
    if open_posts == "y" and urls_to_open:
        print(f"Opening {len(urls_to_open)} posts in browser...")
        for url in urls_to_open:
            webbrowser.open(url)
    
print(f"\nSaved posts metadata written to {output_file}")