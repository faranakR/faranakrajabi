---
permalink: /sleep-stats/
title: "Sleep & Wake Tracking"
layout: single
author_profile: false
classes: wide
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

body {
  font-family: 'Inter', sans-serif;
  background: #f8f9fa;
}

.stats-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2em 1em;
}

.header-section {
  text-align: center;
  margin-bottom: 3em;
}

.header-section h1 {
  font-size: 2.5em;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.5em;
}

.last-updated {
  color: #6c757d;
  font-size: 0.9em;
}

.plots-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2em;
  margin-bottom: 3em;
}

.plot-card {
  background: white;
  border-radius: 16px;
  padding: 2em;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}

.plot-card h2 {
  font-size: 1.5em;
  margin-bottom: 1em;
  color: #1a1a1a;
}

.plot-card img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5em;
  margin-bottom: 3em;
}

.stat-card {
  background: white;
  border-radius: 16px;
  padding: 2em;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  text-align: center;
}

.stat-number {
  font-size: 2.5em;
  font-weight: 700;
  color: #5865f2;
  margin-bottom: 0.3em;
}

.stat-label {
  font-size: 1em;
  color: #6c757d;
  font-weight: 500;
}

.stat-sublabel {
  font-size: 0.85em;
  color: #adb5bd;
  margin-top: 0.5em;
}

.quick-entry {
  background: white;
  border-radius: 16px;
  padding: 2em;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  margin-bottom: 2em;
}

.quick-entry h2 {
  font-size: 1.5em;
  margin-bottom: 1.5em;
  color: #1a1a1a;
}

.input-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1em;
  margin-bottom: 1.5em;
}

.input-group label {
  display: block;
  font-weight: 500;
  color: #495057;
  margin-bottom: 0.5em;
  font-size: 0.9em;
}

.input-group input {
  width: 100%;
  padding: 0.8em;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-family: 'Inter', sans-serif;
  font-size: 1em;
}

.input-group input:focus {
  outline: none;
  border-color: #5865f2;
}

.submit-btn {
  background: #5865f2;
  color: white;
  border: none;
  padding: 1em 2em;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1em;
  cursor: pointer;
  transition: all 0.2s;
}

.submit-btn:hover {
  background: #4752c4;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(88, 101, 242, 0.3);
}

.info-box {
  background: #e3f2fd;
  border-left: 4px solid #2196f3;
  padding: 1.5em;
  border-radius: 8px;
  margin-bottom: 2em;
}

.info-box p {
  margin: 0;
  color: #1565c0;
}

.chart-placeholder {
  background: #f8f9fa;
  padding: 3em;
  text-align: center;
  border-radius: 8px;
  color: #6c757d;
}

@media (max-width: 768px) {
  .input-row {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="stats-container">
  
  <div class="header-section">
    <h1>😴 Sleep & Wake Tracking</h1>
    <p class="last-updated">Last updated: <span id="last-updated">Loading...</span></p>
  </div>

  <!-- Quick Stats -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-number" id="avg-wake">--:--</div>
      <div class="stat-label">Average Wake Time</div>
      <div class="stat-sublabel">All time</div>
    </div>
    
    <div class="stat-card">
      <div class="stat-number" id="avg-sleep">--:--</div>
      <div class="stat-label">Average Bedtime</div>
      <div class="stat-sublabel">All time</div>
    </div>
    
    <div class="stat-card">
      <div class="stat-number" id="total-entries">0</div>
      <div class="stat-label">Total Entries</div>
      <div class="stat-sublabel">Since July 2025</div>
    </div>
    
    <div class="stat-card">
      <div class="stat-number" id="latest-wake">--:--</div>
      <div class="stat-label">Latest Wake Time</div>
      <div class="stat-sublabel" id="latest-wake-date">--</div>
    </div>
  </div>

  <!-- Quick Entry Form -->
  <div class="quick-entry">
    <h2>📝 Quick Entry</h2>
    
    <div class="info-box">
      <p><strong>Note:</strong> This form saves to your browser. Run the MATLAB script to generate updated plots and statistics.</p>
    </div>
    
    <div class="input-row">
      <div class="input-group">
        <label>Date:</label>
        <input type="date" id="entry-date" value="">
      </div>
      
      <div class="input-group">
        <label>Wake Up Time:</label>
        <input type="time" id="wake-time" placeholder="e.g., 10:15">
      </div>
      
      <div class="input-group">
        <label>Bedtime (night before):</label>
        <input type="time" id="bed-time" placeholder="e.g., 03:30">
      </div>
    </div>
    
    <button class="submit-btn" onclick="saveQuickEntry()">💾 Save Entry</button>
    <div id="save-message" style="margin-top: 1em; color: #28a745; font-weight: 500;"></div>
  </div>

  <!-- MATLAB Plots -->
  <div class="plots-grid">
    
    <div class="plot-card">
      <h2>📈 Wake-Up Times</h2>
      <div class="chart-placeholder" id="wakeup-chart">
        <p>📊 Upload your <code>wakeup_plot.png</code> from MATLAB here</p>
        <p style="font-size: 0.9em; margin-top: 1em;">
          Place the file in: <code>/assets/images/sleep/wakeup_plot.png</code>
        </p>
      </div>
      <!-- <img src="/assets/images/sleep/wakeup_plot.png" alt="Wake-up tracking plot"> -->
    </div>
    
    <div class="plot-card">
      <h2>🌙 Bedtimes</h2>
      <div class="chart-placeholder" id="bedtime-chart">
        <p>📊 Upload your <code>bedtime_plot.png</code> from MATLAB here</p>
        <p style="font-size: 0.9em; margin-top: 1em;">
          Place the file in: <code>/assets/images/sleep/bedtime_plot.png</code>
        </p>
      </div>
      <!-- <img src="/assets/images/sleep/bedtime_plot.png" alt="Bedtime tracking plot"> -->
    </div>
    
    <div class="plot-card">
      <h2>📊 Combined View</h2>
      <div class="chart-placeholder" id="combined-chart">
        <p>📊 Upload your <code>combined_plot.png</code> from MATLAB here</p>
        <p style="font-size: 0.9em; margin-top: 1em;">
          Place the file in: <code>/assets/images/sleep/combined_plot.png</code>
        </p>
      </div>
      <!-- <img src="/assets/images/sleep/combined_plot.png" alt="Combined tracking plot"> -->
    </div>
    
  </div>

  <!-- Instructions -->
  <div class="plot-card">
    <h2>🔄 How to Update</h2>
    <ol style="line-height: 2;">
      <li>Fill in the quick entry form above or edit the MATLAB script directly</li>
      <li>Run <code>wakeups_add_and_plot_updated.m</code> in MATLAB</li>
      <li>Copy the generated PNG files to <code>/assets/images/sleep/</code> in your website repo</li>
      <li>Uncomment the <code>&lt;img&gt;</code> tags in this page (and comment out the placeholders)</li>
      <li>Commit and push to GitHub</li>
      <li>Your plots will update automatically!</li>
    </ol>
  </div>

  <div style="text-align: center; margin-top: 3em; padding-top: 2em; border-top: 2px solid #e9ecef;">
    <a href="/tracker/" style="color: #5865f2; text-decoration: none; font-weight: 500; margin: 0 1em;">← Back to Daily Tracker</a>
    <a href="/" style="color: #5865f2; text-decoration: none; font-weight: 500; margin: 0 1em;">Home</a>
  </div>

</div>

<script>
// Set today's date as default
document.getElementById('entry-date').valueAsDate = new Date();

// Load and display stats from localStorage
function loadStats() {
  const entries = Object.keys(localStorage)
    .filter(k => k.startsWith('sleep-entry-'))
    .map(k => JSON.parse(localStorage.getItem(k)))
    .sort((a, b) => new Date(a.date) - new Date(b.date));
  
  if (entries.length === 0) {
    return;
  }
  
  // Calculate averages
  const avgWakeMins = entries.reduce((sum, e) => sum + timeToMinutes(e.wakeTime), 0) / entries.length;
  const avgBedMins = entries.reduce((sum, e) => sum + timeToMinutes(e.bedTime), 0) / entries.length;
  
  document.getElementById('avg-wake').textContent = minutesToTime(avgWakeMins);
  document.getElementById('avg-sleep').textContent = minutesToTime(avgBedMins);
  document.getElementById('total-entries').textContent = entries.length;
  
  // Latest entry
  const latest = entries[entries.length - 1];
  document.getElementById('latest-wake').textContent = latest.wakeTime;
  document.getElementById('latest-wake-date').textContent = new Date(latest.date).toLocaleDateString();
  
  document.getElementById('last-updated').textContent = new Date().toLocaleString();
}

function timeToMinutes(timeStr) {
  const [h, m] = timeStr.split(':').map(Number);
  return h * 60 + m;
}

function minutesToTime(mins) {
  const h = Math.floor(mins / 60);
  const m = Math.round(mins % 60);
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`;
}

function saveQuickEntry() {
  const date = document.getElementById('entry-date').value;
  const wakeTime = document.getElementById('wake-time').value;
  const bedTime = document.getElementById('bed-time').value;
  
  if (!date || !wakeTime || !bedTime) {
    alert('Please fill in all fields');
    return;
  }
  
  const entry = {
    date: date,
    wakeTime: wakeTime,
    bedTime: bedTime,
    timestamp: new Date().toISOString()
  };
  
  localStorage.setItem('sleep-entry-' + date, JSON.stringify(entry));
  
  document.getElementById('save-message').textContent = '✓ Entry saved! Remember to run MATLAB script to update plots.';
  setTimeout(() => {
    document.getElementById('save-message').textContent = '';
  }, 3000);
  
  loadStats();
}

// Export function for MATLAB
function exportForMATLAB() {
  const entries = Object.keys(localStorage)
    .filter(k => k.startsWith('sleep-entry-'))
    .map(k => JSON.parse(localStorage.getItem(k)))
    .sort((a, b) => new Date(a.date) - new Date(b.date));
  
  let matlab = '% Generated from web tracker\n';
  matlab += 'newWakeDates = datetime([\n';
  entries.forEach(e => {
    const d = new Date(e.date);
    matlab += `    ${d.getFullYear()} ${d.getMonth() + 1} ${d.getDate()};\n`;
  });
  matlab += ']);\n\n';
  
  matlab += 'newWakeMins = [\n';
  entries.forEach(e => {
    const [h, m] = e.wakeTime.split(':').map(Number);
    matlab += `    ${h}*60 + ${m};\n`;
  });
  matlab += '];\n\n';
  
  matlab += 'newBedMins = [\n';
  entries.forEach(e => {
    const [h, m] = e.bedTime.split(':').map(Number);
    const mins = h < 12 ? (h + 24) * 60 + m : h * 60 + m; // Adjust for after midnight
    matlab += `    ${Math.floor(mins / 60)}*60 + ${mins % 60};\n`;
  });
  matlab += '];\n';
  
  const blob = new Blob([matlab], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'sleep_entries_for_matlab.m';
  a.click();
}

// Initialize
loadStats();
</script>