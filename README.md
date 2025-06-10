# Bulk Extract Instagram Metadata

## Background

Sometimes there are Instagram posts that I found interesting and want to download them, but I do not like the online tools I found as a lot of them have ads on the site or feels malicious, so I searched around and came across [Instaloader](https://instaloader.github.io/). As I am learning coding as well, so I use this opportunity to create some simple scripts to help me simplify my workflow.

I created `bulk_extract_ig_metadata.py` first as it seems easier to create, but my actual workflow is I might be scrolling Instagram at different time throughout the day, so I would save the interesting posts first, then try to download them while on my laptop, but Instagram Saved Post is somehow quite buggy on web browser and often doesn't load for me, so I created `extract_saved_ig_posts.py` to extract the metadata into a CSV while downloading the saved posts' photos / videos too.

# The Output

There are 2 simple scripts in this repo:
- `bulk_extract_ig_metadata.py` allows user to specify a txt file that contains a list of Instagram URLs and extracted the `username` and the creation date of each post into a CSV file.
- `extract_saved_ig_posts.py` allows user to extract all their Saved posts' metadata (URL, username, local creation date, caption) in their Instagram account and saved it into a CSV file.
    - If you wish to download the saved posts, just uncomment the relevant line in the script.