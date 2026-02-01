import json
from datetime import datetime

AUDIT_LOG_FILE = "audit.log"

def write(entry: dict):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "entry": entry
    }

    with open(AUDIT_LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
