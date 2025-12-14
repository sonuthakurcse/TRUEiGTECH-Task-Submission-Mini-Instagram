
---

# Instagram Mini Clone (Flask Web App)

## Project Overview

This project is a **mini Instagram-like web application** built using **Flask and SQLAlchemy**.
It allows users to **sign up, log in, create posts with images, like and comment on posts, follow other users, and view a personalized feed**.

The goal of this project is to demonstrate **full-stack development concepts**, database relationships, authentication, and REST-style API design.

---

## Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, Jinja Templates
* **Database:** SQLite (via SQLAlchemy ORM)
* **Authentication:** Flask-Login
* **File Uploads:** Werkzeug
* **Tools:** PyCharm, Git, Postman

---

## Features Implemented

* User Signup & Login
* Secure Password Hashing
* Create Post with Image Upload
* Like / Unlike Posts
* Comment on Posts
* Follow / Unfollow Users
* Personalized Feed
* Profile Page with User Posts
* Session-based Authentication

---

## Project Structure

```
instagram-mini-clone/
│
├── app/
│   ├── models/
│   │   ├── user.py
│   │   ├── post.py
│   │   └── comment.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── page_routes.py
│   │   ├── post_routes.py
│   │   └── user_routes.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── feed.html
│   │   ├── create_post.html
│   │   └── profile.html
│   │
│   ├── static/
│   │   └── uploads/
        └── style.css
│   │
│   ├── extensions.py
│   ├── config.py
│   └── __init__.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

## Databasea Design

### Usera Table

* `id` (Primary Key)
* `name`
* `email` (Unique)
* `password`
* `followers` (Many-to-Many)
* `following` (Many-to-Many)

### Post Table

* `id`
* `image_url`
* `caption`
* `created_at`
* `user_id` (Foreign Key)

### Comments Table

* `id`
* `text`
* `created_at`
* `user_id` (Foreign Key)
* `post_id` (Foreign Key)

---

## API Endpoint(Postman Ready)

### Authentication

```
POST   /signup        → Register new user
POST   /login         → Login user
GET    /logout        → Logout user
```

### Posts

```
POST   /post/create               → Create new post
GET    /post/like/<post_id>       → Like / Unlike post
POST   /post/comment/<post_id>    → Comment on post
```

### Users

```
GET    /follow/<user_id>           → Follow user
```

### Pages

```
GET    /feed       → View feed
GET    /profile    → View profile
GET    /create     → Create post page
```

---

## How to Run the Project

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python run.py
```

### 5️⃣ Open Browser

```
http://127.0.0.1:5000
```

---

## Postman API Documentation

* All API endpoints can be tested using **Postman**
* Requests include:

  * User authentication
  * Post creation
  * Like / comment actions
  * Follow users
* Recommended to export Postman collection and include it in Git repository

---

## 🎯 Learning Outcomes

* Flask Blueprint Architecture
* SQLAlchemy Relationships
* Session-Based Authentication
* REST API Design
* File Upload Handling
* Full-Stack Web Development

---

## My Details

**Sonu Thakur**
B.Tech Computer Science AIML (2026)
Flask | Python | SQL | Selenium

Email:sonuthakur009912@gmail.com  
LinkedIn:https://www.linkedin.com/in/sonuthakurcse  
---

