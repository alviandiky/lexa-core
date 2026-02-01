from app.policies import basic

def validate_policies():
    """
    Enforce policy immutability and lifecycle rules.
    This runs at system startup.
    """

    # Rule 1: Deprecated policy must not be active
    if basic.DEPRECATED:
        raise RuntimeError(
            f"Policy {basic.RULE_VERSION} is deprecated and must not be loaded."
        )

    # Rule 2: Rule hash must exist
    if not basic.RULE_HASH:
        raise RuntimeError(
            f"Policy {basic.RULE_VERSION} has no rule hash."
        )

    # Rule 3: Rule version must exist
    if not basic.RULE_VERSION:
        raise RuntimeError(
            "Policy version is missing."
        )
