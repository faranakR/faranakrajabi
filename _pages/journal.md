---
layout: none
permalink: /journal/
title: Work Journal
description: Daily tracking from Nov 16, 2025 to Jan 15, 2026
nav: true
nav_order: 7
---

<style>
/* Journal Styling */
.journal-container {
  max-width: 1000px;
  margin: 0 auto;
}

.journal-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
  text-align: center;
}

.journal-header h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2rem;
}

.countdown {
  font-size: 1.25rem;
  font-weight: 600;
  margin-top: 0.5rem;
}

.add-entry-section {
  background: #f8f9fa;
  border: 2px dashed #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 2rem;
}

.add-entry-section h3 {
  margin: 0 0 1rem 0;
  color: #2c3e50;
}

.entry-form {
  display: grid;
  gap: 1rem;
}

.form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #495057;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-input {
  border: 1px solid #ced4da;
  border-radius: 6px;
  padding: 0.75rem;
  font-size: 1rem;
  transition: border-color 0.2s ease;
}

.form-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-textarea {
  min-height: 120px;
  resize: vertical;
  font-family: inherit;
}

.image-upload-area {
  border: 2px dashed #ced4da;
  border-radius: 6px;
  padding: 1.5rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background: white;
}

.image-upload-area:hover {
  border-color: #667eea;
  background: #f8f9ff;
}

.image-upload-area.drag-over {
  border-color: #667eea;
  background: #e3e7ff;
}

.image-preview-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.image-preview {
  position: relative;
  border-radius: 6px;
  overflow: hidden;
  aspect-ratio: 1;
}

.image-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-remove {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  background: rgba(220, 53, 69, 0.9);
  color: white;
  border: none;
  border-radius: 50%;
  width: 28px;
  height: 28px;
  cursor: pointer;
  font-size: 1.2rem;
  line-height: 1;
  transition: background 0.2s ease;
}

.image-remove:hover {
  background: #dc3545;
}

.btn-save-entry {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 6px;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn-save-entry:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.entries-container {
  margin-top: 2rem;
}

.journal-entry {
  background: white;
  border: 1px solid #dee2e6;
  border-left: 4px solid #667eea;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  transition: box-shadow 0.3s ease;
}

.journal-entry:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.entry-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #f8f9fa;
}

.entry-date {
  font-size: 1.25rem;
  font-weight: 700;
  color: #2c3e50;
}

.entry-day {
  font-size: 0.85rem;
  color: #6c757d;
  margin-top: 0.25rem;
}

.entry-meta {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.meta-badge {
  background: #e9ecef;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #495057;
}

.hours-badge {
  background: #d4edda;
  color: #155724;
}

.mood-badge {
  background: #fff3cd;
  color: #856404;
}

.entry-section {
  margin-bottom: 1rem;
}

.section-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: #667eea;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.5rem;
}

.section-content {
  color: #495057;
  line-height: 1.6;
  white-space: pre-wrap;
}

.entry-images {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.entry-image {
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.entry-image:hover {
  transform: scale(1.02);
}

.entry-image img {
  width: 100%;
  height: auto;
  display: block;
}

.delete-entry {
  background: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.2s ease;
}

.delete-entry:hover {
  background: #c82333;
}

.stats-dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #667eea;
  display: block;
}

.stat-label {
  font-size: 0.9rem;
  color: #6c757d;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.5rem;
}

.filter-section {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1.5rem;
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  align-items: center;
}

.filter-label {
  font-weight: 600;
  color: #495057;
}

.filter-input {
  border: 1px solid #ced4da;
  border-radius: 4px;
  padding: 0.5rem;
}

@media (max-width: 768px) {
  .entry-header {
    flex-direction: column;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="journal-container">

<div class="journal-header">
  <h1>Defense Countdown Journal</h1>
  <p>Track your journey to Master's Defense Success</p>
  <div class="countdown">
    <span id="days-remaining">Loading...</span> days until January 15, 2026
  </div>
  <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.9;">
    <strong>Keyboard Shortcuts:</strong> ← / → arrows or P / N keys to navigate entries | Home / End for first/last
  </div>
</div>

<!-- Stats Dashboard -->
<div class="stats-dashboard">
  <div class="stat-card">
    <span class="stat-number" id="total-entries">0</span>
    <span class="stat-label">Journal Entries</span>
  </div>
  <div class="stat-card">
    <span class="stat-number" id="total-hours">0</span>
    <span class="stat-label">Total Hours Worked</span>
  </div>
  <div class="stat-card">
    <span class="stat-number" id="avg-hours">0</span>
    <span class="stat-label">Avg Hours/Day</span>
  </div>
  <div class="stat-card">
    <span class="stat-number" id="streak-days">0</span>
    <span class="stat-label">Current Streak</span>
  </div>
</div>

<!-- Add New Entry -->
<div class="add-entry-section">
  <h3>Add Today's Entry</h3>
  
  <div class="entry-form">
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Date</label>
        <input type="date" id="entry-date" class="form-input" required>
      </div>
      
      <div class="form-group">
        <label class="form-label">Hours Worked</label>
        <input type="number" id="entry-hours" class="form-input" placeholder="e.g., 4.5" step="0.5" min="0">
      </div>
      
      <div class="form-group">
        <label class="form-label">How I Feel Today</label>
        <select id="entry-mood" class="form-input">
          <option value="">Select mood...</option>
          <option value="Excellent">Excellent</option>
          <option value="Good">Good</option>
          <option value="Okay">Okay</option>
          <option value="Struggling">Struggling</option>
          <option value="Exhausted">Exhausted</option>
        </select>
      </div>
    </div>
    
    <div class="form-group">
      <label class="form-label">What I Worked On Today</label>
      <textarea id="entry-work" class="form-input form-textarea" placeholder="Describe what you accomplished, challenges faced, progress made..."></textarea>
    </div>
    
    <div class="form-group">
      <label class="form-label">What I Learned</label>
      <textarea id="entry-learned" class="form-input form-textarea" placeholder="Key insights, new concepts, aha moments..."></textarea>
    </div>
    
    <div class="form-group">
      <label class="form-label">Thoughts & Reflections</label>
      <textarea id="entry-thoughts" class="form-input form-textarea" placeholder="How you're feeling, worries, wins, anything on your mind..."></textarea>
    </div>
    
    <div class="form-group">
      <label class="form-label">Tomorrow's Goals</label>
      <textarea id="entry-tomorrow" class="form-input form-textarea" placeholder="What you want to accomplish tomorrow..."></textarea>
    </div>
    
    <div class="form-group">
      <label class="form-label">Add Images/Screenshots</label>
      <div class="image-upload-area" id="image-upload-area">
        <input type="file" id="image-input" accept="image/*" multiple style="display: none;">
        <p>Click or drag images here</p>
        <p style="font-size: 0.85rem; color: #6c757d; margin-top: 0.5rem;">Work screenshots, whiteboard photos, progress images</p>
      </div>
      <div class="image-preview-container" id="image-preview-container"></div>
    </div>
    
    <button class="btn-save-entry" id="save-entry-btn">Save Entry</button>
  </div>
</div>

<!-- Filters -->
<div class="filter-section">
  <span class="filter-label">Filter:</span>
  <input type="date" id="filter-date-from" class="filter-input" placeholder="From">
  <input type="date" id="filter-date-to" class="filter-input" placeholder="To">
  <select id="filter-mood" class="filter-input">
    <option value="">All Moods</option>
    <option value="Excellent">Excellent</option>
    <option value="Good">Good</option>
    <option value="Okay">Okay</option>
    <option value="Struggling">Struggling</option>
    <option value="Exhausted">Exhausted</option>
  </select>
  <button onclick="applyFilters()" class="filter-input" style="background: #667eea; color: white; border: none; cursor: pointer; padding: 0.5rem 1rem; border-radius: 4px;">Apply</button>
  <button onclick="clearFilters()" class="filter-input" style="background: #6c757d; color: white; border: none; cursor: pointer; padding: 0.5rem 1rem; border-radius: 4px;">Clear</button>
</div>

<!-- Journal Entries -->
<div class="entries-container" id="entries-container">
  <p style="text-align: center; color: #6c757d; padding: 2rem;">No entries yet. Add your first entry above!</p>
</div>

</div>

<script>
(function() {
  const STORAGE_KEY = 'workJournal_v1';
  let currentImages = [];
  let entries = [];
  
  // Initialize
  document.addEventListener('DOMContentLoaded', function() {
    // Set today's date as default
    document.getElementById('entry-date').valueAsDate = new Date();
    
    // Load entries
    loadEntries();
    
    // Setup image upload
    setupImageUpload();
    
    // Save entry button
    document.getElementById('save-entry-btn').addEventListener('click', saveEntry);
    
    // Update countdown
    updateCountdown();
    setInterval(updateCountdown, 3600000); // Update every hour
  });
  
  function updateCountdown() {
    const defenseDate = new Date('2026-01-15');
    const today = new Date();
    const diffTime = defenseDate - today;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    document.getElementById('days-remaining').textContent = diffDays;
  }
  
  function setupImageUpload() {
    const uploadArea = document.getElementById('image-upload-area');
    const input = document.getElementById('image-input');
    
    uploadArea.addEventListener('click', () => input.click());
    
    input.addEventListener('change', handleImageSelect);
    
    // Drag and drop
    uploadArea.addEventListener('dragover', (e) => {
      e.preventDefault();
      uploadArea.classList.add('drag-over');
    });
    
    uploadArea.addEventListener('dragleave', () => {
      uploadArea.classList.remove('drag-over');
    });
    
    uploadArea.addEventListener('drop', (e) => {
      e.preventDefault();
      uploadArea.classList.remove('drag-over');
      handleImageSelect({ target: { files: e.dataTransfer.files } });
    });
  }
  
  function handleImageSelect(e) {
    const files = Array.from(e.target.files);
    
    files.forEach(file => {
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (e) => {
          currentImages.push(e.target.result);
          displayImagePreviews();
        };
        reader.readAsDataURL(file);
      }
    });
  }
  
  function displayImagePreviews() {
    const container = document.getElementById('image-preview-container');
    container.innerHTML = '';
    
    currentImages.forEach((img, index) => {
      const preview = document.createElement('div');
      preview.className = 'image-preview';
      preview.innerHTML = `
        <img src="${img}" alt="Preview">
        <button class="image-remove" onclick="removeImage(${index})">×</button>
      `;
      container.appendChild(preview);
    });
  }
  
  window.removeImage = function(index) {
    currentImages.splice(index, 1);
    displayImagePreviews();
  };
  
  function saveEntry() {
    const entry = {
      id: Date.now(),
      date: document.getElementById('entry-date').value,
      hours: parseFloat(document.getElementById('entry-hours').value) || 0,
      mood: document.getElementById('entry-mood').value,
      work: document.getElementById('entry-work').value,
      learned: document.getElementById('entry-learned').value,
      thoughts: document.getElementById('entry-thoughts').value,
      tomorrow: document.getElementById('entry-tomorrow').value,
      images: [...currentImages]
    };
    
    if (!entry.date) {
      alert('Please select a date');
      return;
    }
    
    entries.unshift(entry);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(entries));
    
    // Clear form
    document.getElementById('entry-work').value = '';
    document.getElementById('entry-learned').value = '';
    document.getElementById('entry-thoughts').value = '';
    document.getElementById('entry-tomorrow').value = '';
    document.getElementById('entry-hours').value = '';
    document.getElementById('entry-mood').value = '';
    currentImages = [];
    displayImagePreviews();
    
    // Reload entries
    loadEntries();
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  
  function loadEntries() {
    const saved = localStorage.getItem(STORAGE_KEY);
    entries = saved ? JSON.parse(saved) : [];
    displayEntries(entries);
    updateStats();
  }
  
  function displayEntries(entriesToShow) {
    const container = document.getElementById('entries-container');
    
    if (entriesToShow.length === 0) {
      container.innerHTML = '<p style="text-align: center; color: #6c757d; padding: 2rem;">No entries found.</p>';
      return;
    }
    
    container.innerHTML = entriesToShow.map(entry => {
      const date = new Date(entry.date);
      const dayName = date.toLocaleDateString('en-US', { weekday: 'long' });
      const dateStr = date.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
      
      return `
        <div class="journal-entry">
          <div class="entry-header">
            <div>
              <div class="entry-date">${dateStr}</div>
              <div class="entry-day">${dayName}</div>
            </div>
            <div class="entry-meta">
              ${entry.hours ? `<span class="meta-badge hours-badge">${entry.hours} hours</span>` : ''}
              ${entry.mood ? `<span class="meta-badge mood-badge">${entry.mood}</span>` : ''}
              <button class="delete-entry" onclick="deleteEntry(${entry.id})">Delete</button>
            </div>
          </div>
          
          ${entry.work ? `
            <div class="entry-section">
              <div class="section-title">What I Worked On</div>
              <div class="section-content">${entry.work}</div>
            </div>
          ` : ''}
          
          ${entry.learned ? `
            <div class="entry-section">
              <div class="section-title">What I Learned</div>
              <div class="section-content">${entry.learned}</div>
            </div>
          ` : ''}
          
          ${entry.thoughts ? `
            <div class="entry-section">
              <div class="section-title">Thoughts & Reflections</div>
              <div class="section-content">${entry.thoughts}</div>
            </div>
          ` : ''}
          
          ${entry.tomorrow ? `
            <div class="entry-section">
              <div class="section-title">Tomorrow's Goals</div>
              <div class="section-content">${entry.tomorrow}</div>
            </div>
          ` : ''}
          
          ${entry.images && entry.images.length > 0 ? `
            <div class="entry-images">
              ${entry.images.map(img => `
                <div class="entry-image">
                  <img src="${img}" alt="Entry image" onclick="window.open('${img}', '_blank')">
                </div>
              `).join('')}
            </div>
          ` : ''}
        </div>
      `;
    }).join('');
  }
  
  window.deleteEntry = function(id) {
    if (confirm('Delete this entry?')) {
      entries = entries.filter(e => e.id !== id);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(entries));
      loadEntries();
    }
  };
  
  function updateStats() {
    const totalEntries = entries.length;
    const totalHours = entries.reduce((sum, e) => sum + (e.hours || 0), 0);
    const avgHours = totalEntries > 0 ? (totalHours / totalEntries).toFixed(1) : 0;
    
    // Calculate streak
    const sortedDates = entries.map(e => e.date).sort().reverse();
    let streak = 0;
    let currentDate = new Date();
    currentDate.setHours(0, 0, 0, 0);
    
    for (let dateStr of sortedDates) {
      const entryDate = new Date(dateStr);
      entryDate.setHours(0, 0, 0, 0);
      
      const diffDays = Math.floor((currentDate - entryDate) / (1000 * 60 * 60 * 24));
      
      if (diffDays === streak) {
        streak++;
      } else if (diffDays > streak) {
        break;
      }
    }
    
    document.getElementById('total-entries').textContent = totalEntries;
    document.getElementById('total-hours').textContent = totalHours.toFixed(1);
    document.getElementById('avg-hours').textContent = avgHours;
    document.getElementById('streak-days').textContent = streak;
  }
  
  window.applyFilters = function() {
    const dateFrom = document.getElementById('filter-date-from').value;
    const dateTo = document.getElementById('filter-date-to').value;
    const mood = document.getElementById('filter-mood').value;
    
    let filtered = entries;
    
    if (dateFrom) {
      filtered = filtered.filter(e => e.date >= dateFrom);
    }
    
    if (dateTo) {
      filtered = filtered.filter(e => e.date <= dateTo);
    }
    
    if (mood) {
      filtered = filtered.filter(e => e.mood === mood);
    }
    
    displayEntries(filtered);
  };
  
  window.clearFilters = function() {
    document.getElementById('filter-date-from').value = '';
    document.getElementById('filter-date-to').value = '';
    document.getElementById('filter-mood').value = '';
    displayEntries(entries);
  };
  
  // Keyboard navigation
  let currentEntryIndex = 0;
  
  document.addEventListener('keydown', function(e) {
    // Only trigger if not typing in an input/textarea
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
      return;
    }
    
    const journalEntries = document.querySelectorAll('.journal-entry');
    
    if (journalEntries.length === 0) return;
    
    // Left arrow or 'p' for previous
    if (e.key === 'ArrowLeft' || e.key === 'p' || e.key === 'P') {
      e.preventDefault();
      currentEntryIndex = Math.max(0, currentEntryIndex - 1);
      scrollToEntry(journalEntries[currentEntryIndex]);
    }
    
    // Right arrow or 'n' for next
    if (e.key === 'ArrowRight' || e.key === 'n' || e.key === 'N') {
      e.preventDefault();
      currentEntryIndex = Math.min(journalEntries.length - 1, currentEntryIndex + 1);
      scrollToEntry(journalEntries[currentEntryIndex]);
    }
    
    // Home key - go to first entry
    if (e.key === 'Home') {
      e.preventDefault();
      currentEntryIndex = 0;
      scrollToEntry(journalEntries[0]);
    }
    
    // End key - go to last entry
    if (e.key === 'End') {
      e.preventDefault();
      currentEntryIndex = journalEntries.length - 1;
      scrollToEntry(journalEntries[currentEntryIndex]);
    }
  });
  
  function scrollToEntry(entry) {
    // Remove previous highlight
    document.querySelectorAll('.journal-entry').forEach(e => {
      e.style.borderLeft = '4px solid #667eea';
      e.style.transform = 'scale(1)';
    });
    
    // Highlight current entry
    entry.style.borderLeft = '4px solid #dc3545';
    entry.style.transform = 'scale(1.01)';
    entry.style.transition = 'all 0.3s ease';
    
    // Scroll to entry
    entry.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
})();
</script>