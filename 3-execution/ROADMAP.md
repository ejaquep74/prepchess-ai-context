# ROADMAP.md — PrepChess Product Development Stages

> **Status:** Active Planning Document  
> **Goal:** Take PrepChess from a mathematical prototype to a highly defensible, interactive chess training platform.

---

## MVP 1: Proof of Math (The Internal Prototype)
**Objective:** Validate the Expectiminimax algorithm and prove that the "Practical Human Eval" framework successfully identifies tactical minefields that standard engines miss.

* **Backend (Java 21 / Spring Boot):**
  * Implement the foundational Expectiminimax post-order DFS algorithm.
  * Integrate the `ProcessBuilder` Stockfish wrapper to calculate leaf-node Mean Eval (μ) and Standard Deviation / Volatility (σ).
  * Calculate opponent move probabilities P(move) using an initial ingest of a Lichess/Master database.
  * Implement the $U(n)$ utility function with hardcoded weights.
* **Deliverable:** A local console or basic API output proving that PrepChess recommends demonstrably different (and practically safer/sharper) lines than standard Stockfish `+0.00` outputs.

---

## MVP 2: The Core Product & "Aha!" Onboarding (Private Beta)
**Objective:** Build the "Hollow Frontend," protect the IP, and implement the high-conversion onboarding flow to hook early testers (1600–2200 Elo).

* **Infrastructure & Security:**
  * Migrate from local H2 to PostgreSQL with batch inserts.
  * Implement Caffeine in-memory session caching for <15ms backpropagation.
  * Secure the API layer (JWT authentication, rate limiting, and sanitized payload DTOs).
* **Frontend (React + Vite):**
  * Build the interactive chessboard UI using `chessops` and `chessground`.
  * Wire up the debounced Style Sliders (Complexity, Human Eval, Sacrifices).
  * Highlight sacrifice indicators (🚨 / ⚡) dynamically in the move tree.
* **Growth & Onboarding:**
  * Build the **Repertoire X-Ray Tool**: Allow users to input their Lichess/Chess.com username to instantly run an automated audit on their recent games.
  * Render the "Contrast Cards" (Stockfish Eval vs. PrepChess Practical Risk) to deliver instant value without a paywall.

---

## MVP 3: Synthesis Pipeline & Sparring Loop (Public Beta)
**Objective:** Launch the premium training features that lock users into the PrepChess ecosystem and defend against competitors.

* **The Offline Batch Pipeline (Maia-3):**
  * Move the modified Maia-3 bounded rationality search strictly to a backend batch process.
  * Synthesize human-like defensive lines for rare blunders and save the tactical punishments to the database (`is_synthetic=true`).
* **Intelligent Exporting:**
  * Implement the 20+ game frequency filter for the "Lean Mainline."
  * Allow users to export this lean repertoire to Lichess Studies or as PGN files with custom embedded annotations (NAGs and graphical arrows).
* **The "Walled Garden" Sparring Mode:**
  * Lock the "Mistake / Error" chapters inside the PrepChess web application.
  * Build the Interactive Sparring Mode where users play against the synthesized Maia-3 refutations natively in the browser.
  * **AI Interactive Plans:** Implement the "Coach's Voice" feature where an LLM generates structured JSON to explain tactical plans while simultaneously rendering visual arrows and square highlights (e.g., outposts) on the frontend board.
* **Automated Sync:**
  * Poll the Lichess/Chess.com APIs weekly to cross-reference user games against their PrepChess tree, automatically flagging deviations and missed tactical refutations.


---

## MVP 4: Advanced AI Extraction & Pattern Training (Post-Beta)
**Objective:** Replace hardcoded engine rules with vectorized AI pattern recognition and deliver the ultimate "Counter-Example" training loop to users.

* **Vector Database Integration:**
  * Implement the Hybrid Vector pipeline (Geometric Filter -> NNUE Vector -> FAISS/Milvus).
  * Automatically group similar pawn structures and maneuver routes (e.g., `f6-d4-f3`).
* **Batch AI Generation:**
  * Use batch LLM processing (e.g., Gemini Pro) to parse all ECO codes with >2000 master games.
  * Generate a structured JSON database of standard maneuvers, key squares, and typical pawn breaks for every major structure.
* **The "Trap Lab" Expansion:**
  * Build the "Counter-Example" training UI: Show a user where a move works, then immediately show a mathematically similar vector-position where the same move is a blunder.
  * Build the "Secret Weapons" tracker UI, unlocking new variations for live play once the user reaches 80% mastery in spaced repetition.