#!/bin/bash
DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR" || exit 1
source cyberdb/bin/activate
uvicorn app.main:app --reload --port 8000
