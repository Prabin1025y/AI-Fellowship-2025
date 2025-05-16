
# 🧠 AI Fellowship 2025 – FastAPI + Docker + PostgreSQL App

A clean, 12-Factor-compliant backend API built with **FastAPI**, **Docker**, and **PostgreSQL**. Designed as part of a hands-on learning journey through production-ready backend architecture, app development, and cloud-friendly design.

---

## 🚀 Features

- ✅ RESTful API using **FastAPI**
- ✅ Persistent storage using **PostgreSQL** in Docker
- ✅ Clean structure following **12-Factor App principles**
- ✅ Configurable using environment variables via `.env`
- ✅ Includes CRUD endpoints for managing notes

---

## 🏗️ Project Structure

```
📦 Assignment1/
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── wait-for-it.sh
├── requirements.txt
├── .env                # <- Add this manually (see below)
├── main.py             # FastAPI app
├── database.py         # DB connection logic
└── model.py            # Table model using SQLAlchemy
.gitignore
```

---

## 🛠 Setup Instructions

### 1. 🔧 Prerequisites

- Python 3.11+
- Docker + Docker Compose
- Git

### 2. 🗝️ Configure Environment Variables

Create a `.env` file 

Edit the `.env`:

```
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=db_name
DATABASE_URL=postgresql://username:password@db:5432/db_name
```

Make sure `.env` is **added to `.gitignore`**.

---

### 3. 🐳 Run the App

```bash
docker-compose up --build
```

- API will be live at: [http://localhost:8000](http://localhost:8000)
- Swagger UI docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 API Endpoints

### ✅ Create Note

```http
POST /notes/
{
  "title": "My Note",
  "content": "Some content"
}
```

### 📥 Read Notes

```http
GET /notes/
```

### ❌ Delete Note

```http
DELETE /notes/{note_id}
```

---

## 🧪 Testing Locally (without Docker)

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🧠 12-Factor Principles Covered

| Principle                 | Status  | Description |
|--------------------------|---------|-------------|
| I. Codebase              | ✅      | Single Git repo |
| II. Dependencies         | ✅      | Managed via `requirements.txt` |
| III. Config              | ✅      | `.env` for secrets and URLs |
| IV. Backing Services     | ✅      | PostgreSQL in Docker |
| V. Build, Release, Run   | ✅      | Handled via Docker Compose |
| VI. Processes            | ✅      | Stateless web service |
| VII. Port Binding        | ✅      | FastAPI binds to `:8000` |
| VIII. Concurrency        | ✅      | Supports multi-worker scaling |
| IX. Disposability        | ✅      | Graceful startup/shutdown with lifespan events |
| X. Dev/Prod Parity       | ✅      | Docker environment matches prod |
| XI. Logs                 | ✅      | Logs to stdout, captured by Docker |

---

## 🧑‍💻 Author

**Prabin Acharya**  
2025 AI Fellowship Project  
[GitHub Profile](https://github.com/Prabin1025y)

---

## 📄 License

MIT – free to use, modify, and contribute.
