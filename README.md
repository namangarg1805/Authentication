# FastAPI + Keycloak OAuth2 / OIDC Authentication Project

## 📌 Overview
This project demonstrates how to integrate **FastAPI** with **Keycloak** using **OAuth 2.0** and **OpenID Connect (OIDC)** for secure user authentication and authorization.

Users are redirected to Keycloak for login, and after successful authentication, the application receives an authorization code, exchanges it for tokens, and grants access to protected APIs.

---

## 🚀 Features

* FastAPI backend application
* Keycloak integration for authentication
* OAuth 2.0 Authorization Code Flow
* OIDC support for user identity
* JWT token handling
* Protected API routes
* Secure login/logout flow

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Keycloak**
* **OAuth 2.0**
* **OIDC**
* **JWT**
* **Uvicorn**
* **Requests / HTTPX**

---

## 📂 Project Structure

```text
AUTHENTICATION_PROJECT/
├── .venv/
├── requirements.txt
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── auth.py
│   ├── dependencies.py
│   │
│   └── routes/
│       ├── auth_routes.py
│       └── protected_routes.py
│
└── frontend/
    └── index.html
```



## 🔄 Authentication Flow

1. User clicks **Login**
2. FastAPI redirects user to Keycloak login page
3. User enters credentials in Keycloak
4. Keycloak sends **authorization code** to callback URL
5. FastAPI exchanges code for tokens
6. Access token used for protected routes
7. ID token contains user identity details

---

## ▶️ Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
## ⚙️ Configure Keycloak

Update these values in your code:

```python
KEYCLOAK_URL=
REALM=
CLIENT_ID=
CLIENT_SECRET=
REDIRECT_URI=
```
### 4. Start Keycloak
docker run -d --name keycloak `
-p 8080:8080 `
-e KEYCLOAK_ADMIN=admin `
-e KEYCLOAK_ADMIN_PASSWORD=admin `
quay.io/keycloak/keycloak:latest start-dev

### 5. Start FastAPI Server

```bash
uvicorn backend.main:app --reload
```
---

## 🔐 Sample Endpoints

| Endpoint    | Description                |
| ----------- | -------------------------- |
| `/login`    | Redirect to Keycloak login |
| `/callback` | Receives auth code         |
| `/profile`  | Protected user profile     |
| `/logout`   | Logout user                |


* Protected API routes
* Secure login/logout flow

---
## ⭐ If you found this useful, give it a star!
