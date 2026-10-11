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


## ADR-005: PGN Parser Selection [PENDING-REVIEW]
* **Date:** 2026-10-10
* **Context:** The frontend needs to render deeply annotated PGNs, including Lichess-style arrows (`%cal`) and nested variations.
* **Decision:** We are evaluating `@mliebelt/pgn-parser` instead of the default `chess.js` PGN parsing logic. This remains a delicate technical decision under review.
* **Rationale:** `chess.js` lacks an Abstract Syntax Tree (AST) for deeply nested variations and does not natively parse graphical tags. `@mliebelt/pgn-parser` resolves this, allowing the frontend to remain hollow while rendering complex coach annotations.

## ADR-006: Hybrid Vectorization for Positional Analysis [PENDING-REVIEW]
* **Date:** 2026-10-10
* **Context:** Manually coding heuristic rules to classify pawn structures and outposts is brittle and fails on slight piece variations.
* **Decision:** Evaluated a Hybrid Vector extraction pipeline using NNUE (e.g., `jdart1/nnue` or `ChessLM`) and indexing positions into a Vector Database (FAISS/Milvus). Needs more careful analysis before final commitment.
* **Rationale:** This mathematically isolates the "tactical DNA" of a position, allowing the system to dynamically group similar positions for "Counter-Example Training" without relying on rigid FEN matching.


## ADR-007: Metadata Injection for LLM Commentary [PROPOSED / PENDING-REVIEW]
* **Date:** 2026-10-10
* **Context:** Using an LLM to generate opening explanations often causes hallucinations if the model is tasked with calculating board moves directly from FEN strings.
* **Decision:** Decouple calculation from narration. Engine evaluations and deterministic tree metadata (`key_pawn_breaks`, `common_maneuvers`) are assembled by the backend and injected into the prompt. The LLM acts purely as a translator/commentator.
* **Rationale:** Completely eliminates tactical hallucinations while maintaining engaging grandmaster-style commentary.

## ADR-008: Cross-Rating Distribution Projection [PROPOSED / PENDING-REVIEW]
* **Date:** 2026-10-10
* **Context:** Data at the 2500+ Elo level is sparse (13M games) compared to 2200 Elo (160M games), making probability estimation erratic on deeper branches.
* **Decision:** Use regression curves and probability drop-off models across 2000 and 2200 tiers to adjust and project 2500+ move likelihoods, while sourcing blunder refutations from high-eval 2200 games.
* **Rationale:** Prevents severe sample-size starvation on deep master variations without requiring billions of expensive synthetic engine rollouts.


## ADR-009: Move 20 Hybrid EV & Clock Burn Weighting [PROPOSED / PENDING-REVIEW]
* **Date:** 2026-10-10
* **Context:** Pure centipawn evaluations at early plies (e.g., move 10-12) often fail to capture practical winning conversion or human cognitive friction.
* **Decision:** Anchor opening utility to the sustained evaluation at move 20 (The 25-Move Cap) and inject a Clock Burn Index multiplier for lines that force human opponents into severe time expenditure.
* **Rationale:** Aligns the algorithm with practical match victory rather than theoretical engine perfection.

## ADR-010: Sequential Pattern Mining for Winning Highways [PROPOSED / PENDING-REVIEW]
* **Date:** 2026-10-10
* **Context:** Extracting actionable positional advice from hundreds of millions of moves requires isolating recurring piece maneuvers without manual hardcoding.
* **Decision:** Utilize sequential pattern mining (PrefixSpan / N-grams) alongside differential occupancy heatmaps to mathematically extract "winning highways."
* **Rationale:** Provides objective, data-backed maneuver paths that can be automatically converted into visual coach recommendations by Gamma.

## ADR-011: Inflection Point Sparring & Pedagogical Evaluation Tolerance
* **Date:** 2026-10-11
* **Context:** Traditional chess training platforms either drop users into post-blunder tactical puzzles (reactive) or enforce dogmatic, single-move rote memorization from move 1 (Chessable's "Move Rejection Rage").
* **Decision:** 
  1. **Configurable Inflection Point Sparring:** Drop the player $N$ moves *before* the critical blunder or sacrifice occurs, forcing active game-readiness within the escalating tension.
  2. **Pedagogical Blind Testing ("No Spoilers"):** Do not reveal beforehand whether the upcoming critical move is an opponent error or player blunder; challenge the user to play sound chess under pressure.
  3. **Dynamic Evaluation Tolerance ($\le 0.5$ Eval Distance):** Accept alternative candidate moves that preserve dynamic advantage ($\le 0.5$ eval delta) with positive co-pilot feedback, rewarding strategic chess comprehension over single-path memorization.
* **Rationale:** Solves the core user frustration in online chess education, drastically improving training retention and practical over-the-board transfer.

