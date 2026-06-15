import os
import re
import glob

base_dir = "/Users/gsf/.gemini/antigravity/scratch/projects/GSF-Grace"

mission_posts = {
    "coming-to-tokyo": {"date": "2024-07-30", "order": 1},
    "learning-to-wait": {"date": "2024-07-30", "order": 2},
    "growing-familiar": {"date": "2024-10-19", "order": 3},
    "the-last-gift": {"date": "2025-03-31", "order": 4},
    "closer-than-we-think": {"date": "2025-12-12", "order": 5},
    "beginning-again-in-nihonbashi": {"date": "2026-03-31", "order": 6},
}

ko_footer = """---

※ 이 글은 당시 작성된 선교편지를 바탕으로,
GSFGrace 편집 원칙에 따라 에세이 형식으로 재구성한 글입니다.
"""

ja_footer = """---

※ 本記事は当時執筆された宣教レターをもとに、
GSFGrace編集方針に沿ってエッセイ形式へ再構成したものです。
"""

def update_frontmatter(content, date, order):
    parts = content.split('---')
    if len(parts) >= 3:
        fm = parts[1]
        body = '---'.join(parts[2:])
        
        new_fields = f"date: {date}\\nupdated: 2026-06-15\\ncategory: walk\\nseries: Good Samaritan Mission\\norder: {order}"
        if "date: " in fm and "updated: " in fm:
            return content
        
        fm = re.sub(r'^category:.*$', '', fm, flags=re.MULTILINE)
        fm = re.sub(r'^series:.*$', '', fm, flags=re.MULTILINE)
        fm = re.sub(r'^order:.*$', '', fm, flags=re.MULTILINE)
        fm = re.sub(r'\n{2,}', '\n', fm)
        
        if "pubDate: " in fm:
            fm = re.sub(r'pubDate:\s*\S+', new_fields, fm)
        elif "pubDate:" in fm:
            fm = re.sub(r'pubDate:.*', new_fields, fm)
        
        return "---" + fm + "---" + body
    return content

for slug, data in mission_posts.items():
    date = data["date"]
    order = data["order"]
    
    ko_path = os.path.join(base_dir, f"src/content/walk/ko/{slug}.md")
    if os.path.exists(ko_path):
        with open(ko_path, 'r') as f: content = f.read()
        content = update_frontmatter(content, date, order)
        if ko_footer.strip() not in content:
            content += "\n" + ko_footer
        with open(ko_path, 'w') as f: f.write(content)
        
    ja_path = os.path.join(base_dir, f"src/content/walk/ja/{slug}.md")
    if os.path.exists(ja_path):
        with open(ja_path, 'r') as f: content = f.read()
        content = update_frontmatter(content, date, order)
        if ja_footer.strip() not in content:
            content += "\n" + ja_footer
        with open(ja_path, 'w') as f: f.write(content)

    ko_app_path = os.path.join(base_dir, f"content-pipeline/_approved/walk_{slug}_ko.md")
    if os.path.exists(ko_app_path):
        with open(ko_app_path, 'r') as f: content = f.read()
        content = update_frontmatter(content, date, order)
        if ko_footer.strip() not in content:
            content += "\n" + ko_footer
        with open(ko_app_path, 'w') as f: f.write(content)

    ja_app_path = os.path.join(base_dir, f"content-pipeline/_approved/walk_{slug}_ja.md")
    if os.path.exists(ja_app_path):
        with open(ja_app_path, 'r') as f: content = f.read()
        content = update_frontmatter(content, date, order)
        if ja_footer.strip() not in content:
            content += "\n" + ja_footer
        with open(ja_app_path, 'w') as f: f.write(content)

def rename_pubdate(content):
    parts = content.split('---')
    if len(parts) >= 3:
        fm = parts[1]
        body = '---'.join(parts[2:])
        if "pubDate:" in fm and "date:" not in fm:
            fm = fm.replace("pubDate:", "date:")
        return "---" + fm + "---" + body
    return content

# update any remaining pubDate in walk folder to date
for root, _, files in os.walk(os.path.join(base_dir, "src/content/walk")):
    for file in files:
        if file.endswith(".md"):
            p = os.path.join(root, file)
            with open(p, 'r') as f: content = f.read()
            content = rename_pubdate(content)
            with open(p, 'w') as f: f.write(content)

# update any remaining pubDate in approved walk files
approved_walk = glob.glob(os.path.join(base_dir, "content-pipeline/_approved/walk_*.md"))
for p in approved_walk:
    with open(p, 'r') as f: content = f.read()
    content = rename_pubdate(content)
    with open(p, 'w') as f: f.write(content)

# update config
config_path = os.path.join(base_dir, "src/content.config.ts")
with open(config_path, 'r') as f: config = f.read()
if "date: z.coerce.date()" not in config:
    config = config.replace("pubDate: z.coerce.date(),\n    location", "date: z.coerce.date(),\n    updated: z.coerce.date().optional(),\n    category: z.string().optional(),\n    series: z.string().optional(),\n    order: z.number().optional(),\n    location")
    with open(config_path, 'w') as f: f.write(config)

# update components
components = [
    "src/pages/walk/index.astro",
    "src/pages/ko/walk/index.astro",
    "src/pages/walk/[slug].astro",
    "src/pages/ko/walk/[slug].astro",
]

for comp in components:
    p = os.path.join(base_dir, comp)
    if os.path.exists(p):
        with open(p, 'r') as f: content = f.read()
        if "post.data.pubDate" in content:
            content = content.replace("post.data.pubDate", "post.data.date")
            with open(p, 'w') as f: f.write(content)

print("Update complete")
