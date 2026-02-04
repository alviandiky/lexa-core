def on_allow(context: dict):
    """
    Hook executed when a transaction is ALLOWED.
    No side-effects for now.
    """
    pass


def on_block(context: dict):
    """
    Hook executed when a transaction is BLOCKED.
    Placeholder for future enforcement actions:
    - freeze account
    - notify regulator
    - emit event
    """
    pass
