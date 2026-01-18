# 🌦️ Django Weather Application

A fully functional **Django-based Weather Application** that allows users to search for any city and view **real-time weather information** using **WeatherAPI**.  
The project follows **clean architecture**, **secure API key handling**, and **robust exception handling**.

---

## 📌 Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Tech Stack](#tech-stack)
4. [System Architecture](#system-architecture)
5. [Project Structure](#project-structure)
6. [API Integration](#api-integration)
7. [Environment Variables (.env)](#environment-variables-env)
8. [Installation & Setup](#installation--setup)
9. [Exception Handling](#exception-handling)
10. [Frontend UI](#frontend-ui)
11. [Security Best Practices](#security-best-practices)
12. [Testing Scenarios](#testing-scenarios)
13. [Future Enhancements](#future-enhancements)
14. [Contributing](#contributing)
15. [License](#license)
16. [Author](#author)

---

## 🌍 Project Overview

This is a **server-side rendered Django web application** that fetches real-time weather data based on a user-entered city name.

### Users can view:
- 🌡️ Current temperature
- 🌥️ Weather condition
- 💧 Humidity level
- 🌬️ Wind speed
- 🖼️ Weather icon

The application is designed with:
- Clean UI
- Secure API handling
- Graceful failure recovery

---

## ✨ Key Features

- 🔎 Search weather by city name
- 🌡️ Temperature in Celsius
- 🌥️ Condition with icon
- 💧 Humidity percentage
- 🌬️ Wind speed (km/h)
- 🎨 Bootstrap-based UI
- 🔐 Secure API key handling via `.env`
- ⚠️ Robust exception handling
- 📱 Fully responsive design

---

## 🛠️ Tech Stack

### Backend
- Python 3.10+
- Django 4+
- Requests

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### API
- WeatherAPI (`current.json` endpoint)

### Utilities
- python-dotenv

---

## 🧠 System Architecture
```text
User Browser
   ↓
HTML Form (POST)
   ↓
Django View
   ↓
WeatherAPI (External API)
   ↓
JSON Response
   ↓
Django Template Rendering
   ↓
User Interface
```

---

## 📂 Project Structure
```text
weather_project/
│
├── manage.py
├── .env
├── .gitignore
│
├── weather_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── weather_app/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── index.html
│
└── README.md
```
---

## 🌐 API Integration

### API Used
**WeatherAPI – Current Weather Endpoint**
`http://api.weatherapi.com/v1/current.json`


### Request Parameters

| Parameter | Description |
|-----------|-------------|
| key | API key |
| q | City name |
| aqi | Air quality (yes/no) |

### Example Request
```text
?key=API_KEY&q=London&aqi=no
```

---

## 🔐 Environment Variables (.env)

### Why use `.env`?
- Prevents API key exposure
- Keeps secrets out of GitHub
- Follows industry standards

### `.env` file (Project Root)
```env
WEATHER_API_KEY=your_api_key_here
```


### Load `.env` in `settings.py`
```python
from dotenv import load_dotenv
load_dotenv()
```

## 📦 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/django-weather-app.git
cd django-weather-app
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```
Activate:

**Windows:**
```bash
venv\Scripts\activate
```
**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install django requests python-dotenv
```
### 4️⃣ Apply Migrations
```bash
python manage.py migrate
```
### 5️⃣ Run Development Server
```bash
python manage.py runserver
```
- Open in browser:
    `http://127.0.0.1:8000/`


## ⚠️ Exception Handling

| Scenario | Handling |
|--------|---------|
| Invalid city | API error message |
| No internet | Connection error handled |
| API timeout | Timeout exception |
| Invalid API key | HTTP 401 handling |
| Server error | Graceful fallback |
| Invalid JSON | KeyError handling |

All errors are displayed as user-friendly Bootstrap alerts.

## 🎨 Frontend UI
- Gradient background
- Card-based weather display
- Bootstrap alerts
- Responsive for mobile & desktop


## 🔒 Security Best Practices
- API key stored in `.env`
- `.env` added to `.gitignore`
- No hard-coded secrets
- CSRF protection enabled
- Input validation handled


## 🧪 Testing Scenarios
| Test Case | Result |
|---------|--------|
| Valid city | Weather displayed |
| Invalid city | Error message |
| API down | Graceful failure |
| Internet off | No crash |
| First load | Clean UI |



## 🚀 Future Enhancements
- 7-day weather forecast
- Dark mode
- AJAX-based search
- Auto-detect user location
- Docker deployment
- Weather analytics dashboard



## 🤝 Contributing
- Fork repository
- Create feature branch
- Commit changes
- Open pull request

## 📜 License
This project is licensed under the MIT License.

## 👨‍💻 Author
**Shreyas K G**
Python | Django | Web Development

⭐ If you find this project helpful, please give it a star!