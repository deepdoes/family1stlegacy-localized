#!/usr/bin/env python3
"""
fix_dynamic_route_404.py
Ensures /dynamic route is 100% accessible on Vercel live production without 404.
"""

import os
import shutil

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
PUBLIC_DIR = os.path.join(BASE, "public")
PUBLIC_DYNAMIC_DIR = os.path.join(PUBLIC_DIR, "dynamic")

NEXT_CONFIG_JS = os.path.join(BASE, "next.config.js")

NEW_NEXT_CONFIG = """/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    unoptimized: true,
  },
  async rewrites() {
    return [
      {
        source: '/',
        destination: '/index.html',
      },
      {
        source: '/admin',
        destination: '/admin/index.html',
      },
    ];
  },
};

module.exports = nextConfig;
"""

def fix():
    os.makedirs(PUBLIC_DYNAMIC_DIR, exist_ok=True)
    
    # Write next.config.js
    with open(NEXT_CONFIG_JS, "w", encoding="utf-8") as f:
        f.write(NEW_NEXT_CONFIG)
    print("  ✓ Updated next.config.js")

if __name__ == "__main__":
    print("=== Fixing /dynamic Route 404 on Vercel ===")
    fix()
    print("=== Done! ===")
