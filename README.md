```markdown
# Todo App 📝

A simple and scalable **To-Do List** application built with [Flet](https://flet.dev/), now with **PostgreSQL support**, **Dockerization**, and **automatic HTTPS via Traefik & Let's Encrypt**.

## ✨ Features
- Add, update, and delete tasks
- Track task progress with statuses: "To-Do", "In Progress", "Done"
- Filter tasks by status
- Supports both in-memory and PostgreSQL storage
- Dockerized with Traefik reverse proxy
- Automatic SSL certificates via DNS challenge (e.g., Cloudflare)

---

## 🧰 Setup Options

### Option 1: Local Python Development

#### ✅ Prerequisites
- Python 3
- `make`
- Virtual environment (recommended)

#### 📦 Installation
```sh
git clone https://github.com/your-username/todo-app.git
cd todo-app
make venv       # Creates virtual environment
make install    # Installs required packages
```

#### 🚀 Run the App
```sh
make flet-run
```

#### 🌐 Run on Web (custom port optional)
```sh
make flet-web PORT=8000
```

#### 📱 Android / iOS
```sh
make flet-android PORT=3423
make flet-ios PORT=5000
```

> For mobile setup guides:  
[Android Setup](https://flet.dev/docs/getting-started/testing-on-android) | [iOS Setup](https://flet.dev/docs/getting-started/testing-on-ios)

---

### Option 2: Run with Docker, PostgreSQL & Traefik (Recommended for Production) 🐳🔒

#### 🌍 Requirements
- Docker & Docker Compose
- Valid domain (e.g., `todo.example.com`)
- DNS provider API token (e.g., Cloudflare)

#### ⚙️ Steps
1. **Configure environment variables**  
   Copy `.env.example` to `.env` and set your values:
   ```env
   STORAGE_TYPE=database
   DB_DIALECT=postgresql
   DB_USER=todo_user
   DB_PASSWORD=todo_pass
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=todo_db

   CF_DNS_API_TOKEN=your_cloudflare_token
   ACME_EMAIL=your_email@example.com
   DOMAIN=your-domain.com
   ```

2. **Start services**
   ```sh
   sudo docker-compose up -d
   ```

3. **Visit your app**
   ```
   https://todo.your-domain.com
   ```

> DNS Challenge is used for SSL with Let's Encrypt.  
Make sure your DNS provider supports API access (e.g., Cloudflare).

---

## 🔐 SSL Certificates

- Managed automatically by Traefik using DNS challenge
- Stored in the `letsencrypt/` folder (auto-created)
- Do **not** commit this folder to version control:
  ```gitignore
  letsencrypt/
  ```