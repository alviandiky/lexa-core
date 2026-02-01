import json
import hashlib
from datetime import datetime
from pathlib import Path

AUDIT_LOG_FILE = Path("audit.log")


def _get_last_hash() -> str:
    if not AUDIT_LOG_FILE.exists():
        return "0" * 64

    try:
        with AUDIT_LOG_FILE.open("r") as f:
            last_line = None
            for line in f:
                last_line = line

            if not last_line:
                return "0" * 64

            record = json.loads(last_line)
            return record.get("hash", "0" * 64)
    except Exception:
        return "0" * 64


def _calculate_hash(payload: dict) -> str:
    serialized = json.dumps(payload, sort_keys=True).encode()
    return hashlib.sha256(serialized).hexdigest()


def write(entry: dict):
    prev_hash = _get_last_hash()

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "entry": entry,
        "prev_hash": prev_hash,
    }

    record["hash"] = _calculate_hash(record)

    with AUDIT_LOG_FILE.open("a") as f:
        f.write(json.dumps(record) + "\n")
