# Architecture Decision Records (ADR)

## ADR-001: The "Hollow Frontend" Architecture
* **Date:** 2024
* **Context:** Chess web clients often implement engine evaluation natively in the browser via WebAssembly (e.g., Stockfish.wasm).
* **Decision:** We will use a strictly "Hollow Frontend" where the client only renders sanitized data (flags and badges).
* **Rationale:** Protects the proprietary Multi-Objective Utility $U(n)$ coefficients and matrix scoring logic from being scraped or reverse-engineered via minified client bundles.

## ADR-002: PostgreSQL Migration (PENDING)
* **Date:** 2024 (Planned)
* **Context:** The current MVP utilizes an H2 database coupled with a `BuildCheckpointService` for session resumption.
* **Decision:** We will migrate to PostgreSQL with Caffeine in-memory caching.
* **Rationale:** H2 cannot support the MVCC row-level concurrency and batch writing optimizations (`reWriteBatchedInserts=true`) required for massive tree storage and concurrent multi-user load in production.

## ADR-003: Backend Ownership of API Schema
* **Date:** 2026-10
* **Context:** Deciding where to store the single source of truth for the REST API shape.
* **Decision:** The `opening-explorer` (backend) repository exclusively owns the API schema.
* **Rationale:** Utilizing tools like Springdoc/Swagger, the backend can auto-generate the schema directly from the Java DTOs, preventing drift. The AI context repo will not duplicate this schema.

## ADR-004: UI-Driven Backend Debugging (80% Backend Rule)
* **Date:** 2026-10-10
* **Context:** The backend tree-building logic has reached ~80% stability. Debugging complex recursive issues (transpositions, exploding trees, missing games) via raw JSON is extremely inefficient.
* **Decision:** Pause deep backend optimization. Shift primary focus to the frontend `prepchess-ui` to finish building the visual tree explorer.
* **Rationale:** Rendering the tree graphically in the frontend is the only practical way to visually expose and diagnose the remaining 20% of backend edge cases (e.g., parent-node mismatches and transposition errors).


## ADR-005: PGN Parser Selection
* **Date:** 2026-10-10
* **Context:** The frontend needs to render deeply annotated PGNs, including Lichess-style arrows (`%cal`) and nested variations.
* **Decision:** We will use `@mliebelt/pgn-parser` instead of the default `chess.js` PGN parsing logic.
* **Rationale:** `chess.js` lacks an Abstract Syntax Tree (AST) for deeply nested variations and does not natively parse graphical tags. `@mliebelt/pgn-parser` resolves this, allowing the frontend to remain hollow while rendering complex coach annotations.

## ADR-006: Hybrid Vectorization for Positional Analysis
* **Date:** 2026-10-10
* **Context:** Manually coding heuristic rules to classify pawn structures and outposts is brittle and fails on slight piece variations.
* **Decision:** Implement a Hybrid Vector extraction pipeline using NNUE (e.g., `jdart1/nnue` or `ChessLM`) and index positions into a Vector Database (FAISS/Milvus).
* **Rationale:** This mathematically isolates the "tactical DNA" of a position, allowing the system to dynamically group similar positions for "Counter-Example Training" without relying on rigid FEN matching.
