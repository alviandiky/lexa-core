import json
import hashlib
from datetime import datetime
from pathlib import Path

AUDIT_LOG_FILE = "audit.log"
GENESIS_HASH = "GENESIS"


def _compute_hash(record: dict) -> str:
    serialized = json.dumps(record, sort_keys=True).encode()
    return hashlib.sha256(serialized).hexdigest()


def write(entry: dict):
    log_path = Path(AUDIT_LOG_FILE)

    if log_path.exists() and log_path.stat().st_size > 0:
        last_line = log_path.read_text().strip().splitlines()[-1]
        last_record = json.loads(last_line)
        prev_hash = last_record["hash"]
    else:
        prev_hash = GENESIS_HASH

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "entry": entry,
        "prev_hash": prev_hash,
    }

    record["hash"] = _compute_hash(record)

    with open(AUDIT_LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
def write_system_event(event: dict):
    write({
        "type": "SYSTEM_EVENT",
        "event": event
    })
