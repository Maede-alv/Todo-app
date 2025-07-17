Here’s a **beautified, organized, and visually enhanced** version of your README.
I’ve added emojis, better sectioning, and improved readability while keeping all details intact:

---

# **Todo App** 📝

A **simple, scalable, and modern To‑Do List application** built with [Flet](https://flet.dev/).
✅ **PostgreSQL support**
✅ **Dockerized with Traefik**
✅ **Automatic HTTPS via Let’s Encrypt**

---

## 🌟 **Features**

✅ Add, update, and delete tasks
✅ Track progress: **To‑Do**, **In Progress**, **Done**
✅ Filter tasks by status
✅ In‑memory or PostgreSQL storage
✅ 🚀 **Dockerized** with Traefik reverse proxy
✅ 🔒 **Automatic SSL** (DNS challenge with e.g. Cloudflare)
✅ 🤖 **CI/CD** with GitHub Actions (tests, linting, semantic releases)

---

## 🧰 **Setup Options**

### 🔧 **Option 1: Local Python Development**

#### ✅ Prerequisites

* Python **3.12**
* `make` (optional)
* A Python virtual environment (recommended)

#### 📦 Installation

```sh
git clone https://github.com/Maede-alv/Todo-app.git
cd todo-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 🚀 Run the App

```sh
flet run main.py
```

#### 🌐 Run on Web (custom port optional)

```sh
flet run main.py --web --port 8000
```

#### 📱 Run on Mobile

```sh
flet run main.py --android --port 3423
flet run main.py --ios --port 5000
```

👉 For mobile setup guides: [Android Setup](https://flet.dev/docs/guides/python/android) | [iOS Setup](https://flet.dev/docs/guides/python/ios)

---

### 🐳 **Option 2: Run with Docker, PostgreSQL & Traefik** (⭐ Recommended for Production)

#### 🌍 Requirements

* Docker & Docker Compose
* A valid domain (e.g., `todo.example.com`)
* DNS provider API token (e.g., Cloudflare)

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
   docker-compose up -d
   ```

3. **Visit your app**
   👉 [https://todo.your-domain.com](https://todo.your-domain.com)

✅ **SSL Certificates** are managed automatically by Traefik and stored in the `letsencrypt/` folder (⚠️ do **not** commit this folder).

---

## 🤖 **Local CI/CD Testing with act**

Test your GitHub Actions workflow locally with [`act`](https://github.com/nektos/act).

#### ✅ Prerequisites

* Docker
* Install act:

  ```sh
  curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
  ```

#### 🔑 GitHub PAT

Generate a **Personal Access Token** (repo scope):

* GitHub → Settings → Developer settings → Personal access tokens (classic)

#### ⚙️ Configure act

Create `.actrc`:

```sh
echo "-W .github/workflows/ci.yml" > .actrc
echo "--secret GITHUB_TOKEN=your_personal_access_token" >> .actrc
echo "--defaultbranch main" >> .actrc
```

👉 Add `.actrc` to `.gitignore`:

```sh
echo ".actrc" >> .gitignore
```

#### 💻 Optional: Install Python dependencies for faster local tests

```sh
python -m venv venv
source venv/bin/activate
pip install pytest flake8 flet
pip install -r requirements.txt
```

#### 🚀 Run Workflows

```sh
git checkout main
act                # Run all jobs
act push -j test   # Run only tests
act push -j release # Run release job
act pull_request   # Simulate pull request workflow
act -v             # Verbose mode
```

---

## 📚 **Contributing**

💡 **Commit messages:** Follow [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat: add new filter`, `fix: resolve crash`).
🧪 **Run tests:**

```sh
pytest
```

✨ **Lint code:**

```sh
flake8 . --max-line-length=127
```

🤖 **Test workflows:**

```sh
act
```

---

## **Show your support**

If you like this project, ⭐ **star this repo** to help others find it!
Feel free to open issues or submit PRs. Happy coding! ✨

---

If you’d like, I can also add badges (build status, license, Docker pulls, etc.) or a table of contents. Let me know! 🚀
