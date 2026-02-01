import os
from datetime import date
from dotenv import load_dotenv
from app.utils.rule_hash import compute_rule_hash

load_dotenv()

# === POLICY GOVERNANCE METADATA ===
RULE_VERSION = "basic_v1"
EFFECTIVE_FROM = date(2026, 2, 1)
DEPRECATED = False

# === CRYPTOGRAPHIC PROVENANCE (DO NOT TOUCH) ===
RULE_HASH = compute_rule_hash(__file__)

# === POLICY PARAMETERS ===
MAX_TRANSACTION_AMOUNT = int(os.getenv("MAX_TRANSACTION_AMOUNT", "5000"))

def evaluate(transaction: dict) -> dict:
    """
    Evaluate a transaction against the Basic Transaction Amount Policy.

    This function is the single source of truth for:
    - decision
    - reason
    - rule_version
    - rule_hash
    """

    amount = transaction.get("amount", 0)

    if amount > MAX_TRANSACTION_AMOUNT:
        decision = "BLOCK"
        reason = "Amount exceeds maximum allowed threshold"
    else:
        decision = "ALLOW"
        reason = "Within allowed limits"

    return {
        "decision": decision,
        "reason": reason,
        "rule_version": RULE_VERSION,
        "rule_hash": RULE_HASH
    }
