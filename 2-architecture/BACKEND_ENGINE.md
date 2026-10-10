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
