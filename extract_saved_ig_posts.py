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

# Output file
output_file = f"{username}_saved_posts.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["post_url", "Username", "date_local", "caption", "accessibility_caption"])

    saved_posts = list(profile.get_saved_posts())
    total_posts = len(saved_posts)
    print(f"Total saved posts: {total_posts}")

    for idx, post in enumerate(saved_posts, start=1):
        shortcode = post.shortcode
        post_url = f"https://www.instagram.com/p/{shortcode}/"
        writer.writerow([
            post_url,
            post.owner_username,
            post.date_local.strftime("%Y-%m-%d %H:%M:%S") if post.date_local else "N/A",
            post.caption,
            post.accessibility_caption if post.accessibility_caption else "N/A"
        ])

        # [Optional] Download saved posts
        # L.download_post(post, target="saved_posts")

        print(f"Processed {idx}/{total_posts} posts", end='\r') # \r moves the cursor back to the start of the line, so the next print will overwrite the same line.
    
print(f"Saved posts metadata written to {output_file}")