from fastapi import APIRouter
from app.policies import basic, basic_v2
from app.audit import logger

router = APIRouter()

@router.post("/transactions")
def ingest_transaction(payload: dict):
    # === POLICY SELECTION (EXPLICIT) ===
    policy = payload.get("policy", "v1")

    if policy == "v2":
        decision = basic_v2.evaluate(payload)
    else:
        decision = basic.evaluate(payload)

    audit_entry = {
        "transaction": payload,
        "decision": decision
    }

    logger.write(audit_entry)

    return decision
