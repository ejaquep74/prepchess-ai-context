# Domain Dictionary (Ubiquitous Language)

To prevent AI hallucination and developer misalignment, all documentation, variable names, and code structures across the ecosystem MUST adhere strictly to the following terminology:

### Engine & Evaluation Concepts
*   **Practical Human Eval (or Practical Eval):** The core metric distinguishing PrepChess. The backpropagated expected evaluation of a leaf node factoring in the probability of human mistakes.
*   **Composite Score ($U(n)$):** The internal mathematical utility score of a node combining mean evaluation, volatility, and sacrifices.
*   **Volatility ($\sigma$):** The standard deviation of evaluations across legal moves flowing out of a node. High volatility implies a tactical minefield. Do not use the term "Complexity".

### Repertoire Concepts
*   **Sinking Ship / Repertoire Hole:** A line where the user's historical data indicates a high probability of loss or a sudden evaluation drop-off.
*   **Minefield:** A position with high Volatility ($\sigma$) where one mistake leads to severe punishment. 
*   **Tightrope:** A position where Stockfish evaluates `0.00`, but only if the human plays 15 consecutive perfect moves. PrepChess penalizes tightropes.

### System Components
*   **Hollow Frontend:** The React UI architecture. The UI performs NO repertoire math or evaluation. It only renders sanitized API data.
*   **Taylor:** The user-facing mascot and "Psychology-Bot" that guides users.
