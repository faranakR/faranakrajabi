---
permalink: /schedule/confirmed/
# title: "Meeting Confirmed"
layout: single
author_profile: true
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
.confirmation-page {
  max-width: 100%;
  margin: 0;
}

.success-message {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 40px;
  align-items: center;
  padding: 40px 20px 30px 20px;
}

.success-message .text-side {
  text-align: left;
}

.success-message h1 {
  font-size: 48px;
  font-weight: 700;
  color: #111827;
  margin: 0 0 16px 0;
}

.success-message p {
  font-size: 20px;
  color: #6b7280;
  margin: 0 0 30px 0;
}

.ponyo-circle {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto 30px auto;
  border: 4px solid #ffffff;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.ponyo-circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.meeting-details {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 30px;
  margin-bottom: 30px;
}

.detail-row {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 20px 0;
  border-bottom: 1px solid #f3f4f6;
}

.detail-row:last-child {
  border-bottom: none;
}

.detail-icon {
  width: 50px;
  height: 50px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  flex-shrink: 0;
}

.detail-icon.calendar {
  background: #dbeafe;
  color: #3b82f6;
}

.detail-icon.user {
  background: #e0e7ff;
  color: #6366f1;
}

.detail-icon.location {
  background: #fef3c7;
  color: #f59e0b;
}

.detail-content h3 {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  color: #6b7280;
  letter-spacing: 0.5px;
  margin: 0 0 6px 0;
}

.detail-content p {
  font-size: 17px;
  color: #111827;
  font-weight: 500;
  margin: 0;
}

.action-buttons {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-bottom: 30px;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 18px 24px;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  color: white;
}

.action-btn i {
  font-size: 20px;
}

.action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.btn-gcal {
  background: #4285f4;
}

.btn-gcal:hover {
  background: #3367d6;
}

.btn-zoom {
  background: #2d8cff;
}

.btn-zoom:hover {
  background: #0b5cff;
}

.btn-reminder {
  background: #f59e0b;
}

.btn-reminder:hover {
  background: #d97706;
}

.btn-email {
  background: #ef4444;
}

.btn-email:hover {
  background: #dc2626;
}

.info-box {
  background: #f0f9ff;
  border: 2px solid #3b82f6;
  border-left: 4px solid #3b82f6;
  border-radius: 12px;
  padding: 20px;
}

.info-box p {
  margin: 0;
  color: #1e40af;
  font-size: 15px;
  line-height: 1.8;
}

.info-box strong {
  font-weight: 700;
}

.info-box a {
  color: #1e40af;
  font-weight: 600;
  text-decoration: none;
}

.info-box a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .action-buttons {
    grid-template-columns: 1fr;
  }

  .success-message h1 {
    font-size: 36px;
  }

  .success-message p {
    font-size: 18px;
  }
}
</style>

<div class="confirmation-page">

  <!-- Success Message -->
    <div class="success-message">
    <div class="text-side">
        <h1 id="thankYouName">Thank You!</h1>
        <p>Thanks for accepting the invitation</p>
    </div>
    
    <div class="ponyo-circle">
        <img src="/assets/images/ponyo3.jpg" alt="Ponyo">
    </div>
    </div>

  <!-- Meeting Details -->
  <div class="meeting-details">
    <div class="detail-row">
      <div class="detail-icon calendar">
        <i class="far fa-calendar"></i>
      </div>
      <div class="detail-content">
        <h3>When</h3>
        <p id="meetingWhen">Loading...</p>
      </div>
    </div>

    <div class="detail-row">
      <div class="detail-icon user">
        <i class="far fa-user"></i>
      </div>
      <div class="detail-content">
        <h3>Guest</h3>
        <p id="guestEmail">you</p>
      </div>
    </div>

    <div class="detail-row">
      <div class="detail-icon location">
        <i class="fas fa-video"></i>
      </div>
      <div class="detail-content">
        <h3>Location</h3>
        <p id="meetingLocation">Zoom (link in email)</p>
      </div>
    </div>
  </div>

  <!-- Action Buttons -->
  <div class="action-buttons">
    <button class="action-btn btn-gcal" onclick="addToGoogleCalendar()">
      <i class="fab fa-google"></i>
      Add to Calendar
    </button>

    <button class="action-btn btn-zoom" onclick="joinZoom()">
      <i class="fas fa-video"></i>
      Join Zoom
    </button>

    <button class="action-btn btn-reminder" onclick="setReminder()">
      <i class="far fa-bell"></i>
      Set Reminder
    </button>

    <button class="action-btn btn-email" onclick="emailHost()">
      <i class="far fa-envelope"></i>
      Email Faranak
    </button>
  </div>

  <!-- Info Box -->
  <div class="info-box">
    <p>
      <strong><i class="fas fa-envelope"></i> Confirmation Sent:</strong> We've sent a calendar invitation to your email with the Zoom link and all meeting details. 
      Need to reschedule? Contact me at <a href="mailto:faranakrajabi@ucsb.edu">faranakrajabi@ucsb.edu</a>
    </p>
  </div>

</div>

<script>
let meetingData = {};

window.addEventListener('DOMContentLoaded', function() {
  const params = new URLSearchParams(window.location.search);
  
  meetingData = {
    firstName: params.get('firstName') || '',
    lastName: params.get('lastName') || '',
    email: params.get('email') || 'your email',
    datetime: params.get('datetime'),
    duration: params.get('duration') || '30 minutes',
    topic: params.get('topic') || 'Meeting',
    zoom: params.get('zoom') || '',
    token: params.get('token')
  };
  
  if (meetingData.firstName) {
    document.getElementById('thankYouName').textContent = `Thank You, ${meetingData.firstName}!`;
  }
  
  if (meetingData.datetime) {
    const dt = new Date(meetingData.datetime);
    const formatted = dt.toLocaleString('en-US', {
      weekday: 'long',
      month: 'long',
      day: 'numeric',
      year: 'numeric',
      hour: 'numeric',
      minute: '2-digit',
      hour12: true,
      timeZone: 'America/Los_Angeles'
    });
    document.getElementById('meetingWhen').textContent = formatted + ' (' + meetingData.duration + ')';
  }
  
  document.getElementById('guestEmail').textContent = meetingData.email;
  document.getElementById('meetingLocation').textContent = meetingData.zoom || 'Zoom (link in email)';
  
  notifyAdmin();
});

function notifyAdmin() {
  // TODO: Send notification to admin (you)
  console.log('Admin notification:', meetingData);
}

function addToGoogleCalendar() {
  if (!meetingData.datetime) return;
  
  const start = new Date(meetingData.datetime);
  const mins = parseInt(meetingData.duration) || 30;
  const end = new Date(start.getTime() + mins * 60000);
  
  const fmt = (d) => d.toISOString().replace(/-|:|\.\d+/g, '');
  
  const details = `Meeting with Faranak Rajabi${meetingData.zoom ? '\n\nJoin: ' + meetingData.zoom : ''}`;
  
  const url = `https://calendar.google.com/calendar/render?action=TEMPLATE` +
    `&text=${encodeURIComponent(meetingData.topic)}` +
    `&dates=${fmt(start)}/${fmt(end)}` +
    `&details=${encodeURIComponent(details)}` +
    `&location=${encodeURIComponent(meetingData.zoom || 'Zoom')}`;
  
  window.open(url, '_blank');
}

function joinZoom() {
  if (meetingData.zoom) {
    window.open(meetingData.zoom, '_blank');
  } else {
    alert('The Zoom link has been sent to your email!');
  }
}

function setReminder() {
  alert('Reminder will be sent 1 hour before the meeting to: ' + meetingData.email);
  // TODO: Backend integration
}

function emailHost() {
  const subject = encodeURIComponent('Re: Meeting on ' + new Date(meetingData.datetime).toLocaleDateString());
  const body = encodeURIComponent(`Hi Faranak,\n\nI have a question about our upcoming meeting.\n\nBest,\n${meetingData.firstName} ${meetingData.lastName}`);
  
  window.location.href = `mailto:faranakrajabi@ucsb.edu?subject=${subject}&body=${body}`;
}
</script>