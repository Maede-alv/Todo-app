# Todo App 📝

A simple and scalable **To-Do List** application built with [Flet](https://flet.dev/), featuring **PostgreSQL support**, **Dockerization**, and **automatic HTTPS via Traefik & Let's Encrypt**.

## ✨ Features
- Add, update, and delete tasks
- Track task progress with statuses: "To-Do", "In Progress", "Done"
- Filter tasks by status
- Supports both in-memory and PostgreSQL storage
- Dockerized with Traefik reverse proxy
- Automatic SSL certificates via DNS challenge (e.g., Cloudflare)
- CI/CD with GitHub Actions for testing, linting, and semantic releases

---

## 🧰 Setup Options

### Option 1: Local Python Development

#### ✅ Prerequisites
- Python 3.12
- `make` (optional, for Makefile commands)
- Virtual environment (recommended)

#### 📦 Installation
```sh
git clone https://github.com/Maede-alv/Todo-app.git
cd todo-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

🚀 Run the App
flet run main.py

🌐 Run on Web (custom port optional)
flet run main.py --web --port 8000

📱 Android / iOS
flet run main.py --android --port 3423
flet run main.py --ios --port 5000


For mobile setup guides:Android Setup | iOS Setup


Option 2: Run with Docker, PostgreSQL & Traefik (Recommended for Production) 🐳🔒
🌍 Requirements

Docker & Docker Compose
Valid domain (e.g., todo.example.com)
DNS provider API token (e.g., Cloudflare)

⚙️ Steps

Configure environment variablesCopy .env.example to .env and set your values:
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


Start services
docker-compose up -d


Visit your app
https://todo.your-domain.com




Note: DNS Challenge is used for SSL with Let's Encrypt. Ensure your DNS provider supports API access (e.g., Cloudflare).


🔐 SSL Certificates

Managed automatically by Traefik using DNS challenge
Stored in the letsencrypt/ folder (auto-created)
Do not commit this folder to version control:letsencrypt/


🤖 Local Workflow Testing with act
Test the GitHub Actions workflow locally using act to simulate CI tasks.
✅ Prerequisites

Docker (required for act)
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash


A GitHub PAT with repo scope for the release job.

⚙️ Setup

Create a PAT:

Go to GitHub Settings > Developer settings > Personal access tokens > Tokens (classic).
Generate a token with repo scope.
Save it securely (e.g., in a local .env file or as an environment variable).


Configure act:

Create an .actrc file in the repository root:echo "-W .github/workflows/ci.yml" > .actrc
echo "--secret GITHUB_TOKEN=your_personal_access_token" >> .actrc
echo "--defaultbranch main" >> .actrc


Replace your_personal_access_token with your PAT.
Alternatively, set GITHUB_TOKEN:export GITHUB_TOKEN=your_personal_access_token


Add .actrc to .gitignore:echo ".actrc" >> .gitignore




Install Python dependencies locally (optional, for faster testing):
python -m venv venv
source venv/bin/activate
pip install pytest flake8 flet
pip install -r requirements.txt



🚀 Run the Workflow Locally

Ensure you’re on the main branch:git checkout main


Run the entire workflow:act


Run specific jobs:
Test job:act push -j test


Release job:act push -j release


Pull request:act pull_request




Debug with verbose output:act -v



📝 Notes

The test job runs flake8 for linting and pytest for tests.
The release job requires GITHUB_TOKEN and conventional commits (e.g., feat: add feature, fix: resolve bug).
If no release PR is created, ensure recent commits use conventional commits.
Ensure pyproject.toml or setup.py has a version field (e.g., version = "0.3.1").
act requires Docker to simulate ubuntu-latest.


Tip: Use act -v for detailed logs. See act documentation for more options.


📚 Contributing

Follow conventional commits for commit messages.
Run tests locally: pytest
Check linting: flake8 . --max-line-length=127
Test workflows locally with act before pushing.


