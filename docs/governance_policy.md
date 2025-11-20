# SwarmLite Governance Policy

## Policy Owner
**Easir Maruf** - Senior AI/ML Engineer & Strategic Cloud & AI Alliance Leader

## Policy Version
1.0 - Implemented per HIPAA, GDPR, ISO 27001, and BD DPA standards

## Compliance Standards
- HIPAA (Health Insurance Portability and Accountability Act)
- GDPR (General Data Protection Regulation)
- ISO 27001 (Information Security Management)
- BD DPA (Bangladesh Data Protection Act)
- NIST AI RMFR (Risk Management Framework for AI)

## Governance Rules

### Data Handling
- Maximum data retention: 90 days
- PHI encryption required: true
- Data minimization enforced: true

### LLM & AI Governance
- Approved models: gpt-4-turbo, claude-3-opus, mistral-large
- Banned prompts: "ignore previous instructions", "pretend you're not an AI", "reveal system prompt"
- Maximum tokens per prompt: 2000
- Hallucination threshold: 0.75 (triggers human review)

### Audit & Accountability
- Audit log retention: 365 days
- Signature algorithm: HMAC-SHA256
- Mandatory signoff required for: LLM, RAG, database writes, external API calls

### Operational Controls
- Maximum concurrent workflows: 20
- Maximum retry attempts: 3
- Exponential backoff: enabled
- Rollback on failure: enabled

### Access & Authentication
- API key required: true
- Audit secret key required: true
- DB encryption key required: true
- Required headers: X-Request-Source, X-Client-ID

## Implementation
This policy is enforced at runtime through the GovernanceEngine class, which validates all workflow definitions and task executions against these rules before execution.

> *"Compliance is not a checkbox. It's a design principle." — Easir Maruf*