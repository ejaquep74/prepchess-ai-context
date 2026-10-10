# PrepChess AI Context (Master Ledger)

This repository serves as the central hub for specifications, architecture, and multi-agent context for the **ChessGamma (PrepChess)** ecosystem.

## Ecosystem Topology

The system is distributed across the following repositories:

*   **`prepchess-ai-context` (This Repo):** The Master Ledger. Defines the mathematical models, UI constraints, and product vision.
*   **`opening-explorer` (Backend):** Java 21 / Spring Boot service handling the Expectiminimax engine, database, and Maia-3 refutation pipeline. *The backend strictly owns the API schema.*
*   **`prepchess-ui` (Frontend):** React 19 / Vite application acting as a "Hollow Frontend" to render the backend's computed tree.

## Directory Structure

*   `/1-product`: Brand identity, market strategy, and Ubiquitous Language (Glossary).
*   `/2-architecture`: System boundaries and domain-specific implementation specs (Frontend vs. Backend).
*   `/3-execution`: Milestones, Architecture Decision Records (ADRs), and feature specifications.
