---
permalink: /resume/
title: "Resume"
layout: single
author_profile: true
---

<style>
.intro-section {
  margin: 2em 0;
  padding: 2em;
  background: #f8f9fa;
  border-radius: 8px;
  text-align: center;
}

.intro-section p {
  font-size: 1.2em;
  margin-bottom: 1.5em;
}

.download-buttons {
  display: flex;
  gap: 1em;
  justify-content: center;
  margin: 2em 0;
  flex-wrap: wrap;
}

.download-btn {
  padding: 1em 2em;
  background: #001f3f;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1.1em;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-block;
}

.download-btn:hover {
  background: #003366;
  transform: translateY(-2px);
  color: white;
}

.progress-container {
  display: none;
  margin: 2em 0;
}

.progress-bar {
  width: 100%;
  height: 30px;
  background: #e0e0e0;
  border-radius: 15px;
  overflow: hidden;
  margin-bottom: 1em;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #001f3f, #4a90e2);
  width: 0%;
  transition: width 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
}

.cat-section {
  display: none;
  text-align: center;
  margin: 2em 0;
}

.cat-section h3 {
  color: #001f3f;
  margin-bottom: 1em;
  font-size: 1.5em;
}

.cat-image {
  max-width: 500px;
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  margin: 1em 0;
  transition: opacity 0.5s ease;
}

.cat-caption {
  font-style: italic;
  color: #666;
  margin-top: 0.5em;
  font-size: 1.1em;
}
</style>

<div class="intro-section">
  <p>Find my complete Resume and CV below, and contact me at <strong>faranakrajabi@ucsb.edu</strong>! 😊</p>
  
  <div class="download-buttons">
    <button class="download-btn" onclick="downloadFile('resume')">
      📋 Download Resume
    </button>
    <button class="download-btn" onclick="downloadFile('cv')">
      📑 Download Full CV
    </button>
  </div>

  <p style="margin-top: 2em;">And enjoy some photos of my cutie pie while the files load!</p>

  <div class="progress-container" id="progressContainer">
    <div class="progress-bar">
      <div class="progress-fill" id="progressFill">0%</div>
    </div>
    <p id="statusText" style="text-align: center; color: #001f3f; font-weight: bold;"></p>
  </div>

  <div class="cat-section" id="catSection">
    <h3>Meet Ponyo! 🐱</h3>
    <img src="/assets/images/ponyo1.jpg" alt="Ponyo the cat" class="cat-image" id="catImage">
    <p class="cat-caption" id="catCaption">Ponyo says: "Thanks for waiting!"</p>
  </div>
</div>

<script>
// All 13 Ponyo images with captions
const allPonyoImages = [
  { src: '/assets/images/ponyo1.jpg', caption: 'Ponyo says: "Thanks for waiting!"' },
  { src: '/assets/images/ponyo2.jpg', caption: 'Ponyo wondering why you need a resume...' },
  { src: '/assets/images/ponyo3.jpg', caption: 'Ponyo thinks you should hire me!' },
  { src: '/assets/images/ponyo4.jpg', caption: 'Ponyo approves of this download 💖' },
  { src: '/assets/images/ponyo5.jpg', caption: 'Ponyo is supervising this process 👀' },
  { src: '/assets/images/ponyo6.jpg', caption: 'Ponyo says: "Almost done!"' },
  { src: '/assets/images/ponyo7.jpg', caption: 'Ponyo relaxing while you wait 😺' },
  { src: '/assets/images/ponyo8.jpg', caption: 'Ponyo believes in your career! 🌟' },
  { src: '/assets/images/ponyo9.jpg', caption: 'Ponyo is being adorable (as usual)' },
  { src: '/assets/images/ponyo10.jpg', caption: 'Ponyo approves of your life choices 👍' },
  { src: '/assets/images/ponyo11.jpg', caption: 'Ponyo says: "Good things take time!"' },
  { src: '/assets/images/ponyo12.jpg', caption: 'Ponyo wondering what\'s taking so long...' },
  { src: '/assets/images/ponyo13.jpg', caption: 'Ponyo hopes you enjoyed the slideshow! 🎉' }
];

// Randomly select 4-5 images for this download session
let catImages = [];
let currentCatIndex = 0;

function selectRandomImages() {
  const numImages = Math.floor(Math.random() * 2) + 4; // 4 or 5 images
  const shuffled = [...allPonyoImages].sort(() => 0.5 - Math.random());
  catImages = shuffled.slice(0, numImages);
  currentCatIndex = 0;
}

function downloadFile(type) {
  const progressContainer = document.getElementById('progressContainer');
  const catSection = document.getElementById('catSection');
  const progressFill = document.getElementById('progressFill');
  const statusText = document.getElementById('statusText');
  
  // Select random images for this download
  selectRandomImages();
  
  // Show progress bar and cat section
  progressContainer.style.display = 'block';
  catSection.style.display = 'block';
  
  // Set first random image
  document.getElementById('catImage').src = catImages[0].src;
  document.getElementById('catCaption').textContent = catImages[0].caption;
  
  // Reset progress
  let progress = 0;
  progressFill.style.width = '0%';
  progressFill.textContent = '0%';
  
  // File URLs
  const fileUrls = {
    'resume': '/assets/files/FaranakRajabiResume.pdf',
    'cv': '/assets/files/FaranakRajabiCV.pdf'
  };
  
  statusText.textContent = type === 'resume' ? 'Preparing your resume...' : 'Preparing your CV...';
  
  const progressPerImage = 100 / catImages.length;
  
  // Simulate download progress - SLOWER VERSION
  const interval = setInterval(() => {
    progress += Math.random() * 5; // Changed from 12 to 5 - MUCH SLOWER
    if (progress > 100) progress = 100;
    
    progressFill.style.width = progress + '%';
    progressFill.textContent = Math.floor(progress) + '%';
    
    // Change cat image at intervals
    const targetIndex = Math.floor(progress / progressPerImage);
    if (targetIndex > currentCatIndex && targetIndex < catImages.length) {
      currentCatIndex = targetIndex;
      changeCatImage();
    }
    
    // Update status messages
    if (progress < 30) {
      statusText.textContent = 'Compiling all my achievements...';
    } else if (progress < 60) {
      statusText.textContent = 'Adding computational wizardry...';
    } else if (progress < 90) {
      statusText.textContent = 'Almost there!';
    } else if (progress >= 100) {
      statusText.textContent = '✅ Download complete!';
      clearInterval(interval);
      
      // Actually trigger the download
      const link = document.createElement('a');
      link.href = fileUrls[type];
      link.download = type === 'resume' ? 'FaranakRajabiResume.pdf' : 'FaranakRajabiCV.pdf';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      
      // Reset after 3 seconds - LONGER DELAY
      setTimeout(() => {
        progressContainer.style.display = 'none';
        catSection.style.display = 'none';
        currentCatIndex = 0;
      }, 3000); // Changed from 2000 to 3000
    }
  }, 300); // Changed from 200 to 300 - SLOWER UPDATES
}

function changeCatImage() {
  if (currentCatIndex < catImages.length) {
    const img = document.getElementById('catImage');
    // Fade out
    img.style.opacity = '0';
    
    // Change image after fade
    setTimeout(() => {
      img.src = catImages[currentCatIndex].src;
      document.getElementById('catCaption').textContent = catImages[currentCatIndex].caption;
      // Fade in
      img.style.opacity = '1';
    }, 250);
  }
}
</script>
