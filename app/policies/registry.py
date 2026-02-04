from importlib import import_module

# === CANONICAL POLICY REGISTRY ===
# Hanya policy yang TERDAFTAR di sini yang boleh hidup.
POLICY_REGISTRY = {
    "basic_v1": {
        "module": "app.policies.basic_v1",
        "description": "Basic transaction threshold policy v1"
    },
    "basic_v2": {
        "module": "app.policies.basic_v2",
        "description": "Adjusted threshold policy v2"
    }
}

def load_policy(policy_id: str):
    if policy_id not in POLICY_REGISTRY:
        raise ValueError(f"Policy '{policy_id}' is not registered")

    module_path = POLICY_REGISTRY[policy_id]["module"]

    try:
        module = import_module(module_path)
    except Exception as e:
        raise ImportError(f"Failed to load policy module '{module_path}': {e}")

    if not hasattr(module, "evaluate"):
        raise AttributeError(
            f"Policy '{policy_id}' does not expose required 'evaluate()' function"
        )

    return module
