import os
from dotenv import load_dotenv
from app.utils.rule_hash import compute_rule_hash

load_dotenv()

RULE_VERSION = "basic_v1"
MAX_TRANSACTION_AMOUNT = int(os.getenv("MAX_TRANSACTION_AMOUNT", "5000"))

RULE_HASH = compute_rule_hash(__file__)

def evaluate(transaction: dict) -> dict:
    amount = transaction.get("amount", 0)

    if amount > MAX_TRANSACTION_AMOUNT:
        return {
            "decision": "BLOCK",
            "reason": "Amount exceeds maximum allowed threshold",
            "rule_version": RULE_VERSION,
            "rule_hash": RULE_HASH,
        }

    return {
        "decision": "ALLOW",
        "reason": "Within allowed limits",
        "rule_version": RULE_VERSION,
        "rule_hash": RULE_HASH,
    }
