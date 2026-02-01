import hashlib
from pathlib import Path

def compute_rule_hash(policy_file: str) -> str:
    content = Path(policy_file).read_text(encoding="utf-8")

    normalized = (
        content
        .replace("\r\n", "\n")
        .strip()
    )

    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()
