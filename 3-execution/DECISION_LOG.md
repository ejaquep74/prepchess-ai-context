# Architecture Decision Records (ADR)

## ADR-001: The "Hollow Frontend" Architecture
* **Date:** 2024
* **Context:** Chess web clients often implement engine evaluation natively in the browser via WebAssembly (e.g., Stockfish.wasm).
* **Decision:** We will use a strictly "Hollow Frontend" where the client only renders sanitized data (flags and badges).
* **Rationale:** Protects the proprietary Multi-Objective Utility $U(n)$ coefficients and matrix scoring logic from being scraped or reverse-engineered via minified client bundles.

## ADR-002: PostgreSQL Migration
* **Date:** 2024
* **Context:** The prototype MVP 1 utilized an H2 in-memory/file-based database. 
* **Decision:** Migrated to PostgreSQL with Caffeine in-memory caching.
* **Rationale:** H2 cannot support the MVCC row-level concurrency and batch writing optimizations (`reWriteBatchedInserts=true`) required for massive tree storage and concurrent multi-user load.

## ADR-003: Backend Ownership of API Schema
* **Date:** 2026-10
* **Context:** Deciding where to store the single source of truth for the REST API shape.
* **Decision:** The `opening-explorer` (backend) repository exclusively owns the API schema.
* **Rationale:** Utilizing tools like Springdoc/Swagger, the backend can auto-generate the schema directly from the Java DTOs, preventing drift. The AI context repo will not duplicate this schema.
