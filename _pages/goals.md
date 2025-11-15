---
layout: page
permalink: /goals/
title: Goals Tracker
description: Progress tracking and learning journal
nav: true
nav_order: 6
---

<style>
/* Goals Tracker Styling */
.goals-container {
  max-width: 900px;
  margin: 0 auto;
}

.goal-section {
  margin-bottom: 2.5rem;
  border-left: 3px solid #3498db;
  padding-left: 1.5rem;
}

.goal-section h2 {
  color: #2c3e50;
  font-size: 1.5rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

.goal-item {
  background: #fff;
  border: 1px solid #e1e8ed;
  border-radius: 8px;
  padding: 1.25rem;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.goal-item:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}

.goal-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.checkbox-wrapper {
  flex-shrink: 0;
}

.goal-checkbox {
  width: 24px;
  height: 24px;
  cursor: pointer;
  accent-color: #27ae60;
}

.goal-title {
  flex-grow: 1;
  font-weight: 600;
  color: #2c3e50;
  font-size: 1.1rem;
}

.goal-duration {
  background: #ecf0f1;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.85rem;
  color: #7f8c8d;
  font-weight: 500;
}

.goal-meta {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 0.75rem;
  margin-bottom: 0.75rem;
  padding-top: 0.5rem;
  border-top: 1px solid #ecf0f1;
}

.meta-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.meta-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: #95a5a6;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.meta-value {
  font-size: 0.9rem;
  color: #2c3e50;
}

.meta-input {
  border: 1px solid #dfe6e9;
  border-radius: 4px;
  padding: 0.4rem 0.6rem;
  font-size: 0.9rem;
  width: 100%;
  transition: border-color 0.2s ease;
}

.meta-input:focus {
  outline: none;
  border-color: #3498db;
}

.progress-bar-container {
  margin-top: 0.75rem;
  background: #ecf0f1;
  border-radius: 10px;
  height: 8px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #3498db 0%, #2ecc71 100%);
  border-radius: 10px;
  transition: width 0.5s ease;
}

.notes-section {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #ecf0f1;
}

.notes-label {
  font-size: 0.85rem;
  color: #7f8c8d;
  font-weight: 600;
  margin-bottom: 0.5rem;
  display: block;
}

.notes-textarea {
  width: 100%;
  min-height: 80px;
  border: 1px solid #dfe6e9;
  border-radius: 6px;
  padding: 0.75rem;
  font-size: 0.9rem;
  font-family: inherit;
  resize: vertical;
  transition: border-color 0.2s ease;
}

.notes-textarea:focus {
  outline: none;
  border-color: #3498db;
}

.status-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-not-started {
  background: #ecf0f1;
  color: #7f8c8d;
}

.status-in-progress {
  background: #fff3cd;
  color: #856404;
}

.status-completed {
  background: #d4edda;
  color: #155724;
}

.summary-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  color: white;
}

.stat-card {
  text-align: center;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  display: block;
}

.stat-label {
  font-size: 0.85rem;
  opacity: 0.9;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 0.25rem;
}

.deadline-warning {
  background: #fff3cd;
  border-left: 4px solid #ffc107;
  padding: 1rem;
  margin-bottom: 1.5rem;
  border-radius: 4px;
}

.deadline-warning strong {
  color: #856404;
}

.quick-checklist {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 2rem;
}

.quick-checklist h3 {
  margin: 0 0 1rem 0;
  color: #2c3e50;
  font-size: 1.25rem;
  font-weight: 600;
}

.checklist-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 0.5rem;
}

.checklist-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.2s ease;
}

.checklist-item:hover {
  background-color: rgba(52, 152, 219, 0.1);
}

.quick-check {
  width: 20px;
  height: 20px;
  cursor: pointer;
  flex-shrink: 0;
  accent-color: #27ae60;
}

.check-text {
  font-size: 0.95rem;
  color: #2c3e50;
  transition: all 0.3s ease;
}

.checklist-item:has(.quick-check:checked) .check-text {
  text-decoration: line-through;
  color: #95a5a6;
  opacity: 0.6;
}

@media (max-width: 768px) {
  .goal-meta {
    grid-template-columns: 1fr;
  }
  
  .summary-stats {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="goals-container">

<div class="deadline-warning">
  <strong>Target Completion:</strong> Sunday, November 23, 2025
</div>

<!-- QUICK CHECKLIST -->
<div class="quick-checklist">
  <h3>Quick Task List</h3>
  <div class="checklist-grid">
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="cpp-course">
      <span class="check-text">Scientific Computing C++ (21h)</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="hpc-course">
      <span class="check-text">HPC/GPU Programming (15h)</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="python-course">
      <span class="check-text">Python Scientific Projects</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="casl-videos">
      <span class="check-text">CASL Tutorial Videos (12h)</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="solidification-playlist">
      <span class="check-text">Solidification Playlist (20h)</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="casl-paper-1">
      <span class="check-text">CASL Main Paper #1</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="casl-paper-2">
      <span class="check-text">CASL Main Paper #2</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="casl-paper-3">
      <span class="check-text">CASL Main Paper #3</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="casl-paper-4">
      <span class="check-text">CASL Main Paper #4</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="jcp-paper-1">
      <span class="check-text">JCP Paper Review #1</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="jcp-paper-2">
      <span class="check-text">JCP Paper Review #2</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="jcp-paper-3">
      <span class="check-text">JCP Paper Review #3</span>
    </label>
    <label class="checklist-item">
      <input type="checkbox" class="quick-check" data-target="solidification-hw">
      <span class="check-text">Solidification HW (Due Nov 20)</span>
    </label>
  </div>
</div>

<div class="summary-stats">
  <div class="stat-card">
    <span class="stat-number" id="total-hours">68+</span>
    <span class="stat-label">Total Hours</span>
  </div>
  <div class="stat-card">
    <span class="stat-number" id="completed-items">0</span>
    <span class="stat-label">Completed</span>
  </div>
  <div class="stat-card">
    <span class="stat-number" id="progress-percent">0%</span>
    <span class="stat-label">Progress</span>
  </div>
</div>

<!-- COURSES SECTION -->
<div class="goal-section">
  <h2>Online Courses</h2>

  <div class="goal-item" data-item-id="cpp-course">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">Scientific Computing with C++</div>
      <div class="goal-duration">21 hours</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Platform</label>
        <div class="meta-value">Udemy</div>
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Start</label>
        <input type="date" class="meta-input" data-field="plannedStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Actual Start</label>
        <input type="date" class="meta-input" data-field="actualStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Progress %</label>
        <input type="number" class="meta-input progress-input" data-field="progress" placeholder="0-100" min="0" max="100">
      </div>
    </div>

    <div class="progress-bar-container">
      <div class="progress-bar" style="width: 0%"></div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Key Learnings & Notes</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="What did you learn? Any challenges? Important concepts?"></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="hpc-course">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">HPC/GPU Programming</div>
      <div class="goal-duration">15 hours</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Platform</label>
        <div class="meta-value">Udemy</div>
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Start</label>
        <input type="date" class="meta-input" data-field="plannedStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Actual Start</label>
        <input type="date" class="meta-input" data-field="actualStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Progress %</label>
        <input type="number" class="meta-input progress-input" data-field="progress" placeholder="0-100" min="0" max="100">
      </div>
    </div>

    <div class="progress-bar-container">
      <div class="progress-bar" style="width: 0%"></div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Key Learnings & Notes</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="What did you learn? Any challenges? Important concepts?"></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="python-course">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">Python with Scientific Projects</div>
      <div class="goal-duration">TBD</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Platform</label>
        <div class="meta-value">Udemy</div>
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Start</label>
        <input type="date" class="meta-input" data-field="plannedStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Actual Start</label>
        <input type="date" class="meta-input" data-field="actualStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Progress %</label>
        <input type="number" class="meta-input progress-input" data-field="progress" placeholder="0-100" min="0" max="100">
      </div>
    </div>

    <div class="progress-bar-container">
      <div class="progress-bar" style="width: 0%"></div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Key Learnings & Notes</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="What did you learn? Any challenges? Important concepts?"></textarea>
    </div>
  </div>

</div>

<!-- VIDEO TUTORIALS SECTION -->
<div class="goal-section">
  <h2>Video Tutorials</h2>

  <div class="goal-item" data-item-id="casl-videos">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">CASL Tutorial Videos</div>
      <div class="goal-duration">12 hours</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Platform</label>
        <div class="meta-value">YouTube/Lab Resources</div>
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Start</label>
        <input type="date" class="meta-input" data-field="plannedStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Actual Start</label>
        <input type="date" class="meta-input" data-field="actualStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Progress %</label>
        <input type="number" class="meta-input progress-input" data-field="progress" placeholder="0-100" min="0" max="100">
      </div>
    </div>

    <div class="progress-bar-container">
      <div class="progress-bar" style="width: 0%"></div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Key Learnings & Notes</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="What did you learn? Any challenges? Important concepts?"></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="solidification-playlist">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">Solidification Playlist</div>
      <div class="goal-duration">20 hours</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Platform</label>
        <div class="meta-value">YouTube</div>
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Start</label>
        <input type="date" class="meta-input" data-field="plannedStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Actual Start</label>
        <input type="date" class="meta-input" data-field="actualStart">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Progress %</label>
        <input type="number" class="meta-input progress-input" data-field="progress" placeholder="0-100" min="0" max="100">
      </div>
    </div>

    <div class="progress-bar-container">
      <div class="progress-bar" style="width: 0%"></div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Key Learnings & Notes</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="What did you learn? Any challenges? Important concepts?"></textarea>
    </div>
  </div>

</div>

<!-- READING SECTION -->
<div class="goal-section">
  <h2>Research Papers</h2>

  <div class="goal-item" data-item-id="casl-paper-1">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">CASL Main Paper #1</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Paper Title</label>
        <input type="text" class="meta-input" data-field="title" placeholder="Enter paper title">
      </div>
      <div class="meta-item">
        <label class="meta-label">Authors</label>
        <input type="text" class="meta-input" data-field="authors" placeholder="Enter authors">
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Date</label>
        <input type="date" class="meta-input" data-field="plannedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed Date</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Summary & Key Takeaways</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="Main contributions, methodology, results, how it relates to your work..."></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="casl-paper-2">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">CASL Main Paper #2</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Paper Title</label>
        <input type="text" class="meta-input" data-field="title" placeholder="Enter paper title">
      </div>
      <div class="meta-item">
        <label class="meta-label">Authors</label>
        <input type="text" class="meta-input" data-field="authors" placeholder="Enter authors">
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Date</label>
        <input type="date" class="meta-input" data-field="plannedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed Date</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Summary & Key Takeaways</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="Main contributions, methodology, results, how it relates to your work..."></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="casl-paper-3">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">CASL Main Paper #3</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Paper Title</label>
        <input type="text" class="meta-input" data-field="title" placeholder="Enter paper title">
      </div>
      <div class="meta-item">
        <label class="meta-label">Authors</label>
        <input type="text" class="meta-input" data-field="authors" placeholder="Enter authors">
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Date</label>
        <input type="date" class="meta-input" data-field="plannedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed Date</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Summary & Key Takeaways</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="Main contributions, methodology, results, how it relates to your work..."></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="casl-paper-4">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">CASL Main Paper #4</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Paper Title</label>
        <input type="text" class="meta-input" data-field="title" placeholder="Enter paper title">
      </div>
      <div class="meta-item">
        <label class="meta-label">Authors</label>
        <input type="text" class="meta-input" data-field="authors" placeholder="Enter authors">
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Date</label>
        <input type="date" class="meta-input" data-field="plannedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed Date</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Summary & Key Takeaways</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="Main contributions, methodology, results, how it relates to your work..."></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="jcp-paper-1">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">JCP Paper Review #1</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Paper Title</label>
        <input type="text" class="meta-input" data-field="title" placeholder="Enter paper title">
      </div>
      <div class="meta-item">
        <label class="meta-label">Authors</label>
        <input type="text" class="meta-input" data-field="authors" placeholder="Enter authors">
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Date</label>
        <input type="date" class="meta-input" data-field="plannedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed Date</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Summary & Key Takeaways</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="Main contributions, methodology, results, how it relates to your work..."></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="jcp-paper-2">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">JCP Paper Review #2</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Paper Title</label>
        <input type="text" class="meta-input" data-field="title" placeholder="Enter paper title">
      </div>
      <div class="meta-item">
        <label class="meta-label">Authors</label>
        <input type="text" class="meta-input" data-field="authors" placeholder="Enter authors">
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Date</label>
        <input type="date" class="meta-input" data-field="plannedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed Date</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Summary & Key Takeaways</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="Main contributions, methodology, results, how it relates to your work..."></textarea>
    </div>
  </div>

  <div class="goal-item" data-item-id="jcp-paper-3">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">JCP Paper Review #3</div>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Paper Title</label>
        <input type="text" class="meta-input" data-field="title" placeholder="Enter paper title">
      </div>
      <div class="meta-item">
        <label class="meta-label">Authors</label>
        <input type="text" class="meta-input" data-field="authors" placeholder="Enter authors">
      </div>
      <div class="meta-item">
        <label class="meta-label">Planned Date</label>
        <input type="date" class="meta-input" data-field="plannedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Completed Date</label>
        <input type="date" class="meta-input" data-field="completedDate">
      </div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Summary & Key Takeaways</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="Main contributions, methodology, results, how it relates to your work..."></textarea>
    </div>
  </div>

</div>

<!-- ASSIGNMENTS SECTION -->
<div class="goal-section">
  <h2>Assignments</h2>

  <div class="goal-item" data-item-id="solidification-hw">
    <div class="goal-header">
      <div class="checkbox-wrapper">
        <input type="checkbox" class="goal-checkbox" data-field="completed">
      </div>
      <div class="goal-title">Solidification Homework</div>
      <span class="status-badge status-not-started">Due Nov 20</span>
    </div>
    
    <div class="goal-meta">
      <div class="meta-item">
        <label class="meta-label">Assigned Date</label>
        <input type="date" class="meta-input" data-field="assignedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Due Date</label>
        <input type="date" class="meta-input" data-field="dueDate" value="2025-11-20">
      </div>
      <div class="meta-item">
        <label class="meta-label">Started</label>
        <input type="date" class="meta-input" data-field="startedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Submitted</label>
        <input type="date" class="meta-input" data-field="submittedDate">
      </div>
      <div class="meta-item">
        <label class="meta-label">Progress %</label>
        <input type="number" class="meta-input progress-input" data-field="progress" placeholder="0-100" min="0" max="100">
      </div>
    </div>

    <div class="progress-bar-container">
      <div class="progress-bar" style="width: 0%"></div>
    </div>

    <div class="notes-section">
      <label class="notes-label">Work Log & Notes</label>
      <textarea class="notes-textarea" data-field="notes" placeholder="Problems encountered, solutions found, questions to ask professor..."></textarea>
    </div>
  </div>

</div>

</div>

<script>
// Goals Tracker Auto-Save System
(function() {
  const STORAGE_KEY = 'goalsTrackerData_v1';
  
  // Load saved data on page load
  document.addEventListener('DOMContentLoaded', function() {
    loadAllData();
    attachEventListeners();
    updateStats();
  });
  
  function attachEventListeners() {
    // Sync quick checklist with detailed checkboxes
    document.querySelectorAll('.quick-check').forEach(quickCheck => {
      const targetId = quickCheck.getAttribute('data-target');
      const detailedItem = document.querySelector(`[data-item-id="${targetId}"]`);
      
      if (detailedItem) {
        const detailedCheck = detailedItem.querySelector('.goal-checkbox');
        
        // Sync quick check with detailed check on load
        quickCheck.checked = detailedCheck.checked;
        
        // When quick check changes, update detailed check
        quickCheck.addEventListener('change', function() {
          detailedCheck.checked = this.checked;
          saveItemData(detailedItem);
          updateStats();
        });
        
        // When detailed check changes, update quick check
        detailedCheck.addEventListener('change', function() {
          quickCheck.checked = this.checked;
          updateStats();
        });
      }
    });
    
    // Save on any input/textarea/checkbox change
    document.querySelectorAll('.goal-item').forEach(item => {
      const inputs = item.querySelectorAll('input, textarea');
      inputs.forEach(input => {
        input.addEventListener('change', () => saveItemData(item));
        input.addEventListener('input', () => saveItemData(item));
        
        // Update progress bar for number inputs
        if (input.classList.contains('progress-input')) {
          input.addEventListener('input', function() {
            const progressBar = item.querySelector('.progress-bar');
            if (progressBar && this.value) {
              progressBar.style.width = this.value + '%';
            }
            updateStats();
          });
        }
        
        // Update stats when checkbox changes
        if (input.type === 'checkbox') {
          input.addEventListener('change', updateStats);
        }
      });
    });
  }
  
  function saveItemData(item) {
    const itemId = item.getAttribute('data-item-id');
    if (!itemId) return;
    
    const data = {};
    const inputs = item.querySelectorAll('[data-field]');
    
    inputs.forEach(input => {
      const field = input.getAttribute('data-field');
      if (input.type === 'checkbox') {
        data[field] = input.checked;
      } else {
        data[field] = input.value;
      }
    });
    
    // Get existing data
    const allData = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    allData[itemId] = data;
    
    // Save back
    localStorage.setItem(STORAGE_KEY, JSON.stringify(allData));
  }
  
  function loadAllData() {
    const allData = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    
    document.querySelectorAll('.goal-item').forEach(item => {
      const itemId = item.getAttribute('data-item-id');
      if (!itemId || !allData[itemId]) return;
      
      const itemData = allData[itemId];
      const inputs = item.querySelectorAll('[data-field]');
      
      inputs.forEach(input => {
        const field = input.getAttribute('data-field');
        if (field in itemData) {
          if (input.type === 'checkbox') {
            input.checked = itemData[field];
          } else {
            input.value = itemData[field];
            
            // Update progress bar if it's a progress input
            if (input.classList.contains('progress-input') && itemData[field]) {
              const progressBar = item.querySelector('.progress-bar');
              if (progressBar) {
                progressBar.style.width = itemData[field] + '%';
              }
            }
          }
        }
      });
    });
  }
  
  function updateStats() {
    const checkboxes = document.querySelectorAll('.goal-checkbox');
    const total = checkboxes.length;
    const completed = Array.from(checkboxes).filter(cb => cb.checked).length;
    const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;
    
    document.getElementById('completed-items').textContent = completed + '/' + total;
    document.getElementById('progress-percent').textContent = percentage + '%';
  }
})();
</script>