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

Migrated to PostgreSQL for multi-instance scaling and MVCC concurrency (`reWriteBatchedInserts=true`).

* **Nodes Table:** `repertoire_nodes` tracks `session_id`, `parent_id`, `move_san`, `fen`, `mean_eval`, `std_dev_eval`, `player_sac`, `opp_sac`, `opp_play_prob`.
* **Caching:** Caffeine holds active session trees in memory (`expireAfterAccess(15, TimeUnit.MINUTES)`), allowing slider tweaks to complete backpropagation in <15ms.
* **O(N) Reconstruction:** Uses a single-pass `HashMap<Long, RepertoireNode>` to connect parents to children.
