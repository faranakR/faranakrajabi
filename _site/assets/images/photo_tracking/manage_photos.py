#!/usr/bin/env python3
"""
Photo Gallery Management Script
Helps track and organize photos for website galleries
"""

import csv
import os
from datetime import datetime

class PhotoManager:
    def __init__(self):
        self.tracking_dir = "photo_tracking"
        self.master_log = f"{self.tracking_dir}/MASTER_PHOTO_LOG.csv"
        
    def add_photo(self, category, filename, **kwargs):
        """Add a new photo to the master log"""
        with open(self.master_log, 'a', newline='') as f:
            writer = csv.writer(f)
            row = [
                category,
                filename,
                kwargs.get('subject', ''),
                kwargs.get('date', datetime.now().strftime('%Y-%m-%d')),
                kwargs.get('location', ''),
                kwargs.get('people', ''),
                kwargs.get('description', ''),
                kwargs.get('tags', ''),
                kwargs.get('status', 'pending')
            ]
            writer.writerow(row)
        print(f"✅ Added {filename} to {category}")
    
    def list_photos(self, category=None):
        """List all photos, optionally filtered by category"""
        with open(self.master_log, 'r') as f:
            reader = csv.DictReader(f)
            photos = list(reader)
            
        if category:
            photos = [p for p in photos if p['category'] == category]
        
        print(f"\n📸 Photos ({len(photos)} total):")
        print("-" * 80)
        for p in photos:
            print(f"{p['category']:10} | {p['filename']:20} | {p['date']:12} | {p['primary_subject']}")
    
    def generate_captions(self, category):
        """Generate caption list for a category"""
        with open(self.master_log, 'r') as f:
            reader = csv.DictReader(f)
            photos = [p for p in reader if p['category'] == category]
        
        print(f"\n📝 Captions for {category}:")
        print("-" * 80)
        for p in photos:
            print(f"{p['filename']}: {p['description']}")

if __name__ == "__main__":
    manager = PhotoManager()
    
    print("🖼️  Photo Gallery Manager")
    print("=" * 80)
    
    # Show usage
    print("\nQuick commands:")
    print("  python manage_photos.py list              - List all photos")
    print("  python manage_photos.py list cooking      - List cooking photos")
    print("  python manage_photos.py captions hiking   - Show hiking captions")
    print("\nTo add a photo, edit the CSV files directly or use the add_photo() function")
    
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            category = sys.argv[2] if len(sys.argv) > 2 else None
            manager.list_photos(category)
        
        elif command == "captions":
            if len(sys.argv) > 2:
                manager.generate_captions(sys.argv[2])
            else:
                print("❌ Please specify category: cooking, hiking, or boxing")
    else:
        # Default: show summary
        manager.list_photos()
