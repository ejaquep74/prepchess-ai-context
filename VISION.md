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
