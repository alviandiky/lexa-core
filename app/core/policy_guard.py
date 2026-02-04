from app.policies.registry import load_policy

def validate_policies(policy_id: str):
    """
    Guard layer.
    CORE will refuse to boot if a registered policy is broken.
    """
    load_policy(policy_id)
