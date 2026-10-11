# AI Agent Bootstrap Guide: `prepchess-ai-context`

Welcome to the **PrepChess/ChessGamma Master Ledger**.

## 1. Repository Purpose
This repository is the **Single Source of Truth (SSOT)** for the architecture, product vision, and domain language of the PrepChess ecosystem. It contains NO application code. 

**CRITICAL:** 
- If you are an agent working in `prepchess-ui` (Frontend), read `1-product/VISION.md`, `1-product/GLOSSARY.md`, and `2-architecture/FRONTEND_HOLLOW.md`.
- **Discovery Rule:** DO NOT read the `0-discovery/` folder during normal coding sessions. It is a braindump for unapproved ideas. Only read it if the user explicitly asks for ideation, competitor analysis, or to process `***IDEA:` tags. 
  - **Mandatory [PROPOSED] Tagging:** When incorporating ideas from `0-discovery/` into architecture, vision, or engine specs, always label them with `[PROPOSED]` tags (e.g., `[PROPOSED SPECIFICATION]`, `[PROPOSED ALGORITHM]`).
  - **Context & Market Notes:** General observations and competitor insights belong in `1-product/MARKET.md` or relevant files as background context.
  - **Contradiction & Irrelevance Gate:** If an incoming note or idea appears contradictory to the established product vision/constraints or seems irrelevant, do NOT incorporate it silently. You MUST pause and flag it for user confirmation.
  - **Archiving:** Once ideas from a file are processed, move the original file to `0-discovery/archive/` to prevent token waste and reprocessing.

## 2. The API Schema Rule
This repository defines the architecture, but it **DOES NOT** define the exact JSON API schema. 
- The backend (`opening-explorer`) is the sole owner of the API data contract (generated via Swagger/OpenAPI from Java DTOs). 
- Frontend agents must conform to the backend's schema.

## 3. Modifying This Repository
- **Never write code here.** 
- If you alter the architecture or system flows, you MUST update the relevant documents in `2-architecture/` and append an entry to `3-execution/DECISION_LOG.md`.
- Always use the Ubiquitous Language defined in `1-product/GLOSSARY.md`.

## 4. Roadmap Evolution Rule
- **Mandatory Consultation of `ROADMAP-EVOLUTION.md`:** Before making any modifications, re-sequencing, or additions to `3-execution/ROADMAP.md`, you MUST read `3-execution/ROADMAP-EVOLUTION.md`.
- **Proactive Commercial Warning:** You MUST proactively remind and warn the user to take into account the commercial and GTM trade-offs documented in `ROADMAP-EVOLUTION.md` (e.g., early paywalls, viral loops, coach distribution vs. heavy data science) before finalizing their proposed changes to `ROADMAP.md`.
- **ROADMAP vs. Repo Backlogs:** `ROADMAP.md` owns product milestones, commercial gates, and ecosystem capabilities. Repository-level backlogs (`prepchess-ui/TODO.md`, `opening-explorer/TODO.md`) own engineering tasks and must strictly synchronize their top priorities to mirror these roadmap milestones.

## 5. Specification & Planning Alignment Gate
- **The Vision Check (Planning Only):** When authoring new feature specifications in `3-execution/specs/` or modifying `3-execution/ROADMAP.md`, verify that the proposed features reinforce the **Psychological Asymmetry** and **Pawn Skeleton** principles defined in `1-product/VISION.md`. Reject or flag generic chess engine features that dilute this core value proposition. *(Note: Implementation/coding agents in other repositories derive their tasks directly from specs and do not need to perform this check).*

