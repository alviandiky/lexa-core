from fastapi import APIRouter
from app.policies import basic
from app.audit import logger

router = APIRouter()

@router.post("/transactions")
def ingest_transaction(payload: dict):
    # 1. Jalankan policy (JANGAN DIPRETELI)
    decision = basic.evaluate(payload)

    # 2. Audit SELURUH decision object
    audit_entry = {
        "transaction": payload,
        "decision": decision
    }

    logger.write(audit_entry)

    # 3. Kembalikan decision UTUH
    return decision
