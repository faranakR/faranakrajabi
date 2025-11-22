---
permalink: /admin/invite/
title: "Create Meeting Invitation"
layout: single
author_profile: true
---

<style>
.admin-container {
  max-width: 700px;
  margin: 40px auto;
  padding: 20px;
}

.admin-header {
  text-align: center;
  margin-bottom: 40px;
}

.admin-header h1 {
  font-size: 28px;
  font-weight: 700;
  color: #111827;
  margin-bottom: 8px;
}

.admin-header p {
  color: #6b7280;
  font-size: 14px;
}

.invite-form {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 24px;
}

.form-group label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 12px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 14px;
  font-family: inherit;
  transition: border-color 0.2s;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  outline: none;
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group small {
  display: block;
  margin-top: 6px;
  color: #6b7280;
  font-size: 12px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.submit-btn {
  width: 100%;
  padding: 14px;
  background: #111827;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.submit-btn:hover {
  background: #1f2937;
  transform: translateY(-1px);
}

.submit-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.result-box {
  margin-top: 24px;
  padding: 16px;
  border-radius: 8px;
  display: none;
}

.result-box.success {
  background: #ecfdf5;
  border: 1px solid #10b981;
  color: #065f46;
}

.result-box.error {
  background: #fef2f2;
  border: 1px solid #ef4444;
  color: #991b1b;
}

.invitation-link {
  margin-top: 16px;
  padding: 12px;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-family: monospace;
  font-size: 12px;
  word-break: break-all;
}

.copy-btn {
  margin-top: 8px;
  padding: 8px 16px;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 13px;
  cursor: pointer;
}

.copy-btn:hover {
  background: #1d4ed8;
}

@media (max-width: 600px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="admin-container">
  <div class="admin-header">
    <h1>📧 Create Meeting Invitation</h1>
    <p>Send a meeting invitation with accept/decline option</p>
  </div>

  <form class="invite-form" id="inviteForm">
    
    <div class="form-group">
      <label for="guestEmail">Guest Email *</label>
      <input type="email" id="guestEmail" required placeholder="student@ucsb.edu">
      <small>Email address of the person you're inviting</small>
    </div>

    <div class="form-group">
      <label for="guestName">Guest Name</label>
      <input type="text" id="guestName" placeholder="John Doe">
      <small>Optional - will be used in the email</small>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="meetingDate">Date *</label>
        <input type="date" id="meetingDate" required>
      </div>

      <div class="form-group">
        <label for="meetingTime">Time *</label>
        <input type="time" id="meetingTime" required>
      </div>
    </div>

    <div class="form-group">
      <label for="duration">Duration *</label>
      <select id="duration" required>
        <option value="15 minutes">15 minutes</option>
        <option value="30 minutes" selected>30 minutes</option>
        <option value="45 minutes">45 minutes</option>
        <option value="1 hour">1 hour</option>
        <option value="1.5 hours">1.5 hours</option>
        <option value="2 hours">2 hours</option>
      </select>
    </div>

    <div class="form-group">
      <label for="topic">Meeting Topic *</label>
      <input type="text" id="topic" required placeholder="Research Discussion">
    </div>

    <div class="form-group">
      <label for="location">Location/Platform *</label>
      <select id="locationType" onchange="toggleLocationInput()">
        <option value="zoom">Zoom</option>
        <option value="meet">Google Meet</option>
        <option value="teams">Microsoft Teams</option>
        <option value="in-person">In Person</option>
        <option value="other">Other</option>
      </select>
    </div>

    <div class="form-group" id="zoomLinkGroup">
      <label for="zoomLink">Zoom Link</label>
      <input type="url" id="zoomLink" placeholder="https://zoom.us/j/123456789">
      <small>Leave empty to generate later</small>
    </div>

    <div class="form-group">
      <label for="message">Additional Message (Optional)</label>
      <textarea id="message" rows="3" placeholder="Looking forward to discussing..."></textarea>
    </div>

    <button type="submit" class="submit-btn" id="submitBtn">
      📨 Generate Invitation Link
    </button>

    <div class="result-box" id="resultBox"></div>
  </form>
</div>

<script>
function toggleLocationInput() {
  const type = document.getElementById('locationType').value;
  const zoomGroup = document.getElementById('zoomLinkGroup');
  const zoomInput = document.getElementById('zoomLink');
  
  if (type === 'zoom') {
    zoomGroup.style.display = 'block';
    zoomInput.placeholder = 'https://zoom.us/j/123456789';
  } else if (type === 'meet') {
    zoomGroup.style.display = 'block';
    zoomInput.placeholder = 'https://meet.google.com/xxx-yyyy-zzz';
  } else if (type === 'teams') {
    zoomGroup.style.display = 'block';
    zoomInput.placeholder = 'https://teams.microsoft.com/...';
  } else if (type === 'in-person') {
    zoomGroup.style.display = 'block';
    zoomInput.placeholder = 'Engineering Building, Room 301';
  } else {
    zoomGroup.style.display = 'block';
    zoomInput.placeholder = 'Meeting location';
  }
}

document.getElementById('inviteForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const submitBtn = document.getElementById('submitBtn');
  submitBtn.disabled = true;
  submitBtn.textContent = '⏳ Generating...';
  
  // Get form data
  const formData = {
    email: document.getElementById('guestEmail').value,
    name: document.getElementById('guestName').value,
    date: document.getElementById('meetingDate').value,
    time: document.getElementById('meetingTime').value,
    duration: document.getElementById('duration').value,
    topic: document.getElementById('topic').value,
    locationType: document.getElementById('locationType').value,
    location: document.getElementById('zoomLink').value,
    message: document.getElementById('message').value
  };
  
  // Create datetime string
  const datetime = `${formData.date}T${formData.time}:00`;
  
  // Generate unique token (in production, this should come from backend)
  const token = generateToken();
  
  // Create invitation URL
  const inviteUrl = `${window.location.origin}/schedule/?invite=${token}&email=${encodeURIComponent(formData.email)}&name=${encodeURIComponent(formData.name)}&datetime=${datetime}&duration=${encodeURIComponent(formData.duration)}&topic=${encodeURIComponent(formData.topic)}&location=${encodeURIComponent(formData.location || formData.locationType)}`;
  
  // In production, send this to your backend:
  // fetch('/api/send-invitation', {
  //   method: 'POST',
  //   headers: { 'Content-Type': 'application/json' },
  //   body: JSON.stringify({
  //     ...formData,
  //     token: token,
  //     inviteUrl: inviteUrl
  //   })
  // })
  // .then(res => res.json())
  // .then(data => {
  //   showSuccess(inviteUrl);
  // })
  // .catch(error => {
  //   showError(error.message);
  // });
  
  // For now, just show the link
  setTimeout(() => {
    showSuccess(inviteUrl, formData);
    submitBtn.disabled = false;
    submitBtn.textContent = '📨 Generate Invitation Link';
  }, 1000);
});

function generateToken() {
  return Math.random().toString(36).substring(2, 15) + 
         Math.random().toString(36).substring(2, 15);
}

function showSuccess(url, data) {
  const resultBox = document.getElementById('resultBox');
  resultBox.className = 'result-box success';
  resultBox.style.display = 'block';
  
  resultBox.innerHTML = `
    <strong>✓ Invitation Link Generated!</strong>
    <p style="margin: 12px 0 8px 0; font-size: 13px;">Copy and send this link to ${data.email}:</p>
    <div class="invitation-link">${url}</div>
    <button class="copy-btn" onclick="copyToClipboard('${url}')">📋 Copy Link</button>
    
    <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #10b981;">
      <strong>📧 Email Template:</strong>
      <div style="margin-top: 12px; padding: 12px; background: white; border: 1px solid #d1d5db; border-radius: 6px; font-size: 13px; line-height: 1.6;">
        Hi ${data.name || 'there'},<br><br>
        I'd like to invite you to a meeting:<br><br>
        <strong>Topic:</strong> ${data.topic}<br>
        <strong>Date/Time:</strong> ${formatDateTime(data.date, data.time)}<br>
        <strong>Duration:</strong> ${data.duration}<br>
        <strong>Location:</strong> ${data.location || data.locationType}<br><br>
        ${data.message ? data.message + '<br><br>' : ''}
        Please confirm your attendance by clicking here:<br>
        <a href="${url}">${url}</a><br><br>
        Best regards,<br>
        Faranak Rajabi
      </div>
      <button class="copy-btn" onclick="copyEmailTemplate('${data.name || ''}', '${data.topic}', '${data.date}', '${data.time}', '${data.duration}', '${data.location || data.locationType}', '${data.message}', '${url}')" style="margin-top: 8px;">
        📋 Copy Email
      </button>
    </div>
  `;
  
  // Scroll to result
  resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function showError(message) {
  const resultBox = document.getElementById('resultBox');
  resultBox.className = 'result-box error';
  resultBox.style.display = 'block';
  resultBox.innerHTML = `<strong>✗ Error:</strong> ${message}`;
}

function formatDateTime(date, time) {
  const d = new Date(`${date}T${time}`);
  return d.toLocaleString('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
    hour12: true
  });
}

function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('✓ Link copied to clipboard!');
  });
}

function copyEmailTemplate(name, topic, date, time, duration, location, message, url) {
  const template = `Hi ${name || 'there'},

I'd like to invite you to a meeting:

Topic: ${topic}
Date/Time: ${formatDateTime(date, time)}
Duration: ${duration}
Location: ${location}

${message ? message + '\n\n' : ''}Please confirm your attendance by clicking here:
${url}

Best regards,
Faranak Rajabi`;

  navigator.clipboard.writeText(template).then(() => {
    alert('✓ Email template copied to clipboard!');
  });
}

// Set default date to today
document.getElementById('meetingDate').valueAsDate = new Date();
</script>