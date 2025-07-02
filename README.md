# Bulk Extract Instagram Metadata

A collection of Python scripts for extracting Instagram post metadata using the Instaloader library. This project is for educational purposes and personal workflow automation.

## Features

### Scripts Available:
- **`bulk_extract_ig_metadata.py`** - Extract metadata from a list of Instagram URLs
- **`extract_saved_ig_posts.py`** - Export all saved posts metadata with optional browser opening
- **`count_saved_posts.py`** - Count total saved posts in your account

### Output Format:
All scripts generate CSV files with UTF-8 encoding containing:
- Post URLs, usernames, creation dates
- Captions and accessibility descriptions (where available)
- Progress tracking during execution

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Extract from URL List
```bash
python bulk_extract_ig_metadata.py
```
- Prompts for Instagram username and URL file path
- Reads URLs from text file (one per line)
- Outputs to CSV with same filename

### Extract Saved Posts
```bash
python extract_saved_ig_posts.py
```
- Logs into your Instagram account
- Extracts all saved posts metadata
- Optional: Opens posts in browser for review
- Optional: Download media files (uncomment line 47)

### Count Saved Posts
```bash
python count_saved_posts.py
```
- Quick count of total saved posts

## Security Notes

⚠️ **Important Security Considerations:**
- Session files are stored locally - keep them secure
- Don't share session files or commit them to version control
- Use strong Instagram passwords and enable 2FA
- Be aware of Instagram's rate limits and terms of service
- Scripts store authentication tokens in plaintext files

## Background

This project was created to solve the problem of Instagram's web interface being unreliable for accessing saved posts. Instead of using potentially malicious online tools, these scripts provide a local solution using the trusted Instaloader library.

## Disclaimer

This tool is for personal use only. Respect Instagram's terms of service and rate limits. The authors are not responsible for any account restrictions or violations that may result from usage.