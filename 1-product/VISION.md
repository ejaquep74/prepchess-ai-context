# Product Vision: ChessGamma (Internal: PrepChess)

## Brand Identity & Naming
*   **Internal Project Name:** PrepChess
*   **Public Market Name:** ChessGamma
*   **Slogan:** "Your Openings, no drama."
*   **Core Value Proposition:** Stop playing like a cold machine. ChessGamma generates tailor-made opening repertoires to exploit human psychology and practical advantages.

## The Grandmaster Secret: Psychological Asymmetry
Computers calculate without a heartbeat, without clock panic, and without fatigue. Humans don't.

The assumption that Grandmasters simply memorize Stockfish's top choices is an amateur myth. From Emanuel Lasker and Garry Kasparov to Magnus Carlsen and Daniil Dubov, elite champions prepare by **funneling games into their favorite pawn skeletons** and steering opponents into high-friction tactical minefields where the opponent bears the cognitive burden of defense.

ChessGamma bridges the gap between engine truth and practical human victory—giving club players the psychological preparation tools previously reserved for elite Grandmaster teams.

## The Mascot: Gamma (The Wry Tactical Co-Pilot)
To provide a friendly, empowering user experience, the application features a companion mascot named **Gamma**:
* **Role:** The user-facing "Psychology-Bot" co-pilot who translates complex Expectiminimax math and human blunder distributions into actionable, human advice.
* **Archetype:** A calm, hyper-competent tactical co-pilot whispering secret human intelligence in your ear (inspired by *JARVIS with dry chess wit*).
* **Visuals:** Sleek, compact cyber-companion with reactive LED digital eyes (inspired by *EVE / Astro Bot*).
* **Core Function:** Delivers X-Ray audits, draws synchronized arrows for tactical plans, and guides spaced-repetition drills with zero drama.
* **Persona & Dialogue Specification:** See **[VISION-MASCOT.md](file:///home/ejaque/projects/prepchess/prepchess-ai-context/1-product/VISION-MASCOT.md)** for the complete personality rules, visual interaction design, and system prompt dialogue library.

## The "Practical Eval" Metric
Instead of displaying a standard "Engine Eval", the most prominent metric in the UX is the **Practical Eval** (or **Human Eval**). This metric represents the backpropagated expected evaluation of an ultra-leaf node, mathematically factoring in the high probability of human opponents making mistakes. It visually contrasts with the standard engine evaluation to prove the immediate value of playing "tricky" human lines.

## The "Hollow Frontend" & Data Moat
While the user experiences a friendly, interactive frontend guided by Gamma, the actual intelligence (Expectiminimax backpropagation, multi-objective utility scoring, volatility tracking) remains strictly locked in the Java 21 backend. This ensures the global position matrix and scoring algorithms cannot be reverse-engineered or scraped.

## Product Loop (The ChessGamma Freemium Funnel)
1.  **The Style Audit:** OAuth sync pulls recent games, Gamma highlights "Sinking Ships" and identifies the user's style.
2.  **The Fitting:** Users adjust psychological sliders (Chaos, Aggression, Trickiness) to tailor their new repertoire.
3.  **The Trap Lab:** Gamma guides users through spaced-repetition tactical drills based specifically on their tailored lines.
4.  **Live Evolution:** Gamma continuously monitors live Lichess/Chess.com games to patch "seams" and "repertoire holes" automatically.


## The Trap Lab & Pattern Training [PROPOSED TRAINING FEATURE]
Gamma guides users through spaced-repetition tactical drills. This includes **Counter-Example Training**, where users learn the subtleties of an idea by being shown a position where a typical maneuver works, contrasted directly against a similar position where it fails (due to minor pawn structure or square control differences).

## Coach Integration & Ecosystem [PROPOSED ECOSYSTEM]
* **Coach Mode:** Chess coaches can integrate into the loop to track their students' progress in learning specific variations, typical errors, and structural proficiency.
* **Secret Weapons Tracker:** A progress bar tracking the user's proficiency with new, rare sub-variations. Once the user hits 80% mastery in the spaced-repetition deck, the variation is flagged as "Ready for Online Play."

## User Personalization & Sliders [PROPOSED FEATURE]
In addition to Human Eval and Sacrifices, the user has access to sliders to shape their repertoire recommendations:
* **Preferred Pawn Structures:** Users select up to 5 typical structures they excel in, weighting the engine's choice towards those midgame skeletons.
* **Surprise Value:** Ranks lines based on cumulative probabilities of occurrence, finding rare lines with high win ratios.
* **Memorization Difficulty:** Calculates the raw branching factor and node count required to safely learn a line.

## Visual UX Enhancements [PROPOSED UX]
* **Clock Time Estimation:** The UI estimates the time on the clock for both players at any given node, parsed from Lichess PGN timestamps.
* **Heatmaps:** Shows a heatmap overlay of the most visited moves and errors, guiding the user's study focus.
* **Node Graph Visualization (ALTERNATIVE IDEA):** While the primary focus remains on traditional PGN text, an interactive D3 node-graph may be added later as an alternative visualization, where circles represent moves (sized by popularity), line thickness represents forced moves, and colors represent the Human Eval score.


## Advanced Repertoire Metrics [PROPOSED METRIC]
*   **Repertoire Coverage:** The sum of cumulative move probabilities selected in the user's repertoire. Quantifies what fraction of real-world opponent lines are accounted for.
*   **Opponent Memory Load:** Reversing the coverage calculation against the opponent: how many moves an opponent must memorize to achieve the same coverage against the user's repertoire. A high opponent memory load indicates a repertoire that is difficult to face practically.

## Viral Community Features & "The IKEA Effect" [PROPOSED COMMUNITY FEATURE]
To drive authentic viral sharing, gamification and leaderboards must reward the player's real-world execution rather than purely theoretical algorithmic settings:
*   **The "Giant Killer" Board:** Ranks the largest Elo gap defeated in verified live games using a user's customized sideline (e.g., "1400 defeats 1850 in 14 moves using custom Vienna Trap").
*   **The "Community Gauntlet":** A shareable interactive challenge link where users test their custom repertoire against the community. Tracks the survival rate (e.g., "Only 12% of challengers survived past move 15").
*   **The "Trending Novelty" Index:** Allows users to publish high-win-rate, low-memory sidelines to a public lab. Displays crowdsourced live win rates across everyone playing the user's creation.

## Training & UX Enhancements [PROPOSED TRAINING FEATURE]
*   **Guess the Opponent's Move/Blunder:** Interactive review mode where users anticipate the opponent's most probable mistake (and test if they can refute it).
*   **Transposition Path Inspector:** Identifies and groups disparate move orders converging on the identical `shortFEN`, highlighting where different paths lead to the same blunder or structural bottleneck.
*   **Concentric Circles Sunburst View [ALTERNATIVE IDEA]:** An alternative visual representation displaying the repertoire as concentric circles (sunburst style), overlaying red dots for tactical mistakes and blue dots for sacrifice opportunities to highlight move density.


## Deep Player Identity: "Repertoire DNA" [PROPOSED FEATURE]
To create emotional ownership over their repertoire, users see an interactive reflection of their chess personality:
* **Style Spider Charts:** Visual axes mapping *Chaos Tolerance* (unbalanced material/sacrifices), *Structural Purity* (closed maneuvering vs. shattered pawns), *Initiative Bias* (willingness to sacrifice objective eval for attack), and *Endgame Affinity* (tendency to force early queen trades).
* **The "Hero Alignment" (GM Doppelgänger):** Identifies Grandmaster alignment based on generated lines (e.g., *"Your White repertoire is 74% Mikhail Tal and 26% Daniil Dubov"*), biasing example games toward those historical models.
* **Custom Naming Rights:** When adopting a rare sub-variation played fewer than 50 times in master archives, users can name the line inside their app (e.g., *"The Chicago Attack"*), branding all drills and stats.

## Semantic Example Lines & "My Brilliancies" [PROPOSED FEATURE]
Moves are contextualized with hyper-specific semantic tags (`is-sacrifice`, `is-error`, `pawn-break`, `is-iqp`, `king-attack`):
* **Tri-Level Example Tabs:** When exploring an opening idea, users can view three tabs:
  1. *Master Games:* Classical model executions (e.g., Kasparov).
  2. *Community Games:* How club players (1800 Elo) navigate the line.
  3. *My Games:* Scans linked Lichess/Chess.com history to surface the user's past successful executions of this idea.
* **Side-by-Side Repertoire Comparison:** Contrast example games between two competing repertoire options (e.g., French Defense vs. Caro-Kann IQP) before committing to drilling them.

## Bridging the Middlegame Gap [PROPOSED FEATURE]
Overcoming the "Opening-to-Middlegame Cliff":
* **Tabiya Takeover (Targeted Sparring Mode):** Skip the first 10-15 moves and drop instantly into the Move 20 Tabiya against an Elo-calibrated bot to practice converting the resulting positional blueprint.
* **Middlegame Mission Cards:** At the end of each generated opening line, Gamma presents a 3-bullet tactical checklist (e.g., *1. Primary Pawn Break: Prepare ...c5 before move 25; 2. Key Relocation: Route Nf6 via d7 to c5 outpost; 3. Counterplay Alert: Watch for White's b4-b5 push*).
* **Pawn Skeleton Clustering:** Systematically steer both White and Black repertoire responses into shared universal pawn structures (e.g., funneling multiple lines into Isolated Queen's Pawn structures) to drastically compress the total concepts a user must master.

## Anti-Pattern Training & Counter-Examples [PROPOSED FEATURE]
Cures dogmatic autopilot play by testing tactical preconditions:
* **"The Poisoned Square" Drills:** Puzzles where the textbook positional move (e.g., planting a knight on a power square) is a catastrophic tactical blunder due to a missing defensive precondition.
* **"Spot the Difference" Mode:** Side-by-side comparison of Position A (where the power maneuver wins) versus Position B (where a tiny structural difference causes the same maneuver to lose).
* **The "Only-Move" Practical Burden:** Equal (0.00) positions evaluated by cognitive asymmetry: flagging positions where the opponent has only 1 survivable move while the user has 5 comfortable choices.

## Real-World Efficacy Tracking [PROPOSED FEATURE]
* **EV Leak Detector:** Continuously tracks the delta between the user's *Expected Move 20 Eval* and their *Actual Move 20 Eval* in live games, pinpointing the exact transition move where advantage was surrendered and auto-scheduling targeted drills.
* **Style Clash Scouting:** Pre-game opponent scouting comparing Repertoire DNA (e.g., Aggressive IQP vs. Solid Carlsbad) and surfacing model breaks against that specific profile.
