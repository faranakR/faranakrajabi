# 📸 Photo Gallery Tracking System

This folder helps you organize and track all photos for your website galleries.

## Files

- `MASTER_PHOTO_LOG.csv` - Main tracking spreadsheet (use this!)
- `cooking_photos.csv` - Detailed cooking photo metadata
- `hiking_photos.csv` - Detailed hiking trip logs
- `boxing_photos.csv` - Detailed boxing session logs
- `manage_photos.py` - Python script to help manage photos

## Quick Start

### 1. Add a new photo to your website:

1. Copy photo to appropriate folder:
   - Cooking: `assets/images/cooking/`
   - Hiking: `assets/images/hiking/`
   - Boxing: `assets/images/boxing/`

2. Open `MASTER_PHOTO_LOG.csv` in Excel/Numbers/Google Sheets

3. Add a new row with:
   - category (cooking/hiking/boxing)
   - filename (e.g., food7.jpg)
   - primary_subject (what's in the photo)
   - date (when taken)
   - location (where taken)
   - people (who's in it)
   - description (caption for website)
   - tags (comma-separated keywords)
   - status (pending/uploaded/published)

### 2. Using the Python script:
```bash
# List all photos
python photo_tracking/manage_photos.py list

# List only cooking photos
python photo_tracking/manage_photos.py list cooking

# Show all captions for hiking
python photo_tracking/manage_photos.py captions hiking
```

### 3. Category-specific tracking:

For detailed metadata, use:
- `cooking_photos.csv` - Track recipes, occasions, ingredients
- `hiking_photos.csv` - Track trails, elevation, distance, companions
- `boxing_photos.csv` - Track workout type, duration, focus

## Tips

- **Date format**: Use YYYY-MM-DD (e.g., 2024-11-14)
- **Tags**: Use semicolons to separate (e.g., "pasta;seafood;italian")
- **Status**: Use "pending" → "uploaded" → "published"
- **Backup**: Save this folder regularly!

## Photo Naming Convention

- **Cooking**: food1.jpg, food2.jpg, food3.jpg...
- **Hiking**: hike1.jpg, hike2.jpg, hike3.jpg...
- **Boxing**: box1.jpg, box2.jpg, box3.jpg...

Keep numbers sequential as you add more!
