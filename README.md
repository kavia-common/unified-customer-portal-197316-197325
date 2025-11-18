# unified-customer-portal-197316-197325

Backend (FastAPI) is implemented with versioned routes under `/api/v1`:
- Health: `GET /api/v1/health`
- Customers: CRUD endpoints
- Activities: `GET /api/v1/customers/{id}/activities`

See `backend/README.md` for details and how to generate `interfaces/openapi.json`.