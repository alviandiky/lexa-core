# LEXA CORE — Governance & Change Control

## Change Classification

LEXA enforces strict separation between execution and governance.

### 1. Non-Behavioral Changes
Changes that DO NOT affect transaction outcomes.
Examples:
- Documentation updates
- Logging format extensions
- Internal refactoring without logic change

Approval: Engineering Lead  
Audit: Optional

---

### 2. Behavioral Changes (Policy Changes)
Changes that MAY alter transaction decisions.
Examples:
- Threshold modification
- New decision branches
- Policy logic rewrite

Approval: Governance Process Required  
Audit: Mandatory  
Execution: Versioned policy only

---

### 3. Emergency Overrides
Temporary behavior changes for system safety.

Rules:
- Must be explicitly logged
- Time-bound
- Requires post-mortem audit

---

## Core Rule

No behavioral change is allowed without:
- Versioned policy
- Audit chain entry
- Explicit governance action
