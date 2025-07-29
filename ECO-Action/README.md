# 🌱 EcoTracker: Sustainable Habit Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Framework: FastAPI](https://img.shields.io/badge/Framework-FastAPI-%2300C7B7)](https://fastapi.tiangolo.com/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flet: 0.28.3+](https://img.shields.io/badge/Flet-0.28.3%2B-9cf)](https://flet.dev/)

An application that encourages sustainable habits through community engagement and gamification. Tracks eco-friendly actions, rewards users with points, and fosters environmental awareness.

---

## 🚀 Key Features

### 🌟 Core Functionality
| Feature Category       | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **User System**        | Secure authentication with bcrypt hashing                                   |
| **Eco-Action Tracking**| Log 20+ sustainable activities with point rewards                           |
| **Community**          | Real-time leaderboard to track progress against others                      |
| **Admin Tools**        | Manage users, reset leaderboards, and send congratulatory messages          |
| **Responsive UI**      | Cross-platform desktop interface built with Flet                            |

### 🎨 Frontend
- **Interactive UI**: Built with Flet (cross-platform compatibility)
- **Responsive Design**: Adapts to different screen sizes
- **Action History**: Visual timeline of user activities

### ⚙️ Backend
- **RESTful API**: FastAPI-powered endpoints
- **SQLite Database**: Lightweight and efficient data storage
- **JWT Authentication**: Secure API access (future implementation)

---

## 🛠️ Setup Guide :exclamation: :exclamation:

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

```
pip install fastapi uvicorn
pip install passlib bcrypt python-multipart
pip install sqlite3  
pip install flet
pip install httpx pytest pytest-cov
pip install fastapi uvicorn passlib bcrypt python-multipart flet
```

### 🖥️ Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Richmunddd/ECO-Action-Tracker.git


# :satellite: To Run the API server: 


Run in the terminal:

```
cd ~/directory/path/of/the/file/presentation_layer/ python main.py
```

## [To access the HTTP API](http://127.0.0.1:8000/docs)



# :satellite: To Run the Frontend User Interface:


```
cd ~/directory/path/of/the/file/presentation_layer python app.py
```


## Authors
- Richmond Keith P. Mantaring
- Kate Wilsen See

