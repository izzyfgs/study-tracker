# study-tracker

<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>ExamEcho</title>

<style>
  html, body {
    margin: 0; padding: 0; height: 100%;
    overflow: hidden;
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #f9fafb;
  }

  .app { 
    height: 100vh; 
    display: flex; 
    background: #f9fafb; 
  }

  .sidebar {
    width: 340px;
    padding: 24px 18px;
    box-sizing: border-box;
    background: linear-gradient(180deg, #ffffff, #f8f8f8);
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 28px;
  }

  /* Logo */
  .logo {
    display: flex;
    align-items: center;
    gap: 16px;
    font-size: 28px;
    font-weight: 900;
    color: #111;
  }
  .logo img {
    width: 48px;
    height: 48px;
    border-radius: 8px;
    object-fit: contain;
  }

  /* Profile Card */
  .profile-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 22px;
    border-radius: 18px;
    background: #ffffff;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    position: relative;
  }

  .profile-left {
    display: flex;
    align-items: center;
    gap: 18px;
    flex: 1;
  }

  .avatar {
    width: 72px;
    height: 72px;
    border-radius: 50%;
    background: #8b5cf6; /* Purple to match theme */
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    overflow: hidden;
    flex-shrink: 0;
  }
  .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .avatar .plus {
    font-size: 42px;
    color: white;
    font-weight: 300;
  }

  .user-info {
    flex: 1;
  }
  .username {
    font-size: 24px;
    font-weight: 800;
    color: #111;
  }
  .average {
    margin-top: 6px;
    font-size: 15px;
    color: #555;
  }

  /* Three-dot menu */
  .menu-dots {
    font-size: 24px;
    cursor: pointer;
    padding: 8px;
    border-radius: 8px;
  }
  .menu-dots:hover {
    background: rgba(0,0,0,0.06);
  }

  .dropdown {
    position: absolute;
    right: 18px;
    top: 90px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    min-width: 140px;
    display: none;
    z-index: 100;
    border: 1px solid #eee;
  }
  .dropdown.show {
    display: block;
  }
  .dropdown a {
    display: block;
    padding: 12px 16px;
    font-size: 14px;
    color: #333;
    text-decoration: none;
  }
  .dropdown a:hover {
    background: #f0f0f0;
  }
  .dropdown a#deleteProfile {
    color: #e74c3c !important;
  }
  .dropdown a#deleteProfile:hover {
    background: #fef0f0;
  }

  /* Sections */
  .section-header {
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-size: 14px;
    color: #444;
    padding: 10px 6px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .section-header .arrow {
    font-size: 14px;
    font-weight: bold;
    color: #666;
  }

  .section-items { display: none; margin-left: 22px; margin-top: 8px; }
  .section.open .section-items { display: block; }

  .menu-item {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 10px 8px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 8px;
    transition: all 0.2s ease;
  }
  .menu-item:hover {
    background: rgba(255, 0, 0, 0.08); /* Red tint hover */
    transform: translateX(4px);
    color: #c00;
  }
  .icon {
    width: 20px;
    height: 20px;
    stroke: #222;
    stroke-width: 2;
    fill: none;
  }

  /* Main Content */
  .content {
    flex: 1;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 48px;
    background: #f9fafb;
  }

  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
    margin-top: 32px;
  }

  .card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  }

  .card-title {
    font-size: 18px;
    font-weight: 700;
    color: #333;
    margin-bottom: 12px;
  }

  .stat-big {
    font-size: 42px;
    font-weight: 900;
    color: #4a6cf7;
  }

  .subject-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .subject-item {
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 1px solid #eee;
  }

  .subject-item:last-child {
    border-bottom: none;
  }

  .recent-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 12px;
  }

  .recent-table th, .recent-table td {
    text-align: left;
    padding: 12px 0;
    border-bottom: 1px solid #eee;
  }

  .btn-primary {
    background: #8b5cf6;
    color: white;
    border: none;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 600;
    border-radius: 12px;
    cursor: pointer;
    margin-top: 20px;
    transition: background 0.3s;
  }

  .btn-primary:hover {
    background: #7c4dff;
  }

  .welcome-title { font-size: 48px; font-weight: 900; margin: 0; color: #111; }
  .welcome-subtitle { margin-top: 16px; font-size: 18px; color: #444; max-width: 720px; line-height: 1.6; }
</style>
</head>

<body>
<div class="app">

  <aside class="sidebar">

    <!-- Logo: Purple Triangle -->
    <div class="logo">
      <img src="https://thumbs.dreamstime.com/b/triangle-shape-purple-color-design-symbol-vector-illustration-triangle-shape-purple-color-design-407523887.jpg" alt="ExamEcho Icon">
      <span>ExamEcho</span>
    </div>

    <!-- Profile Card -->
    <div class="profile-card">
      <div class="profile-left">
        <div class="avatar" id="avatarWrap">
          <img id="profileImg" src="" alt="" style="display:none;">
          <div class="plus" id="plusSign">+</div>
        </div>
        <div class="user-info">
          <div class="username" id="usernameDisplay">Student</div>
          <div class="average" id="averageDisplay">Average: --%</div>
        </div>
      </div>

      <div class="menu-dots" id="menuDots">⋮</div>
      <div class="dropdown" id="profileDropdown">
        <a href="#" id="editProfile">Edit</a>
        <a href="#" id="deleteProfile">Delete</a>
      </div>
    </div>

    <input type="file" id="profileInput" accept="image/*" style="display:none" />

    <!-- Main Menu -->
    <div class="section open" id="mainMenu">
      <div class="section-header">Main Menu <span class="arrow">▾</span></div>
      <div class="section-items">
        <div class="menu-item"> <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="7" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/></svg> Profile </div>
        <div class="menu-item"> <svg class="icon" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg> Messages </div>
        <div class="menu-item"> <svg class="icon" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><line x1="3" y1="10" x2="21" y2="10"/></svg> Dashboard </div>
        <div class="menu-item"> <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 00.3 1.9l.1.1a2 2 0 01-2.8 2.8l-.1-.1a1.7 1.7 0 00-1.9-.3 1.7 1.7 0 00-1 1.5V21a2 2 0 01-4 0v-.1a1.7 1.7 0 00-1-1.5 1.7 1.7 0 00-1.9.3l-.1.1a2 2 0 01-2.8-2.8l.1-.1a1.7 1.7 0 00.3-1.9 1.7 1.7 0 00-1.5-1H3a2 2 0 010-4h.1a1.7 1.7 0 001.5-1 1.7 1.7 0 00-.3-1.9l-.1-.1a2 2 0 012.8-2.8l.1.1a1.7 1.7 0 001.9.3 1.7 1.7 0 001-1.5V3a2 2 0 014 0v.1a1.7 1.7 0 001 1.5 1.7 1.7 0 001.9-.3l.1-.1a2 2 0 012.8 2.8l-.1.1a1.7 1.7 0 00-.3 1.9 1.7 1.7 0 001.5 1H21a2 2 0 010 4h-.1a1.7 1.7 0 00-1.5 1z"/></svg> Settings </div>
      </div>
    </div>

    <!-- Performance Menu -->
    <div class="section" id="performanceMenu">
      <div class="section-header">Performance <span class="arrow">▸</span></div>
      <div class="section-items">
        <div class="menu-item"> <svg class="icon" viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg> Add New </div>
        <div class="menu-item"> <svg class="icon" viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg> View Scores </div>
      </div>
    </div>

  </aside>

  <main class="content">
    <h1 class="welcome-title">Welcome back!</h1>
    <p class="welcome-subtitle">Your journey through past exams continues. Track every score, watch your growth, and master your subjects.</p>

    <div class="dashboard-grid">
      <!-- Total Sessions -->
      <div class="card">
        <div class="card-title">Total Sessions</div>
        <div class="stat-big">127</div>
        <p style="color:#666; margin-top:8px;">+12 this month</p>
      </div>

      <!-- Overall Average -->
      <div class="card">
        <div class="card-title">Overall Average</div>
        <div class="stat-big">82.4%</div>
        <p style="color:#666; margin-top:8px;">↑ 3.2% from last month</p>
      </div>

      <!-- Best Subject -->
      <div class="card">
        <div class="card-title">Best Subject</div>
        <div class="stat-big">Physics</div>
        <p style="color:#666; margin-top:8px;">Average: 89.7%</p>
      </div>

      <!-- Years Covered -->
      <div class="card">
        <div class="card-title">Years Covered</div>
        <div class="stat-big">47</div>
        <p style="color:#666; margin-top:8px;">From 1978 to 2025</p>
      </div>
    </div>

    <div class="dashboard-grid" style="margin-top:48px;">
      <!-- Subject Breakdown -->
      <div class="card" style="grid-column: span 2;">
        <div class="card-title">Subject Performance</div>
        <ul class="subject-list">
          <li class="subject-item"><span>Physics</span> <strong>89.7%</strong></li>
          <li class="subject-item"><span>Chemistry</span> <strong>85.2%</strong></li>
          <li class="subject-item"><span>Mathematics</span> <strong>81.6%</strong></li>
          <li class="subject-item"><span>English</span> <strong>73.9%</strong></li>
        </ul>
      </div>

      <!-- Recent Activity -->
      <div class="card" style="grid-column: span 2;">
        <div class="card-title">Recent Sessions</div>
        <table class="recent-table">
          <tr><th>Subject</th><th>Year</th><th>Score</th><th>Date</th></tr>
          <tr><td>Physics</td><td>2024</td><td>48/50 (96%)</td><td>Jan 1</td></tr>
          <tr><td>Maths</td><td>2018</td><td>42/50 (84%)</td><td>Dec 30</td></tr>
          <tr><td>Chemistry</td><td>2022</td><td>39/40 (97.5%)</td><td>Dec 28</td></tr>
          <tr><td>English</td><td>2015</td><td>85/100 (85%)</td><td>Dec 27</td></tr>
        </table>
        <button class="btn-primary">Add New Session</button>
      </div>
    </div>
  </main>

</div>

<!-- Same script as before for profile & menu toggle -->
<script>
  // Toggle sections
  document.querySelectorAll(".section-header").forEach(header => {
    header.addEventListener("click", () => {
      const section = header.parentElement;
      section.classList.toggle("open");
      const arrow = header.querySelector(".arrow");
      arrow.textContent = section.classList.contains("open") ? "▾" : "▸";
    });
  });

  // Profile picture & dropdown logic (same as previous version)
  const avatarWrap = document.getElementById("avatarWrap");
  const profileImg = document.getElementById("profileImg");
  const plusSign = document.getElementById("plusSign");
  const profileInput = document.getElementById("profileInput");

  const savedAvatar = localStorage.getItem("examecho_avatar");
  if (savedAvatar) {
    profileImg.src = savedAvatar;
    profileImg.style.display = "block";
    plusSign.style.display = "none";
  }

  avatarWrap.addEventListener("click", (e) => {
    e.stopPropagation();
    profileInput.click();
  });

  profileInput.addEventListener("change", () => {
    const file = profileInput.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      profileImg.src = reader.result;
      profileImg.style.display = "block";
      plusSign.style.display = "none";
      localStorage.setItem("examecho_avatar", reader.result);
    };
    reader.readAsDataURL(file);
  });

  const menuDots = document.getElementById("menuDots");
  const dropdown = document.getElementById("profileDropdown");

  menuDots.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdown.classList.toggle("show");
  });

  document.addEventListener("click", () => {
    dropdown.classList.remove("show");
  });

  document.getElementById("editProfile").addEventListener("click", (e) => {
    e.preventDefault();
    profileInput.click();
    dropdown.classList.remove("show");
  });

  document.getElementById("deleteProfile").addEventListener("click", (e) => {
    e.preventDefault();
    profileImg.src = "";
    profileImg.style.display = "none";
    plusSign.style.display = "block";
    localStorage.removeItem("examecho_avatar");
    dropdown.classList.remove("show");
  });
</script>
</body>
</html>
