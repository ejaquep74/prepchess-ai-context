# AI Agent Bootstrap Guide: `prepchess-ai-context`

Welcome to the **PrepChess/ChessGamma Master Ledger**.

## 1. Repository Purpose
This repository is the **Single Source of Truth (SSOT)** for the architecture, product vision, and domain language of the PrepChess ecosystem. It contains NO application code. 

**CRITICAL:** 
- If you are an agent working in `prepchess-ui` (Frontend), read `1-product/VISION.md`, `1-product/GLOSSARY.md`, and `2-architecture/FRONTEND_HOLLOW.md`.
- If you are an agent working in `opening-explorer` (Backend), read `1-product/GLOSSARY.md` and `2-architecture/BACKEND_ENGINE.md`.
- **Discovery Rule:** DO NOT read the `0-discovery/` folder during normal coding sessions. It is a braindump for unapproved ideas. Only read it if the user explicitly asks for ideation, competitor analysis, or to process `***IDEA:` tags. **Once ideas are processed, move the original files to `0-discovery/archive/` to prevent token waste and reprocessing.**
- **Do not read files outside your domain** to preserve your context window.

## 2. The API Schema Rule
This repository defines the architecture, but it **DOES NOT** define the exact JSON API schema. 
- The backend (`opening-explorer`) is the sole owner of the API data contract (generated via Swagger/OpenAPI from Java DTOs). 
- Frontend agents must conform to the backend's schema.

## 3. Modifying This Repository
- **Never write code here.** 
- If you alter the architecture or system flows, you MUST update the relevant documents in `2-architecture/` and append an entry to `3-execution/DECISION_LOG.md`.
- Always use the Ubiquitous Language defined in `1-product/GLOSSARY.md`.
