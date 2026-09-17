#!/usr/bin/env python3
"""
create_old_spanish_backup.py
Creates a complete, isolated backup snapshot of all current Spanish HTML files in `old/` and `public/old/`
so the user and client can compare the pre-update version side-by-side at any time.
"""

import os
import shutil

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
OLD_DIR = os.path.join(BASE, "old")
PUBLIC_OLD_DIR = os.path.join(BASE, "public", "old")

os.makedirs(OLD_DIR, exist_ok=True)
os.makedirs(PUBLIC_OLD_DIR, exist_ok=True)

def backup():
    spanish_files = [f for f in os.listdir(BASE) if f.endswith("_es.html") and not f.startswith("v1") and not f.startswith("old")]
    
    for fname in sorted(spanish_files):
        src_path = os.path.join(BASE, fname)
        dst_old_path = os.path.join(OLD_DIR, fname)
        dst_public_old_path = os.path.join(PUBLIC_OLD_DIR, fname)

        # Copy exact current state
        shutil.copy2(src_path, dst_old_path)
        shutil.copy2(src_path, dst_public_old_path)
        print(f"  ✓ Saved snapshot of {fname} to /old/ and /public/old/")

def main():
    print("=== Creating Pre-Update Backup Snapshot in /old and /public/old ===")
    backup()
    print("=== Backup Complete! ===")

if __name__ == "__main__":
    main()
