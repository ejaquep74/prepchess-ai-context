# Product Vision: ChessGamma (Internal: PrepChess)

## Brand Identity & Naming
*   **Internal Project Name:** PrepChess
*   **Public Market Name:** ChessGamma
*   **Slogan:** "Your Openings, no drama."
*   **Core Value Proposition:** Stop playing like a cold machine. ChessGamma generates tailor-made opening repertoires to exploit human psychology and practical advantages.

## The Mascot: Taylor the Assistant
To provide a friendly, interactive user experience alongside the powerful ChessGamma engine, the application features a mascot named **Taylor**. 

**Concept:**
While the "Gamma" engine is an advanced AI, Taylor acts as the user-facing "Psychology-Bot" expert. While Stockfish represents a cold calculator spitting out 0.00 evaluations, Taylor is an expressive, sleek tech assistant that focuses entirely on human psychology.
*   **Visuals (The Tape Measure):** Taylor wears a yellow "tailor's tape" sash. Why? Because Taylor is here to help you generate **tailor-made repertoires**. It bridges the gap between raw AI power and highly customized, human-centric learning.
*   **Personality:** Taylor specializes in analyzing *human* behavior. Instead of providing dry computer lines, Taylor highlights human blunders, saying things like, *"The Gamma engine calls this equal, but my sensors show humans blunder here 40% of the time!"*
*   **Interactive Role:** Taylor acts as the voice for the AI-Generated Plan Explanations, drawing arrows on the board in real-time, and dropping into the user's inbox to notify them of newly discovered "Repertoire Holes" from their overnight games.

## The "Practical Eval" Metric
Instead of displaying a standard "Engine Eval", the most prominent metric in the UX is the **Practical Eval** (or **Human Eval**). This metric represents the backpropagated expected evaluation of an ultra-leaf node, mathematically factoring in the high probability of human opponents making mistakes. It visually contrasts with the standard engine evaluation to prove the immediate value of playing "tricky" human lines.

## The "Hollow Frontend" & Data Moat
While the user experiences a friendly, interactive frontend guided by Taylor, the actual intelligence (Expectiminimax backpropagation, multi-objective utility scoring, volatility tracking) remains strictly locked in the Java 21 backend. This ensures the global position matrix and scoring algorithms cannot be reverse-engineered or scraped.

## Product Loop (The ChessGamma Freemium Funnel)
1.  **The Style Audit:** OAuth sync pulls recent games, Taylor highlights "Sinking Ships" and identifies the user's style.
2.  **The Fitting:** Users adjust psychological sliders (Chaos, Aggression, Trickiness) to tailor their new repertoire.
3.  **The Trap Lab:** Taylor guides users through spaced-repetition tactical drills based specifically on their tailored lines.
4.  **Live Evolution:** Taylor continuously monitors live Lichess/Chess.com games to patch "seams" and "repertoire holes" automatically.


## The Trap Lab & Pattern Training 
Taylor guides users through spaced-repetition tactical drills. This includes **Counter-Example Training**, where users learn the subtleties of an idea by being shown a position where a typical maneuver works, contrasted directly against a similar position where it fails (due to minor pawn structure or square control differences).

## Coach Integration & Ecosystem
* **Coach Mode:** Chess coaches can integrate into the loop to track their students' progress in learning specific variations, typical errors, and structural proficiency.
* **Secret Weapons Tracker:** A progress bar tracking the user's proficiency with new, rare sub-variations. Once the user hits 80% mastery in the spaced-repetition deck, the variation is flagged as "Ready for Online Play."

## User Personalization & Sliders
In addition to Human Eval and Sacrifices, the user has access to sliders to shape their repertoire recommendations:
* **Preferred Pawn Structures:** Users select up to 5 typical structures they excel in, weighting the engine's choice towards those midgame skeletons.
* **Surprise Value:** Ranks lines based on cumulative probabilities of occurrence, finding rare lines with high win ratios.
* **Memorization Difficulty:** Calculates the raw branching factor and node count required to safely learn a line.

## Visual UX Enhancements
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
