<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Социальные сети</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #212121;
      color: #eee;
      margin: 0;
      padding: 0;
    }
    #header {
      text-align: center;
      padding: 20px;
      background-color: #19191a;
    }
    #header img {
      border-radius: 50%;
      border: 4px solid #444;
    }
    #badges {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 10px;
      padding: 20px;
      background-color: #34383d;
      border-radius: 10px;
      margin: 20px;
    }
    #badges a {
      text-decoration: none;
    }
    #badges img {
      width: 100px;
      height: 40px;
    }
    #trophies {
      text-align: center;
      margin: 20px;
    }
    #content {
      padding: 20px;
    }
    .section {
      margin: 20px 0;
    }
    .section h1, .section h2, .section h3 {
      color: #fff;
      text-align: center;
    }
    .section p {
      font-size: 18px;
      text-indent: 40px;
    }
    .tech-stack, .database-stack, .tools-stack {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
    }
    .tech-stack img, .database-stack img, .tools-stack img {
      width: auto;
      height: 40px;
      margin: 5px;
    }
    .tech-stack img.sql {
      height: 28px;
    }
  </style>
</head>
<body>
  <div id="header">
    <img src="https://avatars.githubusercontent.com/u/95464313?v=4" width="150" alt="Profile Image"/>
    <h1>Добро пожаловать в мой профиль GitHub!</h1>
  </div>
  <div id="content">
    <div class="section" align="center">
      <h1>Обо мне</h1>
      <hr>
      <p>Я закончил университет МУБИНТ в 2024 году. Мне нравится писать код на Python, хотя моим первым языком программирования был C. Я увлекаюсь созданием сайтов, разработкой десктопных приложений и многим другим.</p>
      <p>Самым большим моим проектом является десктопное приложение для управления операционной системой Windows, написанное на Python. Это приложение настраивает и оптимизирует систему, делая её работу более эффективной и удобной для пользователя. В свободное время я продолжаю изучать новые языки программирования и технологии. Мне интересно следить за последними тенденциями в области IT и я постоянно совершенствую свои навыки, участвуя в различных проектах и открытых сообществах разработчиков.</p>
      <p>Моя цель – продолжать развиваться в сфере разработки программного обеспечения и вносить значительный вклад в интересные и полезные проекты. Я верю, что постоянное обучение и практика – ключ к успеху в этой динамичной и быстро развивающейся области.</p>
    </div>
    <div class="section">
      <h1>Мой стек технологий</h1>
      <h3>Языки программирования</h3>
      <div class="tech-stack">
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
        <img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=white" alt="C"/>
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
        <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
        <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM91T1S4z84bTfnQg-ExIMn9MW_bs43wkg5g&s" class="sql" alt="SQL"> 
      </div>
      <h3>Фреймворки и библиотеки</h3>
      <div class="tech-stack">
        <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
        <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
        <img src="https://img.shields.io/badge/PyQt6-41cd52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt6"/>
        <img src="https://img.shields.io/badge/Telegram_Bot_API-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot API"/>
      </div>
      <h3>Базы данных</h3>
      <div class="database-stack">
        <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
        <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
        <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
        <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
        <img src="https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white" alt="Oracle"/>
      </div>
      <h3>Инструменты и технологии</h3>
      <div class="tools-stack">
        <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
        <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
        <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
        <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code"/>
        <img src="https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white" alt="PyCharm"/>
        <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/>
      </div>
    </div>
    <div id="badges">
      <a href="https://t.me/zoomkaXXX">
        <img src="https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Badge"/>
      </a>
      <a href="https://vk.com/zoomkaxxx">
        <img src="https://img.shields.io/badge/VK-blue?style=for-the-badge&logo=vk&logoColor=white" alt="VK Badge"/>
      </a>
      <a href="mailto:rrarrk123@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-red?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail Badge"/>
      </a>
      <a href="https://www.facebook.com/rrarrkfacit/">
        <img src="https://img.shields.io/badge/Facebook-blue?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook Badge"/>
      </a>
      <a href="https://discord.com/users/zoomkaxxx">
        <img src="https://img.shields.io/badge/Discord-blue?style=for-the-badge&logo=discord&logoColor=white" alt="Discord Badge"/>
      </a>
    </div>
    <div id="trophies">
      <h2>🏆 Мои награды</h2>
      <a href="https://github.com/ryo-ma/github-profile-trophy">
        <img src="https://github-profile-trophy.vercel.app/?username=zoomprog&row=1&column=3" alt="GitHub Trophies"/>
      </a>
    </div>
  </div>
  <div style="text-align: center;">
    <img src="status.svg" alt="Status">
  </div>
</body>
</html>
