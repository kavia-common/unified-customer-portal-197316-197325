# Unified Customer Portal - Backend

This FastAPI backend provides a versioned API under `/api/v1` with the following routers:
- Health: `GET /api/v1/health`
- Customers: `GET /api/v1/customers`, `GET /api/v1/customers/{id}`, `POST /api/v1/customers`, `PUT /api/v1/customers/{id}`, `DELETE /api/v1/customers/{id}`
- Activities: `GET /api/v1/customers/{id}/activities`

Schemas:
- Customer, CustomerCreate, CustomerUpdate
- Activity

Repository/Service:
- In-memory repositories with seed data wired through services for easy DB swap later.

Settings & CORS:
- Settings read from environment variables. Use FRONTEND_ORIGIN (or REACT_APP_FRONTEND_URL) to configure CORS.
- In production/preview over HTTPS, ensure FRONTEND_ORIGIN matches your frontend (e.g., https://vscode-internal-15894-beta.beta01.cloud.kavia.ai:3000).
- API prefix can be configured via API_PREFIX environment variable (default `/api/v1`).

Run:
- uvicorn src.api.main:app --host 0.0.0.0 --port 3001

Generate OpenAPI:
- python -m src.api.generate_openapi
- The schema is saved to `interfaces/openapi.json`.
