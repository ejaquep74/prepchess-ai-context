# Master System Architecture

## 1. Core Philosophy

**PrepChess (ChessGamma)** is an adaptive, algorithmic chess opening repertoire generator and interactive study platform. Traditional engines rely on standard Minimax search to identify the "objectively best" move, assuming perfect play. This produces "tightrope" lines—positions where a single human inaccuracy leads to immediate collapse.

PrepChess introduces the **"Practical Human Eval"** framework:
1. **Minefields vs. Tightropes:** Identifies lines where human opponents are statistically prone to errors.
2. **Multi-Objective Utility:** Instead of pure centipawn scores, candidate branches are evaluated using a custom utility function combining mean evaluation, volatility ($\sigma$), and sacrifice metrics.
3. **Hollow Frontend Security:** All proprietary math executes strictly on the backend.

## 2. Component Responsibilities

```mermaid
flowchart TD
    subgraph Client ["CLIENT LAYER (prepchess-ui)"]
        direction TB
        C1["• Board Rendering: chessground"]
        C2["• Rule Engine & Tree Traversal: chessops"]
        C3["• Debounced Style Sliders (Volatility, Sacrifices)"]
    end

    subgraph Backend ["BACKEND LAYER (opening-explorer)"]
        direction TB
        B1["• Repertoire Backpropagator Service (Expectiminimax)"]
        B2["• In-Memory Cache: Caffeine Cache"]
        B3["• Relational Storage: PostgreSQL (MVCC)"]
    end

    subgraph Pipeline ["OFFLINE PIPELINE"]
        direction TB
        P1["• Stockfish Worker Pool (FEN Evaluator)"]
        P2["• Maia-3 Refutation Engine (Bounded Rationality)"]
    end

    Client -- "REST API (API Schema owned by Backend)" --> Backend
    Backend -- "Internal Queue" --> Pipeline
```

## 3. Database Schema Overview

Currently implemented using an **H2 Database** (file-based) coupled with a robust `BuildCheckpointService` for session resumption and async state persistence.

* **Session Entities:** `BuildSessionEntity` tracks the lifecycle of an `IN_PROGRESS` repertoire run.
* **Checkpointing Cache:** `ExploredFenEntity` and `EvaluatedFenEntity` track completed subtrees and FEN evaluations to allow instant O(1) skips across restarts.
* **O(N) Reconstruction:** Uses a single-pass `HashMap<Long, RepertoireNode>` to connect parents to children during rendering.
* **Future Scaling:** Migration to PostgreSQL (MVCC, `reWriteBatchedInserts=true`) is planned for MVP 2 to support multi-user concurrent generation.


## 4. Metadata Injection Architecture for AI Commentary [PROPOSED ARCHITECTURE]

To generate grandmaster-level natural language commentary without hallucinations or expensive client-side compute, the system implements the **Metadata Injection Pattern**:

```mermaid
flowchart LR
    A["Board Position (FEN)"] --> B["Stockfish Engine (Grounding)"]
    A --> C["Opening Tree Database (Metadata)"]
    B -- "Numeric Score + Tactical Flags" --> D["Prompt Orchestrator"]
    C -- "Theoretical Facts (Breaks, Maneuvers)" --> D
    D --> E["LLM Commentator (Translator)"]
    E --> F["Natural Language Explanation"]
```

### Pipeline Principles
1. **Engine Grounding:** The LLM NEVER calculates moves or evaluates raw FENs. Stockfish provides structured numeric signals (e.g., `score: +0.6`, `flag: hanging_piece`).
2. **Deterministic Metadata Injection:** Position nodes in relational storage (PostgreSQL per ADR-002) store structured theoretical attributes:
   * `key_pawn_breaks`: Array of critical levers (e.g., `["d4", "c5"]`).
   * `common_maneuvers`: Standard piece routes (e.g., `["Nb1-d2-f1-g3"]`).
   * `strategic_goals`: High-level objectives (e.g., `["Control d5 square", "Minority attack"]`).
3. **LLM as Pure Translator:** The LLM acts strictly as a natural language synthesizer, translating the structured engine score and injected opening facts into human coaching advice.
4. **Vector RAG Fallback:** For novel positions outside the precomputed opening tree, vector embeddings of the pawn/piece structure are used to retrieve commentary from historically similar positions.
