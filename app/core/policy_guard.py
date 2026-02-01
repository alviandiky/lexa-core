from app.policies import basic
from app.policies import basic_v2

def _validate(policy):
    if policy.DEPRECATED:
        raise RuntimeError(
            f"Policy {policy.RULE_VERSION} is deprecated and must not be loaded."
        )

    if not policy.RULE_VERSION:
        raise RuntimeError("Policy version is missing.")

    if not policy.RULE_HASH:
        raise RuntimeError(
            f"Policy {policy.RULE_VERSION} has no rule hash."
        )

def validate_policies():
    _validate(basic)      # basic_v1
    _validate(basic_v2)   # basic_v2
