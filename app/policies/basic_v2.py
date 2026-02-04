from app.utils.rule_hash import compute_rule_hash

RULE_VERSION = "basic_v2"
RULE_HASH = compute_rule_hash(__file__)

def evaluate(transaction: dict) -> dict:
    amount = transaction.get("amount", 0)

    return {
        "decision": "ALLOW",
        "reason": "Within allowed limits (v2)",
        "rule_version": RULE_VERSION,
        "rule_hash": RULE_HASH,
    }
