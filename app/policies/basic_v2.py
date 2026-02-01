import os
from datetime import date
from dotenv import load_dotenv
from app.utils.rule_hash import compute_rule_hash

load_dotenv()

# === POLICY GOVERNANCE METADATA ===
RULE_VERSION = "basic_v2"
EFFECTIVE_FROM = date(2026, 2, 1)
DEPRECATED = False

# === CRYPTOGRAPHIC PROVENANCE ===
RULE_HASH = compute_rule_hash(__file__)

# === POLICY PARAMETERS (V2) ===
# Contoh perubahan: threshold lebih tinggi
MAX_TRANSACTION_AMOUNT = int(os.getenv("MAX_TRANSACTION_AMOUNT_V2", "10000"))

def evaluate(transaction: dict) -> dict:
    amount = transaction.get("amount", 0)

    if amount > MAX_TRANSACTION_AMOUNT:
        decision = "BLOCK"
        reason = "Amount exceeds maximum allowed threshold (v2)"
    else:
        decision = "ALLOW"
        reason = "Within allowed limits (v2)"

    return {
        "decision": decision,
        "reason": reason,
        "rule_version": RULE_VERSION,
        "rule_hash": RULE_HASH
    }
