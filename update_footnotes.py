import os
import re

# Define the new footnotes
WALK_STORY_KO_NEW = """※ 이 글은 과거의 기록을 바탕으로,
오늘의 걸음 속에서 다시 정리한 글입니다."""

WALK_STORY_JA_NEW = """※ 本記事は過去の記録をもとに、
今日の歩みの中であらためて綴り直したものです。"""

ARCHE_KO_NEW = """※ 이 글은 과거에 정리한 비전과 사역 원칙을 바탕으로,
현재의 방향성과 언어에 맞추어 다시 정리한 문서입니다."""

ARCHE_JA_NEW = """※ 本記事は過去にまとめたビジョンと宣教方針をもとに、
現在の方向性と言葉に合わせて再構成した文書です。"""

# Define the old footnotes to replace
WALK_STORY_KO_OLD = """※ 이 글은 당시 작성된 선교편지를 바탕으로,
GSFGrace 편집 원칙에 따라 에세이 형식으로 재구성한 글입니다."""
WALK_STORY_JA_OLD = """※ 本記事は当時執筆された宣教レターをもとに、
GSFGrace編集方針に沿ってエッセイ形式へ再構成したものです。"""

def update_file(filepath, category, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract pubDate or date
    match = re.search(r'^(?:pubDate|date):\s*([\d-]+)', content, re.MULTILINE)
    if not match:
        return
            
    date_str = match.group(1).strip()
    if date_str >= '2026-06-01':
        return

    # Process based on category and lang
    if category in ['walk', 'story']:
        new_footnote = WALK_STORY_KO_NEW if lang == 'ko' else WALK_STORY_JA_NEW
        old_footnote = WALK_STORY_KO_OLD if lang == 'ko' else WALK_STORY_JA_OLD
    elif category == 'arche':
        new_footnote = ARCHE_KO_NEW if lang == 'ko' else ARCHE_JA_NEW
        old_footnote = None
    else:
        return

    original_content = content

    if old_footnote and old_footnote in content:
        content = content.replace(old_footnote, new_footnote)
    else:
        # Check if the new footnote is already there
        if new_footnote not in content:
            # Append it. Make sure there's a blank line before it.
            content = content.rstrip() + "\n\n" + new_footnote + "\n"

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

# Process src directories
base_dir = '/Users/gsf/.gemini/antigravity/scratch/projects/GSF-Grace/src/content'
for category in ['walk', 'story', 'arche']:
    for lang in ['ko', 'ja']:
        dir_path = os.path.join(base_dir, category, lang)
        if os.path.exists(dir_path):
            for filename in os.listdir(dir_path):
                if filename.endswith('.md') or filename.endswith('.mdx'):
                    filepath = os.path.join(dir_path, filename)
                    update_file(filepath, category, lang)

# Process backup directory
backup_dir = '/Users/gsf/.gemini/antigravity/scratch/projects/GSF-Grace/content-pipeline/_approved'
if os.path.exists(backup_dir):
    for filename in os.listdir(backup_dir):
        if filename.endswith('.md'):
            # Filename format: category_slug_lang.md
            parts = filename.replace('.md', '').split('_')
            if len(parts) >= 3:
                category = parts[0]
                lang = parts[-1]
                if category in ['walk', 'story', 'arche'] and lang in ['ko', 'ja']:
                    filepath = os.path.join(backup_dir, filename)
                    update_file(filepath, category, lang)
