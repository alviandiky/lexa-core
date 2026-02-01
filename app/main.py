from fastapi import FastAPI
from app.api.transactions import router as transaction_router

app = FastAPI(
    title="LEXA CORE",
    description="Transactional Compliance & Enforcement Core",
    version="0.1.0"
)
app.include_router(transaction_router)

@app.get("/")
def root():
    return {
        "status": "alive",
        "system": "lexa-core"
    }
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "component": "core",
        "version": "0.1.0"
    }
