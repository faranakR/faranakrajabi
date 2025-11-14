---
permalink: /tracker/
title: "Daily Tracker"
layout: none
---

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daily Tracker</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: #0f0f1e;
  color: #e4e4e7;
  overflow-x: hidden;
}

.container {
  width: 100%;
  max-width: 100%;
  padding: 2em 3em;
}

/* Header */
.header {
  text-align: center;
  margin-bottom: 2em;
}

.date-display {
  font-size: 2.5em;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 0.2em;
}

.day-count {
  font-size: 1.1em;
  color: #a1a1aa;
  font-weight: 500;
}

.nav-pills {
  display: flex;
  justify-content: center;
  gap: 0.5em;
  margin-top: 1.5em;
}

.nav-pill {
  padding: 0.6em 1.5em;
  background: #1e1e2e;
  border: 2px solid #2e2e3e;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 500;
  font-size: 0.95em;
  transition: all 0.2s;
  color: #e4e4e7;
}

.nav-pill:hover {
  background: #2e2e3e;
  border-color: #4c4f69;
}

.nav-pill.active {
  background: linear-gradient(135deg, #4c1d95 0%, #1e3a8a 100%);
  border-color: #6366f1;
  color: white;
}

/* Main Layout */
.main-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0;
  margin-top: 2em;
}

/* Task Checklist at Top */
.checklist-section {
  margin-bottom: 3em;
  padding-bottom: 2em;
  border-bottom: 2px solid #2e2e3e;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5em;
}

.section-title {
  font-size: 1.5em;
  font-weight: 700;
  color: #a78bfa;
}

.add-task-btn {
  padding: 0.7em 1.5em;
  background: linear-gradient(135deg, #4c1d95 0%, #1e3a8a 100%);
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9em;
  transition: all 0.2s;
}

.add-task-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.3);
}

.task-table {
  width: 100%;
  border-collapse: collapse;
}

.task-table thead {
  border-bottom: 2px solid #2e2e3e;
}

.task-table th {
  padding: 1em 0.5em;
  text-align: left;
  font-size: 0.85em;
  font-weight: 600;
  color: #a1a1aa;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.task-table td {
  padding: 1em 0.5em;
  border-bottom: 1px solid #1e1e2e;
}

.task-checkbox {
  width: 20px;
  height: 20px;
  cursor: pointer;
  accent-color: #6366f1;
}

.task-name-input {
  background: transparent;
  border: none;
  border-bottom: 1px solid transparent;
  color: #e4e4e7;
  font-size: 1em;
  padding: 0.3em;
  width: 100%;
  transition: border-color 0.2s;
}

.task-name-input:focus {
  outline: none;
  border-bottom-color: #6366f1;
}

.task-name-input.completed {
  text-decoration: line-through;
  color: #71717a;
}

.time-input-small {
  background: transparent;
  border: none;
  border-bottom: 1px solid transparent;
  color: #e4e4e7;
  font-size: 0.9em;
  padding: 0.3em;
  width: 80px;
  transition: border-color 0.2s;
}

.time-input-small:focus {
  outline: none;
  border-bottom-color: #6366f1;
}

.priority-select {
  background: #1e1e2e;
  border: 1px solid #2e2e3e;
  color: #e4e4e7;
  padding: 0.4em;
  border-radius: 6px;
  font-size: 0.85em;
  cursor: pointer;
}

.priority-select:focus {
  outline: none;
  border-color: #6366f1;
}

.percentage-input {
  background: transparent;
  border: none;
  border-bottom: 1px solid transparent;
  color: #e4e4e7;
  font-size: 0.9em;
  padding: 0.3em;
  width: 60px;
  transition: border-color 0.2s;
}

.percentage-input:focus {
  outline: none;
  border-bottom-color: #6366f1;
}

.delete-task-btn {
  background: transparent;
  border: none;
  color: #71717a;
  cursor: pointer;
  font-size: 1.2em;
  padding: 0.3em;
  transition: color 0.2s;
}

.delete-task-btn:hover {
  color: #ef4444;
}

/* Timeline - NO BOXES */
.timeline-section {
  margin-top: 2em;
}

.time-block {
  margin-bottom: 3em;
  padding-left: 2.5em;
  border-left: 3px solid #2e2e3e;
  position: relative;
}

.time-block::before {
  content: '';
  position: absolute;
  left: -8px;
  top: 5px;
  width: 13px;
  height: 13px;
  background: linear-gradient(135deg, #4c1d95 0%, #1e3a8a 100%);
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
}

.time-label {
  font-size: 0.85em;
  font-weight: 600;
  color: #a78bfa;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 1em;
}

.time-input-group {
  display: flex;
  gap: 1.5em;
  margin-bottom: 1.5em;
  flex-wrap: wrap;
}

.time-input {
  display: flex;
  align-items: center;
  gap: 0.5em;
  font-size: 0.9em;
}

.time-input label {
  color: #a1a1aa;
  font-weight: 500;
}

.time-input input {
  padding: 0.5em 0.8em;
  border: none;
  border-bottom: 2px solid #2e2e3e;
  background: transparent;
  color: #e4e4e7;
  font-family: 'Inter', sans-serif;
  font-size: 0.95em;
  transition: border-color 0.2s;
}

.time-input input:focus {
  outline: none;
  border-bottom-color: #6366f1;
}

/* NO BOXES for text areas */
.text-area {
  width: 100%;
  min-height: 100px;
  padding: 1em 0;
  border: none;
  border-bottom: 1px solid #2e2e3e;
  background: transparent;
  color: #e4e4e7;
  font-family: 'Inter', sans-serif;
  font-size: 0.95em;
  line-height: 1.6;
  resize: vertical;
  transition: border-color 0.2s;
  margin-top: 0.5em;
}

.text-area:focus {
  outline: none;
  border-bottom-color: #6366f1;
}

.text-area::placeholder {
  color: #52525b;
}

.prompt-text {
  font-size: 0.9em;
  color: #a1a1aa;
  margin-bottom: 0.3em;
  margin-top: 1.5em;
  font-weight: 500;
}

/* Save Button */
.save-btn {
  position: fixed;
  bottom: 2em;
  right: 2em;
  padding: 1.2em 2.5em;
  background: linear-gradient(135deg, #4c1d95 0%, #1e3a8a 100%);
  color: white;
  border: none;
  border-radius: 50px;
  font-weight: 600;
  font-size: 1em;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
  z-index: 1000;
}

.save-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.5);
}

.save-status {
  position: fixed;
  bottom: 5em;
  right: 2em;
  color: #4ade80;
  font-size: 0.9em;
  font-weight: 500;
  z-index: 1000;
}

/* Footer */
.footer-links {
  text-align: center;
  margin-top: 3em;
  padding-top: 2em;
  border-top: 2px solid #2e2e3e;
}

.footer-links a {
  color: #a78bfa;
  text-decoration: none;
  font-weight: 500;
  margin: 0 1em;
}

.footer-links a:hover {
  color: #c4b5fd;
  text-decoration: underline;
}

/* Default Checklist Items */
.routine-check-item {
  display: flex;
  align-items: center;
  gap: 0.8em;
  padding: 0.7em;
  margin-bottom: 0.5em;
  transition: background 0.2s;
  border-radius: 8px;
}

.routine-check-item:hover {
  background: #1e1e2e;
}

.routine-checkbox {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: #6366f1;
  flex-shrink: 0;
}

.routine-label {
  color: #e4e4e7;
  font-size: 0.9em;
  cursor: pointer;
  flex: 1;
}

.routine-label.completed {
  text-decoration: line-through;
  color: #71717a;
}

.sub-item {
  margin-left: 2em;
  font-size: 0.85em;
  color: #a1a1aa;
}

@media (max-width: 968px) {
  .container {
    padding: 1em;
  }
  
  .task-table {
    font-size: 0.85em;
  }
  
  .time-input-group {
    flex-direction: column;
  }
}
</style>
</head>
<body>

<div class="container">
  
  <!-- Header -->
  <div class="header">
    <div class="date-display" id="date-display">Friday, November 14</div>
    <div class="day-count" id="day-count">Day 1 of 32 until Dec 15</div>
    
    <div class="nav-pills">
      <button class="nav-pill" onclick="changeDay(-1)">← Yesterday</button>
      <button class="nav-pill active" onclick="loadToday()">Today</button>
      <button class="nav-pill" onclick="changeDay(1)">Tomorrow →</button>
    </div>
  </div>

  <!-- TODAY'S CHECKLIST -->
  <div class="checklist-section">
    <div class="section-header">
      <h2 class="section-title">✅ Today's Checklist</h2>
      <button class="add-task-btn" onclick="addTask()">+ Add Task</button>
    </div>
    
    <table class="task-table">
      <thead>
        <tr>
          <th style="width: 40px;">Done</th>
          <th>Task</th>
          <th style="width: 100px;">Est. Time</th>
          <th style="width: 100px;">Actual Time</th>
          <th style="width: 120px;">Priority</th>
          <th style="width: 80px;">% Done</th>
          <th style="width: 40px;"></th>
        </tr>
      </thead>
      <tbody id="task-tbody">
        <!-- Tasks will be added here -->
      </tbody>
    </table>
  </div>

  <!-- DEFAULT DAILY CHECKLIST -->
  <div class="checklist-section" style="margin-top: 3em;">
    <div class="section-header">
      <h2 class="section-title">📋 Daily Routine Checklist</h2>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2em;">
      
      <!-- Morning Routine -->
      <div>
        <h3 style="color: #a78bfa; font-size: 1.1em; margin-bottom: 1em; font-weight: 600;">☀️ Morning Routine</h3>
        <div id="morning-routine-checks"></div>
      </div>

      <!-- Night Routine -->
      <div>
        <h3 style="color: #a78bfa; font-size: 1.1em; margin-bottom: 1em; font-weight: 600;">🌙 Night Routine</h3>
        <div id="night-routine-checks"></div>
      </div>

      <!-- Daily Goals -->
      <div>
        <h3 style="color: #a78bfa; font-size: 1.1em; margin-bottom: 1em; font-weight: 600;">🎯 Daily Goals</h3>
        <div id="daily-goals-checks"></div>
      </div>
      
    </div>
  </div>

  <!-- JOURNAL TIMELINE -->
  <div class="timeline-section">
    
    <!-- Morning -->
    <div class="time-block">
      <div class="time-label">☀️ Morning</div>
      
      <div class="time-input-group">
        <div class="time-input">
          <label>Woke up</label>
          <input type="time" id="wake-time">
        </div>
        <div class="time-input">
          <label>Got up</label>
          <input type="time" id="getup-time">
        </div>
        <div class="time-input">
          <label>Sleep quality (1-10)</label>
          <input type="number" id="sleep-quality" min="1" max="10" placeholder="1-10" style="width: 60px;">
        </div>
      </div>
      
      <div class="prompt-text">What fears and resentments?</div>
      <textarea class="text-area" id="morning-fears" placeholder="I'm afraid of..."></textarea>
      
      <div class="prompt-text">Premeditated notes</div>
      <textarea class="text-area" id="morning-notes" placeholder="What I'm thinking about today..."></textarea>
    </div>

    <!-- Work -->
    <div class="time-block">
      <div class="time-label">💼 Work</div>
      
      <div class="time-input-group">
        <div class="time-input">
          <label>Started</label>
          <input type="time" id="work-start">
        </div>
        <div class="time-input">
          <label>Focus hours</label>
          <input type="number" id="focus-hours" min="0" max="12" step="0.5" placeholder="0-12" style="width: 70px;">
        </div>
        <div class="time-input">
          <label>Energy peak</label>
          <input type="time" id="energy-peak">
        </div>
      </div>
      
      <div class="prompt-text">What pulled me away from work?</div>
      <textarea class="text-area" id="work-distractions" placeholder=""></textarea>
      
      <div class="prompt-text">What I accomplished</div>
      <textarea class="text-area" id="work-accomplished" placeholder=""></textarea>
    </div>

    <!-- Evening -->
    <div class="time-block">
      <div class="time-label">🌙 Evening</div>
      
      <div class="prompt-text">What fears and resentments?</div>
      <textarea class="text-area" id="evening-fears" placeholder="End of day thoughts..."></textarea>
      
      <div class="prompt-text">Premeditated notes</div>
      <textarea class="text-area" id="evening-notes" placeholder=""></textarea>
    </div>

    <!-- Before Bed -->
    <div class="time-block">
      <div class="time-label">📝 Before Bed</div>
      
      <div class="time-input-group">
        <div class="time-input">
          <label>Going to sleep</label>
          <input type="time" id="sleep-time">
        </div>
        <div class="time-input">
          <label>Mood (one word)</label>
          <input type="text" id="mood" placeholder="e.g., neutral" style="width: 120px;">
        </div>
      </div>
      
      <div class="prompt-text">What actually happened today?</div>
      <textarea class="text-area" id="day-summary" style="min-height: 150px;" placeholder="Free write about your day..."></textarea>
      
      <div class="prompt-text">Did I move my body? How?</div>
      <textarea class="text-area" id="movement" placeholder="Kickboxing, walk, yoga, or no"></textarea>
      
      <div class="prompt-text">What am I avoiding looking at?</div>
      <textarea class="text-area" id="avoiding" placeholder=""></textarea>
      
      <div class="prompt-text">If tomorrow is exactly like today, I'd change:</div>
      <textarea class="text-area" id="tomorrow-change" placeholder=""></textarea>
    </div>

    <!-- Gratitude -->
    <div class="time-block">
      <div class="time-label">💖 Gratitude</div>
      
      <div class="prompt-text">Three things I'm grateful for today:</div>
      <textarea class="text-area" id="gratitude" style="min-height: 100px;" placeholder="1. 
2. 
3. "></textarea>
      
      <div class="prompt-text">One win today (however small):</div>
      <textarea class="text-area" id="win-today" placeholder="What went well?"></textarea>
    </div>

    <!-- Free Journal -->
    <div class="time-block">
      <div class="time-label">✍️ Free Journal</div>
      
      <div class="prompt-text">Write anything on your mind... no rules, just write:</div>
      <textarea class="text-area" id="free-journal" style="min-height: 200px;" placeholder="Stream of consciousness... thoughts, feelings, dreams, frustrations, ideas..."></textarea>
    </div>

  </div>

  <!-- Footer -->
  <div class="footer-links">
    <a href="YOUR_GOOGLE_DOC_LINK" target="_blank">📝 Google Doc Journal</a>
    <a href="/sleep-stats/">😴 Sleep Stats</a>
    <a href="/">← Back to Home</a>
  </div>

</div>

<!-- Floating Save Button -->
<button class="save-btn" onclick="saveEntry()">💾 Save Entry</button>
<div class="save-status" id="save-status"></div>

<script>
let currentDate = new Date();
const startDate = new Date('2025-11-14');
const endDate = new Date('2025-12-15');

function updateDisplay() {
  const options = { weekday: 'long', month: 'long', day: 'numeric' };
  document.getElementById('date-display').textContent = currentDate.toLocaleDateString('en-US', options);
  
  const daysPassed = Math.floor((currentDate - startDate) / (1000 * 60 * 60 * 24));
  const totalDays = Math.floor((endDate - startDate) / (1000 * 60 * 60 * 24));
  
  document.getElementById('day-count').textContent = `Day ${daysPassed + 1} of ${totalDays} until Dec 15`;
}

function getDateKey() {
  return currentDate.toISOString().split('T')[0];
}

// ==================== TASK MANAGEMENT ====================
function addTask() {
  const dateKey = getDateKey();
  const tasks = JSON.parse(localStorage.getItem('tasks-' + dateKey) || '[]');
  
  tasks.push({
    id: Date.now(),
    done: false,
    name: '',
    estimatedTime: '',
    actualTime: '',
    priority: 'medium',
    percentage: 0
  });
  
  localStorage.setItem('tasks-' + dateKey, JSON.stringify(tasks));
  loadTasks();
}

function loadTasks() {
  const dateKey = getDateKey();
  const tasks = JSON.parse(localStorage.getItem('tasks-' + dateKey) || '[]');
  const tbody = document.getElementById('task-tbody');
  tbody.innerHTML = '';
  
  if (tasks.length === 0) {
    // Add one empty row to start
    const row = document.createElement('tr');
    row.innerHTML = `
      <td style="text-align: center;">
        <input type="checkbox" class="task-checkbox" disabled style="opacity: 0.3;">
      </td>
      <td colspan="6" style="text-align: center; color: #71717a; padding: 2em; font-style: italic;">
        Click "+ Add Task" above to start adding tasks
      </td>
    `;
    tbody.appendChild(row);
  } else {
    tasks.forEach(task => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td style="text-align: center;">
          <input type="checkbox" class="task-checkbox" ${task.done ? 'checked' : ''} 
                 onchange="toggleTaskDone('${dateKey}', ${task.id})">
        </td>
        <td>
          <input type="text" class="task-name-input ${task.done ? 'completed' : ''}" 
                 value="${task.name}" 
                 onchange="updateTask('${dateKey}', ${task.id}, 'name', this.value)"
                 placeholder="Task name...">
        </td>
        <td>
          <input type="text" class="time-input-small" 
                 value="${task.estimatedTime}" 
                 onchange="updateTask('${dateKey}', ${task.id}, 'estimatedTime', this.value)"
                 placeholder="2h">
        </td>
        <td>
          <input type="text" class="time-input-small" 
                 value="${task.actualTime}" 
                 onchange="updateTask('${dateKey}', ${task.id}, 'actualTime', this.value)"
                 placeholder="1.5h">
        </td>
        <td>
          <select class="priority-select" 
                  onchange="updateTask('${dateKey}', ${task.id}, 'priority', this.value)">
            <option value="low" ${task.priority === 'low' ? 'selected' : ''}>Low</option>
            <option value="medium" ${task.priority === 'medium' ? 'selected' : ''}>Medium</option>
            <option value="high" ${task.priority === 'high' ? 'selected' : ''}>High</option>
          </select>
        </td>
        <td style="text-align: center;">
          <input type="number" class="percentage-input" 
                 value="${task.percentage}" 
                 min="0" max="100"
                 onchange="updateTask('${dateKey}', ${task.id}, 'percentage', this.value)"
                 placeholder="0">%
        </td>
        <td style="text-align: center;">
          <button class="delete-task-btn" onclick="deleteTask('${dateKey}', ${task.id})">×</button>
        </td>
      `;
      tbody.appendChild(row);
    });
  }
}

function toggleTaskDone(dateKey, taskId) {
  const tasks = JSON.parse(localStorage.getItem('tasks-' + dateKey) || '[]');
  const task = tasks.find(t => t.id === taskId);
  if (task) {
    task.done = !task.done;
    if (task.done) task.percentage = 100;
    localStorage.setItem('tasks-' + dateKey, JSON.stringify(tasks));
    loadTasks();
  }
}

function updateTask(dateKey, taskId, field, value) {
  const tasks = JSON.parse(localStorage.getItem('tasks-' + dateKey) || '[]');
  const task = tasks.find(t => t.id === taskId);
  if (task) {
    task[field] = value;
    localStorage.setItem('tasks-' + dateKey, JSON.stringify(tasks));
  }
}

function deleteTask(dateKey, taskId) {
  if (confirm('Delete this task?')) {
    let tasks = JSON.parse(localStorage.getItem('tasks-' + dateKey) || '[]');
    tasks = tasks.filter(t => t.id !== taskId);
    localStorage.setItem('tasks-' + dateKey, JSON.stringify(tasks));
    loadTasks();
  }
}

// ==================== JOURNAL SAVE/LOAD ====================
function saveEntry() {
  const data = {
    date: getDateKey(),
    wakeTime: document.getElementById('wake-time').value,
    getupTime: document.getElementById('getup-time').value,
    sleepQuality: document.getElementById('sleep-quality').value,
    morningFears: document.getElementById('morning-fears').value,
    morningNotes: document.getElementById('morning-notes').value,
    workStart: document.getElementById('work-start').value,
    focusHours: document.getElementById('focus-hours').value,
    energyPeak: document.getElementById('energy-peak').value,
    workDistractions: document.getElementById('work-distractions').value,
    workAccomplished: document.getElementById('work-accomplished').value,
    eveningFears: document.getElementById('evening-fears').value,
    eveningNotes: document.getElementById('evening-notes').value,
    sleepTime: document.getElementById('sleep-time').value,
    mood: document.getElementById('mood').value,
    daySummary: document.getElementById('day-summary').value,
    movement: document.getElementById('movement').value,
    avoiding: document.getElementById('avoiding').value,
    tomorrowChange: document.getElementById('tomorrow-change').value,
    gratitude: document.getElementById('gratitude').value,
    winToday: document.getElementById('win-today').value,
    freeJournal: document.getElementById('free-journal').value
  };
  
  localStorage.setItem('journal-' + getDateKey(), JSON.stringify(data));
  
  document.getElementById('save-status').textContent = '✓ Saved';
  setTimeout(() => {
    document.getElementById('save-status').textContent = '';
  }, 2000);
}

function loadEntry() {
  const saved = localStorage.getItem('journal-' + getDateKey());
  
  if (saved) {
    const data = JSON.parse(saved);
    
    document.getElementById('wake-time').value = data.wakeTime || '';
    document.getElementById('getup-time').value = data.getupTime || '';
    document.getElementById('sleep-quality').value = data.sleepQuality || '';
    document.getElementById('morning-fears').value = data.morningFears || '';
    document.getElementById('morning-notes').value = data.morningNotes || '';
    document.getElementById('work-start').value = data.workStart || '';
    document.getElementById('focus-hours').value = data.focusHours || '';
    document.getElementById('energy-peak').value = data.energyPeak || '';
    document.getElementById('work-distractions').value = data.workDistractions || '';
    document.getElementById('work-accomplished').value = data.workAccomplished || '';
    document.getElementById('evening-fears').value = data.eveningFears || '';
    document.getElementById('evening-notes').value = data.eveningNotes || '';
    document.getElementById('sleep-time').value = data.sleepTime || '';
    document.getElementById('mood').value = data.mood || '';
    document.getElementById('day-summary').value = data.daySummary || '';
    document.getElementById('movement').value = data.movement || '';
    document.getElementById('avoiding').value = data.avoiding || '';
    document.getElementById('tomorrow-change').value = data.tomorrowChange || '';
    document.getElementById('gratitude').value = data.gratitude || '';
    document.getElementById('win-today').value = data.winToday || '';
    document.getElementById('free-journal').value = data.freeJournal || '';
  } else {
    document.querySelectorAll('input, textarea').forEach(el => el.value = '');
  }
}

function changeDay(delta) {
  currentDate.setDate(currentDate.getDate() + delta);
  updateDisplay();
  loadEntry();
  loadTasks();
}

function loadToday() {
  currentDate = new Date();
  updateDisplay();
  loadEntry();
  loadTasks();
}

// Auto-save every 30 seconds
setInterval(() => {
  const hasContent = document.querySelector('textarea');
  if (hasContent && hasContent.value.trim()) {
    saveEntry();
  }
}, 30000);

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeTracker);
} else {
  initializeTracker();
}

function initializeTracker() {
  updateDisplay();
  loadEntry();
  loadTasks();
  loadRoutineChecklists();
}

// ==================== DEFAULT ROUTINE CHECKLISTS ====================
const morningRoutine = [
  { id: 'morning-skincare', text: 'Skin care', sub: ['Cleanser', 'Exfoliate', 'Niacinamide', 'Hyaluronic acid', 'Moisturizer', 'Sunscreen'] },
  { id: 'morning-makebed', text: 'Make bed' },
  { id: 'morning-tea', text: 'Green tea or juice' },
  { id: 'morning-meditation', text: 'Meditation' },
  { id: 'morning-vacuum', text: 'Vacuum massaging the stomach' },
  { id: 'morning-pills', text: 'Pills', sub: ['Adderall', 'Trazodone', 'Vitamin D', 'Ferritin'] },
  { id: 'morning-planning', text: 'Planning the day' },
  { id: 'morning-journal', text: 'Journal' },
  { id: 'morning-gratitude', text: 'Gratitude' }
];

const nightRoutine = [
  { id: 'night-reading', text: 'Reading book before bed' },
  { id: 'night-brush', text: 'Brush teeth' },
  { id: 'night-skincare', text: 'Skin care', sub: ['Cleanse', 'Differin'] },
  { id: 'night-meditation', text: 'Meditate' },
  { id: 'night-ponyo', text: 'Playing with Ponyo' },
  { id: 'night-journal', text: 'Night journal' }
];

const dailyGoals = [
  { id: 'goal-workout', text: 'Morning or night workout (90 minutes)' },
  { id: 'goal-meditation', text: 'Meditation 1×' },
  { id: 'goal-work', text: '≥ 8 hours of work' },
  { id: 'goal-salads', text: 'Had two bowls of salads today' },
  { id: 'goal-french', text: '30 minutes French practice' },
  { id: 'goal-chess', text: '15 minutes chess practice' }
];

function loadRoutineChecklists() {
  const dateKey = getDateKey();
  const routineData = JSON.parse(localStorage.getItem('routine-' + dateKey) || '{}');
  
  renderRoutineSection('morning-routine-checks', morningRoutine, routineData);
  renderRoutineSection('night-routine-checks', nightRoutine, routineData);
  renderRoutineSection('daily-goals-checks', dailyGoals, routineData);
}

function renderRoutineSection(containerId, items, routineData) {
  const container = document.getElementById(containerId);
  container.innerHTML = '';
  
  items.forEach(item => {
    const isChecked = routineData[item.id] || false;
    
    const itemDiv = document.createElement('div');
    itemDiv.className = 'routine-check-item';
    
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'routine-checkbox';
    checkbox.checked = isChecked;
    checkbox.onchange = () => toggleRoutineItem(item.id);
    
    const label = document.createElement('label');
    label.className = 'routine-label' + (isChecked ? ' completed' : '');
    label.textContent = item.text;
    label.onclick = () => {
      checkbox.checked = !checkbox.checked;
      toggleRoutineItem(item.id);
    };
    
    itemDiv.appendChild(checkbox);
    itemDiv.appendChild(label);
    container.appendChild(itemDiv);
    
    // Add sub-items if they exist
    if (item.sub) {
      item.sub.forEach(subText => {
        const subDiv = document.createElement('div');
        subDiv.className = 'sub-item';
        subDiv.textContent = '• ' + subText;
        container.appendChild(subDiv);
      });
    }
  });
}

function toggleRoutineItem(itemId) {
  const dateKey = getDateKey();
  const routineData = JSON.parse(localStorage.getItem('routine-' + dateKey) || '{}');
  routineData[itemId] = !routineData[itemId];
  localStorage.setItem('routine-' + dateKey, JSON.stringify(routineData));
  loadRoutineChecklists();
}
</script>

</body>
</html>