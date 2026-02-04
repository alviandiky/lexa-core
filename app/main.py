from fastapi import FastAPI
from app.core.policy_guard import validate_policies
from app.api.transactions import router as transaction_router
from app.api.audit import router as audit_router

app = FastAPI(
    title="LEXA CORE",
    description="Transactional Compliance & Enforcement Core",
    version="0.1.0"
)

# === POLICY ALLOWLIST (EXPLICIT & AUDITABLE) ===
ALLOWED_POLICIES = [
    "basic_v1",
    "basic_v2",
]

for policy_id in ALLOWED_POLICIES:
    validate_policies(policy_id)

# === ROUTERS ===
app.include_router(transaction_router)
app.include_router(audit_router)

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
