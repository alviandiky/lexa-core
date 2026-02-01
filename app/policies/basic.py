MAX_TRANSACTION_AMOUNT = 5000

def evaluate(transaction: dict) -> dict:
    amount = transaction.get("amount", 0)

    if amount > MAX_TRANSACTION_AMOUNT:
        return {
            "decision": "BLOCK",
            "reason": "Amount exceeds maximum allowed threshold"
        }

    return {
        "decision": "ALLOW",
        "reason": "Within allowed limits"
    }
