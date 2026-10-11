# Domain Dictionary (Ubiquitous Language)

To prevent AI hallucination and developer misalignment, all documentation, variable names, and code structures across the ecosystem MUST adhere strictly to the following terminology:

### Engine & Evaluation Concepts
*   **Practical Human Eval (or Practical Eval):** The core metric distinguishing PrepChess. The backpropagated expected evaluation of a leaf node factoring in the probability of human mistakes.
*   **Composite Score ($U(n)$):** The internal mathematical utility score of a node combining mean evaluation, volatility, and sacrifices.
*   **Volatility ($\sigma$) / Complexity:** The standard deviation of evaluations across legal moves flowing out of a node. High volatility implies a tactical minefield. **Convention:** In backend engine code and algorithmic specifications, use **Volatility ($\sigma$)**. In frontend user-facing UI and marketing sliders, use **Complexity** (as it is the natural term in chess culture).

### Repertoire Concepts
*   **Sinking Ship / Repertoire Hole:** A line where the user's historical data indicates a high probability of loss or a sudden evaluation drop-off.
*   **Minefield:** A position with high Volatility ($\sigma$) where one mistake leads to severe punishment. 
*   **Tightrope:** A position where Stockfish evaluates `0.00`, but only if the human plays 15 consecutive perfect moves. PrepChess penalizes tightropes.
*   **Main Line (ML) vs. Deep Analysis (DA):** The distinction in how the engine explores the tree. *Main Lines* are standard user-explored paths, whereas *Deep Analysis* nodes are generated asynchronously to calculate deeper tactical metrics.
*   **Transposition:** When the identical board position (FEN) is reached via a different sequence of moves. The system strictly deduplicates these (Cross-Branch Transposition Pruning) by referencing the original evaluated node to prevent exponential tree explosion.

### System Components
*   **Hollow Frontend:** The React UI architecture. The UI performs NO repertoire math or evaluation. It only renders sanitized API data.
*   **Gamma:** The user-facing mascot and "Wry Tactical Co-Pilot" (see [VISION-MASCOT.md](file:///home/ejaque/projects/prepchess/prepchess-ai-context/1-product/VISION-MASCOT.md)). An alert, non-judgmental companion bot translating engine data into human psychological insights.
*   **Interactive Plan Explanations:** An AI-generated coach's voice synchronized with visual board indicators (arrows, highlighted outposts) to explain the structural goals of a position, rather than just listing raw moves.

*   **Rare Pawn Structure:** A pawn skeleton that breaks common conventions (e.g., an early atypical pawn break in a Hedgehog) but holds statistical significance in the user's games.
*   **Hybrid Pattern Vector:** A mathematical abstraction of a position's tension and structure, extracted by neutralizing irrelevant pieces and processing through an NNUE network. Used for positional clustering.
*   **Compound Metric:** The final weighted score of a node calculated dynamically on the fly, composed of isolated metrics (Human Eval, Sacrifice Pctg, Std Dev, Surprise, Memorization Difficulty).
*   **Counter-Example Training:** A learning mode where the user is shown a typical maneuver (e.g., `Nfe5`) in a position where it fails (due to structural differences) immediately after seeing where it succeeds.
*   **Ultra-leaf threshold:** The depth expansion stopping condition based on cumulative probability (e.g., $< 0.8\%$ chance to reach) rather than a fixed node depth.
*   **Maneuver Route:** The tracked sequential path of a critically active piece (e.g., `f6-d4-f3`), saved for pattern training.

*   **Repertoire Coverage:** The sum of cumulative move probabilities selected in a user's repertoire, indicating the mathematical proportion of opponent lines accounted for.
*   **Opponent Memory Load:** The total number of distinct moves an opponent must memorize to achieve the same coverage against the user's repertoire.
*   **Metadata Injection:** The architectural pattern where structured chess facts (pawn breaks, maneuvers) and engine evaluations are injected into an LLM prompt so the model acts strictly as a natural-language commentator without tactical hallucinations.
*   **The Community Gauntlet:** A shareable challenge mode testing how many human players survive a customized repertoire past a move threshold.
*   **Cross-Rating Calibration:** Mathematical projection adjusting blitz play and high-volume rating bands (e.g. 2200) to estimate probability distributions in sparse bands (2500+).

*   **Repertoire DNA:** A player's visual style profile across key operational axes: Chaos Tolerance, Structural Purity, Initiative Bias, and Endgame Affinity.
*   **Move 20 Hybrid EV:** An opening utility metric factoring sustained middlegame engine yield (moves 18–25), Maia human volatility, and the Clock Burn Index.
*   **Clock Burn Index:** A metric boosting candidate variations based on empirical data proving they force human opponents into deep time expenditure.
*   **Tabiya Takeover:** A targeted sparring mode where the user skips initial moves and plays directly from the Move 20 position against an Elo-calibrated AI bot.
*   **Middlegame Mission Card:** A 3-bullet checklist generated at the end of an opening line detailing immediate strategic objectives (pawn break, piece relocation, opponent counterplay).
*   **Pawn Skeleton Clustering:** An algorithmic optimization steering a player's White and Black repertoires toward shared pawn structures to minimize memorization load.
*   **Differential Heatmapping:** A mathematical comparison of piece occupancy between winning (+1.5) and losing (-1.5) states to isolate true key squares.
*   **The Poisoned Square Drill:** A counter-example puzzle where an intuitively attractive positional move loses to a concrete tactical refutation.
*   **Spot the Difference Mode:** A training format contrasting two nearly identical positions where a subtle structural shift determines whether a power move succeeds or fails.
*   **EV Leak Detector:** An automated audit comparing a user's theoretical Move 20 EV against their actual live game Move 20 evaluation.
