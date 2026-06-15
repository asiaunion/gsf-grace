import os
import re

base_dir = "/Users/gsf/.gemini/antigravity/scratch/projects/GSF-Grace"

def remove_first_h1(content):
    parts = content.split('---')
    if len(parts) >= 3:
        fm = parts[1]
        body = '---'.join(parts[2:])
        # Remove empty lines at the start of body
        body = body.lstrip()
        # If the first line is an H1, remove it
        if body.startswith('# '):
            # Find the first newline
            newline_idx = body.find('\n')
            if newline_idx != -1:
                body = body[newline_idx+1:].lstrip()
            else:
                body = ''
        return "---" + fm + "---\n\n" + body
    return content

def fix_coming_to_tokyo_date(content):
    parts = content.split('---')
    if len(parts) >= 3:
        fm = parts[1]
        fm = re.sub(r'date: 2024-07-30', 'date: 2024-05-10', fm)
        return "---" + fm + "---" + '---'.join(parts[2:])
    return content

# 1. Update coming-to-tokyo date in both languages and approved backups
tokyo_files = [
    "src/content/walk/ko/coming-to-tokyo.md",
    "src/content/walk/ja/coming-to-tokyo.md",
    "content-pipeline/_approved/walk_coming-to-tokyo_ko.md",
    "content-pipeline/_approved/walk_coming-to-tokyo_ja.md"
]

for p in tokyo_files:
    full_path = os.path.join(base_dir, p)
    if os.path.exists(full_path):
        with open(full_path, 'r') as f: content = f.read()
        content = fix_coming_to_tokyo_date(content)
        with open(full_path, 'w') as f: f.write(content)

# 2. Remove first H1 from all mission posts in walk/ko and walk/ja and _approved
walk_dirs = [
    "src/content/walk/ko",
    "src/content/walk/ja",
]

for wd in walk_dirs:
    for root, _, files in os.walk(os.path.join(base_dir, wd)):
        for file in files:
            if file.endswith(".md"):
                p = os.path.join(root, file)
                with open(p, 'r') as f: content = f.read()
                content = remove_first_h1(content)
                with open(p, 'w') as f: f.write(content)

# update _approved directory as well for all walk posts
import glob
approved_walk = glob.glob(os.path.join(base_dir, "content-pipeline/_approved/walk_*.md"))
for p in approved_walk:
    with open(p, 'r') as f: content = f.read()
    content = remove_first_h1(content)
    with open(p, 'w') as f: f.write(content)

print("Update complete")
