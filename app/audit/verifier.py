import json
import hashlib
from pathlib import Path

AUDIT_LOG_FILE = "audit.log"
GENESIS_HASH = "GENESIS"


def _compute_hash(record: dict) -> str:
    """
    Compute deterministic SHA256 hash of a log record
    (excluding the 'hash' field itself).
    """
    record_copy = dict(record)
    record_copy.pop("hash", None)

    serialized = json.dumps(record_copy, sort_keys=True).encode()
    return hashlib.sha256(serialized).hexdigest()


def verify_audit_chain() -> bool:
    """
    Verify integrity of the audit log chain.

    Rules:
    - First record MUST have prev_hash == GENESIS
    - Each record.prev_hash MUST equal previous record.hash
    - Each record.hash MUST match recomputed hash
    """

    log_path = Path(AUDIT_LOG_FILE)

    if not log_path.exists():
        raise ValueError("❌ audit.log not found")

    lines = log_path.read_text().strip().splitlines()

    if not lines:
        raise ValueError("❌ audit.log is empty")

    previous_hash = GENESIS_HASH

    for index, line in enumerate(lines, start=1):
        record = json.loads(line)

        # 1. Check prev_hash continuity
        if record.get("prev_hash") != previous_hash:
            raise ValueError(
                f"❌ Chain broken at line {index}: prev_hash mismatch"
            )

        # 2. Verify hash integrity
        expected_hash = _compute_hash(record)
        if record.get("hash") != expected_hash:
            raise ValueError(
                f"❌ Chain broken at line {index}: hash mismatch"
            )

        previous_hash = record["hash"]

    return True
