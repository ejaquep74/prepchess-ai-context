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
