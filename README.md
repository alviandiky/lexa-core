# LEXA — Global Transactional Compliance & Enforcement Core

LEXA is an infrastructure-first compliance enforcement engine designed to evaluate, decide, and audit transactional events in real time.

This repository contains the initial enterprise-grade MVP implementing:
- Deterministic transaction evaluation
- Explicit ALLOW / BLOCK enforcement
- Immutable audit logging
- API-first architecture

---

## Core Principles

- Infrastructure beats product
- Deterministic decisions over probabilistic guesses
- Every decision must be auditable
- No feature without direct compliance impact

---

## Current Capabilities (MVP)

### Health Check
GET /health

Returns system liveness status.

### Transaction Evaluation
POST /transactions

Evaluates a transaction payload and returns:
- decision: ALLOW or BLOCK
- reason: deterministic rule outcome

### Audit Log Access
GET /audit

Returns recorded audit trail of evaluated transactions.

---

## Architecture Overview

- FastAPI (API layer)
- Rule-based decision engine (core logic)
- File-based audit log (append-only)
- Stateless request processing

Designed for future extension into:
- External policy engines
- Database-backed audit storage
- Cryptographic audit integrity

---

## Running Locally

Requirements:
- Python 3.10+
- Git

Install dependencies:
pip install -r requirements.txt

Run server:
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

Access API:
http://localhost:8000

---

## Status

This project is an active foundational infrastructure.
Scope is intentionally narrow.
Every addition must reinforce compliance enforcement integrity.
