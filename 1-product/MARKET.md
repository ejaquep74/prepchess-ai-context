# Market Strategy & Business Proposition: ChessGamma

## App Store & Marketing Positioning
*   **Tagline / Hero Text:** "Your Openings, no drama."
*   **Sub-headline:** "Tailor-made repertoires built to exploit human psychology."
*   **App Store Title Strategy:** "ChessGamma - Opening Trainer" or "ChessGamma: Tailored Openings"
*   **App Store Subtitle:** "Your Openings, no drama."

## Executive Summary
ChessGamma (internal project: PrepChess) is a next-generation SaaS platform designed to solve the critical flaw in modern chess preparation: the disconnect between strict engine evaluations (0.00) and practical human playability. By leveraging a massive database of positions enriched with multi-depth engine heuristics, the platform identifies "minefields"—positions where human opponents are statistically proven to blunder—and curates personalized repertoires that maximize practical winning chances over theoretical perfection.

## Target Audience
- **Core Demographic:** 1500 to 2200 Elo players on Lichess and Chess.com.
- **Pain Point:** Frustration with memorizing "perfect" engine lines that are impossible to execute practically, and losing to tricky sidelines. They need an automated grandmaster second that understands *human* tendencies.

## Competitive Landscape
| Competitor | Core Flaw | PrepChess Advantage |
|---|---|---|
| **Chessbook** | Relies on static surface-level crowd stats. Doesn't understand *why* lines are hard. | **Expectiminimax Backpropagation:** PrepChess tracks evaluation drop-offs (volatility $\sigma$) and evaluates the multi-objective utility of nodes to isolate hidden traps. |
| **OpeningFit / Chessaliz** | Suffers from small-sample hallucinations based on tiny user game logs. | **Global Statistical Anchoring:** Validates user style against a massive global matrix (currently PostgreSQL + Caffeine cache, scaling to RocksDB/Zobrist hashing), ensuring stability. |
| **Chessable** | Static, manual, and generalized. Forces memorization of broad theory. | **Dynamic Evolution Engine:** PrepChess dynamically patches and customizes repertoires based on live account metrics and psychological sliders. |

## Core Competitive Advantages (The Moat)

1. **The "Hollow Frontend" Security Architecture:** All proprietary math—including the Expectiminimax scoring coefficients, leaf node composite scores (combining mean eval, volatility, and sacrifice metrics), and probability tables—executes purely on the Java 21 backend. The React/Zustand UI is just a rendering shell, making the mathematical engine entirely un-scrapable by competitors.
2. **Dynamic "Style Sliders" Repertoire Generation:** Users don't just get a static tree. They use sliders (Originality, Trickiness, Chaos/Complexity, Aggression) to shape the repertoire to their exact psychological profile. The backend dynamically assigns weights to these parameters to generate a mathematically optimal, personalized tree.
3. **Synthetic Refutation Pipeline (Maia-3):** When human data is sparse (e.g., a rare 1-game blunder), the offline pipeline uses Maia-3 (Bounded Rationality Search) to synthesize realistic human defenses and engine refutations, filling in the gaps where competitors' data simply stops.
4. **The "Trap Lab" & Neuroscience Training:** Uses prediction error-driven learning (asking users to guess the blunder before showing the refutation) and contrastive visual encoding (Book Move vs. Blunder) coupled with an SM-2/Leitner spaced repetition engine.
5. **Microscopic Operational Cost:** Heavy tree resolution is cached via Caffeine for sub-15ms backpropagation. Scaling the static eval matrix to RocksDB using 64-bit Zobrist hashing will allow sub-millisecond lookups for billions of positions without active, expensive cloud-engine fees.

## Monetization Architecture (Freemium Funnel)

**Free Tier ("The Style Audit"):** 
- OAuth via Lichess/Chess.com. 
- Pulls the last 100 games, highlights top 3 "Sinking Ships" (losing lines), and maps a general style profile (e.g., Positional Grind vs. Sharp Chaos).

**Premium Tier ($7 - $9 / Month):** 
- Unlimited deep variation optimizations (up to depth 25).
- Automated multi-chapter PGN exports separating Mainlines, Errors, and Refutations.
- Unlimited access to the "Trap Lab" / Punishment Trainer.
- **Live Integration ("Repertoire Hole" Detector):** Silent 24/7 background syncs that scan recent games to detect where users stepped out of book, generating instant morning drill alerts to "plug the hole".
- **The "Evolution Engine":** Upload static Chessable PGNs and let the backend inject live, Elo-specific amateur traps and high-volatility sidelines.
- **Pre-Game Prep Dashboard:** Scrape an upcoming opponent's games and intersect their repertoire with the user's to generate a targeted 5-minute pre-game drill.

## Risk Management & Mitigation

- **IP Theft:** Mitigated by the "Hollow Frontend" and sanitized API payloads (sending UI badges like "High Sharpness" rather than raw utility coefficients). API requests are also heavily rate-limited (Bucket4j + Redis) to prevent scraping.
- **Database Bloat:** Current PostgreSQL + Caffeine strategy is highly efficient for session trees (~10MB for 50k nodes). The global 20-billion position matrix will use RocksDB + Zobrist hashes for 80% compression on cheap, bare-metal storage architecture.
- **Stockfish Compliance:** Stockfish is isolated as a backend oracle via standard UCI/ProcessBuilder commands, keeping the proprietary system safely out of GPLv3 copyleft scope.


## Expanded Competitive Landscape
| Competitor | Core Flaw | PrepChess Advantage |
|---|---|---|
| **WhyThisMove** | Focuses on static move-by-move move explanation without personalized repertoire generation or opponent psychology. | **Psychological Tailoring:** Generates trees that exploit opponent blunders and align with user style. |
| **Chessprep.io** | Traditional line builder lacking deep practical human evaluation and synthetic blunder generation. | **Expectiminimax + Maia-3:** Solves sparse human data with synthesized refutations. |
| **Chessline** | Basic visual exploration without volatility metrics or automated repertoire repair. | **Continuous Evolution:** Live background syncing to plug repertoire holes automatically. |

## Proposed Go-To-Market & Pricing [PROPOSED GTM]
*   **Target Pricing:** Freemium conversion targeting $10 - $12 USD/month subscription (directly challenging Chessable's pricing tier).
*   **B2B Coach Ambassador Program:** Direct outreach to chess coaches on Lichess/Chess.com offering free premium access for coaches plus up to 20 students to drive organic adoption.
*   **Precalculated Foundation Trees:** Precomputing ~100 core master openings (covering 90% of typical amateur responses) ensures zero-latency client loads, while reserving cloud infrastructure for on-demand deep subvariant calculations.
