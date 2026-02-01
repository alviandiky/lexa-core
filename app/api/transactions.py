from fastapi import APIRouter
from app.policies import basic
from app.audit import logger

router = APIRouter()

@router.post("/transactions")
def ingest_transaction(payload: dict):
    result = basic.evaluate(payload)

    audit_entry = {
        "transaction": payload,
        "decision": result["decision"],
        "reason": result["reason"]
    }

    logger.write(audit_entry)

    return {
        "decision": result["decision"],
        "reason": result["reason"]
    }
