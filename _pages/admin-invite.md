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

<!-- EmailJS Library -->
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script type="text/javascript">
  (function(){
    emailjs.init("M_6AgBlV0CHoFIjLP");
  })();
</script>

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
      📨 Send Invitation Email
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
  submitBtn.textContent = '📧 Sending Email...';
  
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
  
  const datetime = `${formData.date}T${formData.time}:00`;
  
  const dt = new Date(datetime);
  const formattedDateTime = dt.toLocaleString('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
    hour12: true,
    timeZone: 'America/Los_Angeles'
  });
  
  const token = generateToken();
  
  const inviteUrl = `${window.location.origin}/schedule/?invite=${token}&email=${encodeURIComponent(formData.email)}&name=${encodeURIComponent(formData.name)}&datetime=${datetime}&duration=${encodeURIComponent(formData.duration)}&topic=${encodeURIComponent(formData.topic)}&location=${encodeURIComponent(formData.location || formData.locationType)}`;
  
  const emailParams = {
    guest_name: formData.name || 'there',
    guest_email: formData.email,
    topic: formData.topic,
    meeting_datetime: formattedDateTime,
    duration: formData.duration,
    location: formData.location || formData.locationType,
    message: formData.message || '',
    invitation_link: inviteUrl,
    to_email: formData.email
  };
  
  emailjs.send('service_3lm4w34', 'template_k7d8bxs', emailParams)
    .then(function(response) {
      console.log('Email sent successfully!', response);
      showSuccess(inviteUrl, formData);
      submitBtn.disabled = false;
      submitBtn.textContent = '📨 Send Invitation Email';
    }, function(error) {
      console.error('Email failed to send:', error);
      showError('Failed to send email: ' + error.text);
      submitBtn.disabled = false;
      submitBtn.textContent = '📨 Send Invitation Email';
    });
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
    <strong>✓ Invitation Email Sent!</strong>
    <p style="margin: 12px 0 8px 0; font-size: 13px;">Professional invitation sent to ${data.email}</p>
    <div class="invitation-link">${url}</div>
    <button class="copy-btn" onclick="copyToClipboard('${url}')">📋 Copy Link</button>
  `;
  
  resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function showError(message) {
  const resultBox = document.getElementById('resultBox');
  resultBox.className = 'result-box error';
  resultBox.style.display = 'block';
  resultBox.innerHTML = `<strong>✗ Error:</strong> ${message}`;
}

function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('✓ Link copied to clipboard!');
  });
}

document.getElementById('meetingDate').valueAsDate = new Date();
</script>