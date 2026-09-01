#!/usr/bin/env python3
"""
trace_article_history.py
Traces the git commit history and past versions of blog_*.html to explain to the user
exactly when and why the articles were formatted or shortened.
"""

import subprocess

def get_commit_history(filepath):
    cmd = ["git", "log", "--oneline", "-n", "10", "--", filepath]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd="/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy")
    return result.stdout.strip()

blog_files = [
    "blog_family_protection.html",
    "blog_retirement.html",
    "blog_education.html",
    "blog_living_benefits.html",
    "blog_financial_strategy.html",
    "blog_legacy.html"
]

def main():
    print("=== Git History for Blog Articles ===")
    for b in blog_files:
        print(f"\n📜 History for {b}:")
        history = get_commit_history(b)
        print(history if history else "  No commit history found.")

if __name__ == "__main__":
    main()
