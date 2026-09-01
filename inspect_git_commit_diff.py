#!/usr/bin/env python3
"""
inspect_git_commit_diff.py
Inspects commit 67976d9 and earlier commits to see how the blog articles were originally structured.
"""

import subprocess

def get_diff(commit_hash, filepath):
    cmd = ["git", "show", f"{commit_hash}:{filepath}"]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd="/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy")
    return result.stdout

def count_words(text):
    clean = subprocess.run(["python3", "-c", f"import re; print(len(re.sub(r'<[^>]+>', ' ', '''{text}''').split()))"], capture_output=True, text=True).stdout.strip()
    return clean

def main():
    print("=== Inspecting Article Length History Across Git Commits ===")
    commits = ["1a5af23", "67976d9", "HEAD"]
    
    for c in commits:
        print(f"\n📌 Commit: {c}")
        try:
            content = get_diff(c, "blog_legacy.html")
            print(f"   blog_legacy.html total bytes: {len(content)}")
        except Exception as e:
            print(f"   Error reading commit {c}: {e}")

if __name__ == "__main__":
    main()
