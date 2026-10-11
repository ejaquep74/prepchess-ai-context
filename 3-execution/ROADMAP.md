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

## MVP 1.5: The Interactive Pilot (Internal Dogfooding)
**Objective:** Deliver an end-to-end playable vertical slice on curated high-asymmetry example lines (e.g., Vienna Gambit, Smith-Morra, Fried Liver), proving the practical value of blunder exploitation and tactical sacrifices without external OAuth or billing dependencies.

* **Move Table Telemetry & Visual Indicators:**
  * Add visual icons in the explorer table for **Tactical Sacrifices** (🚨 / ⚡) and **Opponent Errors/Blunders** (⚠️ / 💥).
  * Expose quick contextual action triggers ("Errors" and "Sacrifices" action buttons) on any evaluated position within example lines.
* **Dedicated Asymmetry Views (Errors & Sacrifices):**
  * Clicking "Errors" or "Sacrifices" routes to a dedicated **Tactical View**.
  * **Explore Mode (Default):**
    * Inspect the branch tree of common opponent blunders or candidate player sacrifices line-by-line.
    * Real-time visual board arrows and Gamma co-pilot commentary highlighting why human opponents fail here.
  * **Training Mode (Interactive Sparring):**
    * Seamless toggle from Explore to Training on the same branch.
    * Automatically pauses the board 1–2 plies before the critical inflection point.
    * **The Challenge:** The user must guess the most common human blunder or find the tactical sacrifice and punishing refutation on the board.
    * **Feedback Loop:** Gamma overlay provides instant, non-judgmental evaluation of the move ("no drama").
* **Deliverable:** A fully interactive web prototype loaded with 5–10 curated example repertoires, ready for internal testing and friendly chess coach reviews.

---

## MVP 2: The Core Product & "Aha!" Onboarding (Private Beta)
**Objective:** Build the "Hollow Frontend," protect the IP, and implement the high-conversion onboarding flow to hook early testers (1600–2200 Elo).

* **Infrastructure & Security:**
  * Migrate from local H2 to PostgreSQL with batch inserts.
  * Implement Caffeine in-memory session caching for <15ms backpropagation.
  * Secure the API layer (JWT authentication, rate limiting, and sanitized payload DTOs).
* **Frontend (React + Vite):**
  * Build the interactive chessboard UI using `chessops` and `chessground`.
  * Wire up the debounced user-facing Style Sliders (Complexity, Human Eval, Sacrifices), backed by server-side volatility ($\sigma$) calculations returning sanitized UI badges per the Hollow Frontend constraint.
  * Highlight sacrifice indicators (🚨 / ⚡) dynamically in the move tree.
* **Growth & Onboarding:**
  * Build the **Repertoire X-Ray Tool**: Allow users to input their Lichess/Chess.com username to instantly run an automated audit on their recent games.
  * Render the "Contrast Cards" (Stockfish Eval vs. PrepChess Practical Risk) to deliver instant "Aha!" value.
  * **The Monetization Gate:** Implement Stripe/billing integration: Free X-Ray audit surfaces the top 3 "Sinking Ships" (leaks), with a one-click paywall conversion ($9–$12/mo) to unlock Gamma's custom fix and drill deck.

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

## MVP 4: Pawn Skeleton Clustering & Repertoire Harmonization [PROPOSED SPECIFICATION]
**Objective:** Slash memorization overhead by systematically funneling the player's White and Black repertoires into shared universal pawn structures (e.g., IQP, Carlsbad, Hedgehog).

* **Pawn Skeleton Classifier:**
  * Categorize all tree branches beyond move 10 by their underlying pawn skeleton.
* **Tree Optimizer:**
  * Algorithmic weighting steering candidate lines across both colors to funnel games into the user's preferred structures, cutting required study concepts by 50%.
* **Unified Middlegame Transition:**
  * Generate shared strategic guidelines showing how identical middlegame plans apply across ostensibly different opening branches.

---

## MVP 5: Opponent Memory Load & Coverage Engine [PROPOSED SPECIFICATION]
**Objective:** Quantify repertoire completeness and practical match difficulty, providing tangible proof of value to the user.

* **Repertoire Coverage Calculator:**
  * Sum cumulative move probabilities across selected lines to show what percentage of real-world opponent play is accounted for.
* **Opponent Memory Load Engine:**
  * Invert coverage calculations against the opponent to measure the exact number of distinct moves an opponent must memorize to achieve matching coverage.
* **Explorer Dashboard Integration:**
  * Expose real-time Coverage % and Opponent Memory Load badges directly in the `prepchess-ui` tree explorer.

---

## MVP 6: Cross-Rating Elo Calibration Pipeline [PROPOSED ALGORITHMIC PIPELINE]
**Objective:** Eliminate sample-size starvation on deep master variations and mathematically calibrate Blitz data to simulate Rapid play.

* **Time-Control Regression Model:**
  * Statistically adjust high-volume Blitz move probabilities using regression models to mimic Rapid/Classical human decision distributions.
* **Cross-Tier Projection Model:**
  * Use the rich 2200 Elo dataset (160M games) to project reliable probability drop-off curves for sparse 2500+ master nodes (13M games).
* **Blunder Refutation Filter:**
  * Source blunder refutations safely from high-eval 2200 games to patch missing defensive lines in deep master variations without requiring billions of expensive synthetic engine rollouts.

---

## Proposed MVP Concepts [UNDER EVALUATION]

### MVP Proposal: Advanced AI Extraction & Pattern Training (Post-Beta)
* **Objective:** Replace hardcoded engine rules with vectorized AI pattern recognition and deliver the ultimate "Counter-Example" training loop to users.
* **Key Components:**
  * **Vector Database Integration:** Implement the Hybrid Vector pipeline (Geometric Filter -> NNUE Vector -> FAISS/Milvus) to group positions by tactical DNA.
  * **Batch AI Generation:** Use batch LLM processing (e.g., Gemini Pro) across ECO codes with >2000 master games to compile structured theory facts (breaks, maneuvers, outposts).
  * **The Trap Lab Expansion:** Build Counter-Example drills (poisoned square exceptions) and Secret Weapons tracker (80% mastery progress bar).
  * **Contextual Sparring:** Tabiya Takeover (sparring from move 20 against AI bots), Middlegame Mission Cards, and EV Leak Detector.
  * **Identity & Growth:** Repertoire DNA spider charts, B2B Coach Ambassador program, and viral Community Gauntlet links.

### MVP Proposal: Clock Burn Index & In-Game Time Simulator [DEFERRED / DOUBTFUL ROI]
* **Objective:** Parse Lichess PGN move timestamps to display estimated clock times and give an Expected Value (EV) boost to lines that empirically force opponents into time trouble.
* **Feasibility & ROI Assessment:** Considered **too complicated to implement** at this stage. Storing granular per-move clock timestamps across hundreds of millions of moves in the database creates massive storage bloat and overhead, while the practical return on investment (ROI) is doubtful compared to core evaluation and repertoire features.

### MVP Proposal: Study Heatmap Overlay [PROPOSED UX]
* **Objective:** Render a visual heatmap overlay across the move tree and board to highlight heavily drilled lines versus unpracticed blind spots, streamlining daily training decisions.

### MVP Proposal: Sequential Pattern Mining for "Winning Highways" [PROPOSED ALGORITHM]
* **Objective:** Apply sequential pattern mining (PrefixSpan / N-grams) across the 500M-move dataset to isolate recurring piece maneuver sequences (e.g., `Nb1-d2-f1-g3`) that mathematically correlate with winning outcomes, automatically feeding coach arrows.