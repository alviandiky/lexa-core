from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class PolicyMeta:
    version: str
    active: bool
    deprecated: bool


POLICY_REGISTRY: Dict[str, PolicyMeta] = {
    "basic_v1": PolicyMeta(
        version="basic_v1",
        active=False,
        deprecated=True
    ),
    "basic_v2": PolicyMeta(
        version="basic_v2",
        active=True,
        deprecated=False
    )
}


def get_policy_meta(version: str) -> PolicyMeta:
    if version not in POLICY_REGISTRY:
        raise ValueError(f"Unknown policy version: {version}")
    return POLICY_REGISTRY[version]
