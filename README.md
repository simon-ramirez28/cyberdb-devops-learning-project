# ⚡ CyberDB — Data Black Market

A cyberpunk-themed REST API and web UI for anonymously submitting, querying, and tracking data leaks. Built with **FastAPI** as a DevOps learning project — from code to containerized deployment.

## Features

- **Anonymous submissions** — Post data and get a unique NetRunner handle (e.g. `Neo_42`, `ZeroCool_7`)
- **Data integrity** — Each record is SHA-256 hashed
- **Full CRUD** — Create, list, retrieve by ID, and delete records
- **Live statistics** — Total records, top NetRunners, recent activity
- **Cyberpunk UI** — Dark theme with neon green, scanlines, and glitch effects served directly from FastAPI

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI (Python) |
| Frontend | HTML + CSS + JS (vanilla) |
| Testing | pytest + httpx |
| Containerization | Docker (multi-stage) |
| CI/CD | GitHub Actions → GitHub Container Registry |

## Project Structure

```
.
├── app/
│   ├── main.py              # FastAPI application
│   ├── models.py            # Pydantic schemas
│   ├── database.py          # In-memory data store
│   ├── utils.py             # Handle generation & hashing
│   ├── routers/
│   │   ├── data.py          # CRUD endpoints
│   │   └── stats.py         # Statistics endpoint
│   └── static/
│       ├── index.html       # Web UI
│       ├── style.css        # Cyberpunk theme
│       └── script.js        # Frontend logic
├── tests/
│   ├── conftest.py          # pytest fixtures
│   └── test_api.py          # 8 integration tests
├── scripts/
│   └── start_local.sh       # Run locally (works from any directory)
├── requirements.txt
├── Dockerfile
├── .github/workflows/ci.yml
└── README.md
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Service health check |
| `POST` | `/api/data` | Submit a new data record |
| `GET` | `/api/data` | List records (`?skip=0&limit=50`) |
| `GET` | `/api/data/{id}` | Get record by ID |
| `DELETE` | `/api/data/{id}` | Delete record by ID |
| `GET` | `/api/stats` | Usage statistics |

Interactive API docs available at `/docs` (Swagger UI).

## Quick Start

### Prerequisites

- Python 3.11+
- (Optional) Docker

### Run locally

```bash
# 1. Clone the repository
git clone https://github.com/<your-user>/cyberdb.git
cd cyberdb

# 2. Create virtual environment and install dependencies
python3 -m venv cyberdb
source cyberdb/bin/activate
pip install -r requirements.txt

# 3. Start the server
./scripts/start_local.sh
```

Open **http://localhost:8000** for the web UI or **http://localhost:8000/docs** for the API docs.

### Run tests

```bash
source cyberdb/bin/activate
pytest -v
```

## Roadmap

- [x] FastAPI app with CRUD + stats
- [x] Cyberpunk web UI
- [x] Integration tests
- [ ] Docker multi-stage build
- [ ] GitHub Actions CI/CD (auto-build & push to ghcr.io)
- [ ] LocalStack integration (AWS S3 for persistence)

## License

MIT
