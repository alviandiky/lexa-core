from fastapi import APIRouter
from app.policies.registry import load_policy
from app.audit import logger
from app.enforcement import hooks

router = APIRouter()

@router.post("/transactions")
def ingest_transaction(payload: dict):
    policy_id = payload.get("policy", "basic_v1")

    policy = load_policy(policy_id)
    result = policy.evaluate(payload)

    context = {
        "transaction": payload,
        "decision": result
    }

    # === AUDIT FIRST (NON-NEGOTIABLE) ===
    logger.write(context)

    # === ENFORCEMENT HOOKS ===
    if result["decision"] == "BLOCK":
        hooks.on_block(context)
    else:
        hooks.on_allow(context)

    return result
