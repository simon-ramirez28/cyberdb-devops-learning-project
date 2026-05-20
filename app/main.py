from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers import data, stats

app = FastAPI(
    title="CyberDB — Mercado Negro de Datos",
    description="API del mercado negro de datos. Sube, consulta y rastrea información anónima.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data.router)
app.include_router(stats.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def root():
    from fastapi.responses import FileResponse
    return FileResponse("app/static/index.html")


@app.get("/health")
def health():
    return {"status": "ok", "service": "cyberdb"}
