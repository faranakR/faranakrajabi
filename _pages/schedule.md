---
permalink: /schedule/
# title: "Meeting Invitation"
layout: single
author_profile: true
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
.invitation-page {
  max-width: 100%;
  margin: 0;
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

.detail-icon.clock {
  background: #fef3c7;
  color: #f59e0b;
}

.detail-icon.topic {
  background: #e0e7ff;
  color: #6366f1;
}

.detail-icon.location {
  background: #fce7f3;
  color: #ec4899;
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

.name-section {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 30px;
  margin-bottom: 30px;
}

.name-section h2 {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
  margin: 0 0 20px 0;
}

.name-fields {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 20px;
}

.field-group label {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
}

.field-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 15px;
  transition: all 0.2s;
}

.field-group input:focus {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.rsvp-section {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 30px;
  margin-bottom: 30px;
}

.rsvp-question {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 20px;
  text-align: center;
}

.rsvp-buttons {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.rsvp-btn {
  padding: 20px;
  border: 2px solid #e5e7eb;
  background: white;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.rsvp-btn i {
  font-size: 32px;
  margin-bottom: 4px;
}

.rsvp-btn span {
  font-size: 16px;
  font-weight: 600;
}

.rsvp-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.rsvp-btn.yes {
  color: #059669;
}

.rsvp-btn.yes i {
  color: #10b981;
}

.rsvp-btn.yes:hover {
  background: #ecfdf5;
  border-color: #10b981;
}

.rsvp-btn.maybe {
  color: #d97706;
}

.rsvp-btn.maybe i {
  color: #f59e0b;
}

.rsvp-btn.maybe:hover {
  background: #fffbeb;
  border-color: #f59e0b;
}

.rsvp-btn.no {
  color: #dc2626;
}

.rsvp-btn.no i {
  color: #ef4444;
}

.rsvp-btn.no:hover {
  background: #fef2f2;
  border-color: #ef4444;
}

/* Response Screens */
.response-screen {
  display: none;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 60px 40px;
  text-align: center;
}

.response-screen.show {
  display: block;
}

.response-icon {
  width: 100px;
  height: 100px;
  margin: 0 auto 24px;
  background: #f9fafb;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.response-icon i {
  font-size: 50px;
}

.response-screen.declined .response-icon {
  background: #fef2f2;
}

.response-screen.declined .response-icon i {
  color: #ef4444;
}

.response-screen.tentative .response-icon {
  background: #fffbeb;
}

.response-screen.tentative .response-icon i {
  color: #f59e0b;
}

.response-screen h2 {
  font-size: 28px;
  font-weight: 700;
  color: #111827;
  margin-bottom: 16px;
}

.response-screen p {
  font-size: 16px;
  color: #6b7280;
  line-height: 1.8;
  margin-bottom: 24px;
}

.action-btns {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 300px;
  margin: 0 auto;
}

.action-btn {
  padding: 14px 24px;
  border: none;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.action-btn.primary {
  background: #111827;
  color: white;
}

.action-btn.primary:hover {
  background: #1f2937;
  transform: translateY(-1px);
}

.action-btn.secondary {
  background: white;
  color: #111827;
  border: 2px solid #e5e7eb;
}

.action-btn.secondary:hover {
  background: #f9fafb;
}

@media (max-width: 768px) {
  .name-fields {
    grid-template-columns: 1fr;
  }

  .rsvp-buttons {
    grid-template-columns: 1fr;
  }

}
</style>

<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script type="text/javascript">
  (function(){
    emailjs.init("M_6AgBlV0CHoFIjLP");
  })();
</script>

<div class="invitation-page">


<div class="invitation-page">

  <!-- Invitation Header -->
<div style="text-align: center; margin-bottom: 40px; padding-top: 30px;">
  <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 20px;">
    <i class="far fa-calendar-check" style="font-size: 30px; color: white;"></i>
  </div>
  <h1 style="font-size: 32px; font-weight: 700; color: #111827; margin: 0 0 8px 0;">Meeting Invitation</h1>
  <p style="font-size: 16px; color: #6b7280; margin: 0;">You've been invited by Faranak Rajabi</p>
</div>

  <!-- RSVP Screen -->
  <div id="rsvpScreen">
    
    <!-- Meeting Details -->
    <div class="meeting-details">
      <div class="detail-row">
        <div class="detail-icon calendar">
          <i class="far fa-calendar"></i>
        </div>
        <div class="detail-content">
          <h3>When</h3>
          <p id="inviteWhen">Loading...</p>
        </div>
      </div>

      <div class="detail-row">
        <div class="detail-icon clock">
          <i class="far fa-clock"></i>
        </div>
        <div class="detail-content">
          <h3>Duration</h3>
          <p id="inviteDuration">30 minutes</p>
        </div>
      </div>

      <div class="detail-row">
        <div class="detail-icon topic">
          <i class="fas fa-comments"></i>
        </div>
        <div class="detail-content">
          <h3>Topic</h3>
          <p id="inviteTopic">Meeting</p>
        </div>
      </div>

      <div class="detail-row">
        <div class="detail-icon location">
          <i class="fas fa-map-marker-alt"></i>
        </div>
        <div class="detail-content">
          <h3>Location</h3>
          <p id="inviteLocation">Zoom</p>
        </div>
      </div>
    </div>

    <!-- RSVP Buttons -->
    <div class="rsvp-section">
      <p class="rsvp-question">Will you attend this meeting?</p>
      <div class="rsvp-buttons">
        <button class="rsvp-btn yes" onclick="respond('yes')">
          <i class="fas fa-check-circle"></i>
          <span>Yes, I'll attend</span>
        </button>
        <button class="rsvp-btn maybe" onclick="respond('maybe')">
          <i class="fas fa-question-circle"></i>
          <span>Maybe</span>
        </button>
        <button class="rsvp-btn no" onclick="respond('no')">
          <i class="fas fa-times-circle"></i>
          <span>Can't attend</span>
        </button>
      </div>
    </div>

  </div>

  <!-- Declined Screen -->
  <div class="response-screen declined" id="noScreen">
    <div class="response-icon">
      <i class="fas fa-times"></i>
    </div>
    <h2>We'll Miss You</h2>
    <p>Thanks for letting me know. If you'd like to reschedule, feel free to reach out anytime at <a href="mailto:faranakrajabi@ucsb.edu">faranakrajabi@ucsb.edu</a></p>
    
    <div class="action-btns">
      <button class="action-btn secondary" onclick="window.location.href='/'">
        Close
      </button>
    </div>
  </div>

  <!-- Tentative Screen -->
  <div class="response-screen tentative" id="maybeScreen">
    <div class="response-icon">
      <i class="fas fa-clock"></i>
    </div>
    <h2>Marked as Tentative</h2>
    <p>No problem! Please confirm when you can. I'll send you a reminder closer to the meeting date.</p>
    
    <div class="action-btns">
      <button class="action-btn primary" onclick="respond('yes')">
        Actually, I'll Attend
      </button>
      <button class="action-btn secondary" onclick="window.location.href='/'">
        Close
      </button>
    </div>
  </div>

</div>

<script>
let inviteData = null;

window.addEventListener('DOMContentLoaded', function() {
  const params = new URLSearchParams(window.location.search);
  const token = params.get('invite');
  
  if (!token) {
    window.location.href = '/';
    return;
  }
  
    inviteData = {
    token: token,
    email: params.get('email'),
    name: params.get('name'),  
    datetime: params.get('datetime'),
    duration: params.get('duration'),
    topic: params.get('topic'),
    location: params.get('location')
    };
  
  if (inviteData.datetime) {
    const dt = new Date(inviteData.datetime);
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
    document.getElementById('inviteWhen').textContent = formatted;
  }
  
  document.getElementById('inviteDuration').textContent = inviteData.duration || '30 minutes';
  document.getElementById('inviteTopic').textContent = inviteData.topic || 'Meeting';
  document.getElementById('inviteLocation').textContent = inviteData.location || 'TBD';
});

function respond(answer) {
  const fullName = inviteData.name || '';
  const nameParts = fullName.split(' ');
  const firstName = nameParts[0] || '';
  const lastName = nameParts.slice(1).join(' ') || '';
  
  document.getElementById('rsvpScreen').style.display = 'none';
  
  if (answer === 'yes') {
    // Format datetime for email
    const dt = new Date(inviteData.datetime);
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
    
    // Generate Google Calendar link
    const start = new Date(inviteData.datetime);
    const mins = parseInt(inviteData.duration) || 30;
    const end = new Date(start.getTime() + mins * 60000);
    const fmt = (d) => d.toISOString().replace(/-|:|\.\d+/g, '');
    const calendarLink = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent(inviteData.topic)}&dates=${fmt(start)}/${fmt(end)}&details=Meeting%20with%20Faranak%20Rajabi&location=${encodeURIComponent(inviteData.location)}`;
    
    // Send confirmation email to guest
    const guestEmailParams = {
      first_name: firstName,
      guest_email: inviteData.email,
      topic: inviteData.topic,
      meeting_datetime: formattedDateTime,
      duration: inviteData.duration,
      location: inviteData.location,
      zoom_link: inviteData.location,
      calendar_link: calendarLink
    };
    
    emailjs.send('service_3lm4w34', 'template_yhm6ssq', guestEmailParams)
      .then(function(response) {
        console.log('Confirmation email sent to guest!', response);
      }, function(error) {
        console.error('Failed to send confirmation email:', error);
      });

    emailjs.send('service_3lm4w34', 'template_yhm6ssq', guestEmailParams)
  .then(function(response) {
    console.log('Confirmation email sent to guest!', response);
  }, function(error) {
    console.error('Failed to send confirmation email:', error);
  });

    // ADD NTFY NOTIFICATION HERE ⬇️
    fetch('https://ntfy.sh/faranak-meetings', {
    method: 'POST',
    body: `✅ ${firstName} ${lastName} accepted your meeting!
    📅 ${inviteData.topic}
    🕐 ${formattedDateTime}
    📧 ${inviteData.email}`
    }).catch(error => console.error('Notification failed:', error));

    // Redirect to confirmation page
    const params = new URLSearchParams({  
    
    // Redirect to confirmation page
    const params = new URLSearchParams({
      firstName: firstName,
      lastName: lastName,
      email: inviteData.email,
      datetime: inviteData.datetime,
      duration: inviteData.duration,
      topic: inviteData.topic,
      zoom: inviteData.location,
      token: inviteData.token
    });
    
    window.location.href = `/schedule/confirmed/?${params.toString()}`;
  } else if (answer === 'no') {
    document.getElementById('noScreen').classList.add('show');
  } else {
    document.getElementById('maybeScreen').classList.add('show');
  }
}

</script>