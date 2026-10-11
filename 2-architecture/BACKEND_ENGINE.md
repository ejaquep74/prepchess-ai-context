# Backend Engine & Algorithmic Specifications

## 1. Leaf Node Composite Score ($U(n)$)

For every terminal leaf node $n$ at depth $D$ (up to move 25), the utility $U(n)$ is calculated via user-controlled slider weights $w$:

$U(n) = (w_{\mu} \cdot \mu(n)) + (w_{\sigma} \cdot \sigma(n)) + (w_{sac\_player} \cdot Sac_{player}(n)) - (w_{sac\_opp} \cdot Sac_{opp}(n))$

Where:
* **$\mu(n)$ (Mean Eval):** Normalized average engine evaluation across candidate moves from node $n$ (capped between -3.0 and +3.0).
* **$\sigma(n)$ (Volatility):** Standard deviation of evaluations across legal moves flowing out of node $n$. High $\sigma$ indicates tactical "minefields".
* **$Sac(n)$:** Continuous indicators (0.0 to 1.0) measuring material imbalance relative to starting material.

## 2. Expectiminimax Backpropagation

Tree evaluation flows bottom-up via Post-Order Depth-First Search (DFS):

1. **Player Nodes (MAX Decision):**
   $U(v) = \max_{a} ( U(child(v, a)) )$ across all legal moves $a$.
2. **Opponent Nodes (Expectation Decision):**
   $U(v) = \sum_{a} [ P(a | v) \cdot U(child(v, a)) ]$ across all opponent moves $a$.

Where $P(a | v) = (\text{Games with move } a) / (\text{Total games in position } v)$ based on database frequency filtering ($\ge 20$ games).

## 3. Synthetic Refutation Pipeline (Maia-3)
* **Sparse Data Handling:** When empirical game data lacks defensive continuations for rare 1-game blunders, the offline pipeline runs a modified **Maia-3 50-node Bounded Rationality Search**.
* **Purpose:** Synthesize realistic human defense lines and their punishments to patch missing empirical data.


## 4. MoveNode DB Schema Additions
* **ECO Codes:** Every `MoveNode` stores the ECO code of the opening being explored. This facilitates querying for transpositions by matching short FENs across different opening branches.
* **Granular Metric Storage:** Instead of only storing a static compound score, the DB stores the isolated metrics (`humanEval`, `sacrificePctg`, `stdDev`). This allows the frontend sliders to recalculate the compound metric on the fly.

## 5. Dynamic Exploration Depth (Ultra-Leaf)
Instead of capping tree exploration at a fixed arbitrary depth (e.g., 25 moves), the engine explores forward until the *cumulative probability* of reaching the node drops below a threshold (e.g., $< 0.8\%$), or until the absolute evaluation drops below 1.0 (indicating the end of a forced advantage line).

## 6. Hybrid Pattern Extraction Pipeline (Vectorization)
To categorize tactical motifs and structural heuristics without relying entirely on manual rules:
1. **Geometric Filtering:** The board is stripped of irrelevant pieces using `python-chess` or `ChessLib`, isolating the core tension (e.g., just the pawn structure and attacking knights).
2. **NNUE Vectorization:** The purified FEN is passed through a neural network (e.g., `ChessLM` or `jdart1/nnue`) to extract a multidimensional vector representing the position's "tactical DNA".
3. **Clustering:** Vectors are indexed into a vector database (`FAISS` or `Milvus`). This allows the system to instantly find mathematically similar positions for Counter-Example training, grouping positions with the same structural DNA even if the exact pieces differ.
4. **Maneuver Tracking:** The engine tracks and backpropagates highly effective piece routes (e.g., a knight maneuvering `f6-d4-f3`) and tags positions with specific heuristic attributes (`label:pawn-struct-carlsbad`, `attrib:center-control:0.85`).


## 7. Cross-Rating Elo Calibration [PROPOSED / EXPERIMENTAL]
*   **Time Control Adjustment:** Adjust Blitz move probabilities using linear regression / ML to mimic Rapid/Classical human decision distributions.
*   **Sparse 2500+ Projection:** Address sample scarcity at the 2500+ Elo tier (13M games vs. 160M games at 2200 Elo) by projecting the move probability drop-off curve from lower rating bands (2000, 2200) to adjust 2500+ estimations, while sourcing error refutations safely from high-eval 2200 games.

## 8. Leaf-at-Move-20 Pruning [PROPOSED - ALTERNATIVE EXPLORATION STRATEGY]
*   **Un-evaluated Branch Trimming:** When constructing trees up to move 20 using cloud/annotated evals, if a node before move 20 lacks children with evaluations, backpropagate and prune single-child predecessor chains. Ensures all backpropagated human evals originate from legitimate terminal evaluations.

## 9. Hybrid Maia Bounded Search [PROPOSED ENHANCEMENT]
*   **50-Node Bounded Rationality Search:** Construct a small 50-node candidate tree evaluated by Maia and tuned against empirical human blunder rates.
*   **Positional Heuristic Stabilization:** Evaluate average positional/material heuristics across 3–4 plies. When heuristic values stabilize, Maia selects lines that mimic human positional logic while avoiding catastrophic tactical blunders in rare branches where empirical game data is missing.


## 10. Move 20 Hybrid EV & Clock Burn Weighting [PROPOSED SPECIFICATION]
To evaluate practical human middlegame yield beyond raw move-12 engine scores:
* **The 25-Move Cap:** Restricts primary algorithmic exploration to moves 1–25, avoiding late-middlegame/endgame bloat and focusing where 80% of non-master games are decided.
* **Middlegame Yield (Moves 18–25):** Evaluates whether an opening sustains its positional advantage into the early middlegame.
* **Clock Burn Index:** Analyzes empirical online time-spent distributions per ply. Variations that mathematically force opponents to consume disproportionate clock time navigating complex defensive trees receive an Expected Value (EV) multiplier.

## 11. Differential Heatmapping & Sequential Pattern Mining [PROPOSED ALGORITHMIC PIPELINE]
To identify structural winning highways and key squares from the heuristic database:
* **Differential Occupancy Heatmapping:** Contrasts piece occupancy across winning game states ($\ge +1.5$) versus losing states ($\le -1.5$) to isolate statistically critical squares.
* **Winning Highways (PrefixSpan / N-grams):** Employs sequential pattern mining across move trees to isolate recurring piece maneuvers that exclusively correlate with advantage generation.
* **Actionable Rule Cards (Feature Importance):** Trains ML classifiers (XGBoost / Random Forest) on position heuristics to identify the primary failure point (e.g., lost king safety, passive rook) causing evaluation collapse.

## 12. Counter-Example & Anti-Pattern Isolation [PROPOSED ALGORITHM]
To isolate tactical exceptions for training:
* **Heuristic Contradiction Query:** Detects positions where structural heuristic scores (e.g., Outpost Score) are high but engine evaluation drops sharply ($0.00 \to -4.0$).
* **Popular Blunder Filter:** Identifies positions where an intuitive power maneuver is the most frequent human candidate move but fails to a concrete tactical refutation.
