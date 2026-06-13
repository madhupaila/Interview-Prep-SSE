# Security, Auth & Multi-Tenancy

## Definition

**Authentication** verifies identity. **Authorization** controls access. **Multi-tenancy** isolates data between customers (tenants).

---

## Authentication

| Method | Use |
|--------|-----|
| OAuth 2.0 + OIDC | Social login, enterprise SSO |
| JWT | Stateless API tokens |
| Session cookies | Web apps with server-side session |
| API keys | Service-to-service, developer APIs |
| mTLS | Service mesh internal auth |

**JWT flow:** Login → issue signed JWT → client sends `Authorization: Bearer` → service validates signature.

---

## Authorization

| Model | Description |
|-------|-------------|
| RBAC | Roles (admin, user) with permissions |
| ABAC | Attribute-based (department, region) |
| ACL | Per-resource access lists |

---

## Multi-Tenancy Models

| Model | Isolation | Cost |
|-------|-----------|------|
| Shared DB, tenant_id column | Logical | Lowest |
| Schema per tenant | Medium | Medium |
| DB per tenant | Strong | Highest |

**Senior mention:** Row-level security, encryption per tenant, noisy neighbor limits.

---

## Data Protection

- **Encryption at rest:** AES-256 (KMS-managed keys)
- **Encryption in transit:** TLS 1.3
- **PII:** Minimize collection, tokenize, support deletion (GDPR)
- **Secrets:** Vault, AWS Secrets Manager — never in code

---

## Gen AI Security

- Prompt injection defense: input sanitization, system prompt isolation
- PII redaction before sending to LLM
- Output filtering for toxic/harmful content
- Audit logs for compliance

---

## Interview Phrases

> "OAuth for user login; JWT for API auth with 1h expiry + refresh token."
> "Multi-tenant SaaS: tenant_id on every row + row-level security in Postgres."
> "PII redacted before LLM inference; audit log retained 7 years."

---

## Memory Map

```
SECURITY
├── Auth: OAuth | JWT | API keys
├── AuthZ: RBAC | ABAC
├── Multi-tenant: tenant_id | schema | DB per tenant
├── Encrypt: TLS (transit) + KMS (rest)
└── Gen AI: PII redact | prompt injection defense
```
