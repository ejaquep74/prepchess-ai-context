# Frontend "Hollow" Architecture Constraints

## 1. Security & IP Isolation
* **Proprietary Isolation:** The utility function $U(n)$, leaf metrics ($\mu$, $\sigma$), and probability tables $P(a | v)$ remain strictly on the Java backend.
* **Sanitized API Payloads:** Network responses return only boolean flags and presentation labels (e.g., `{"recommended": true, "badge": "High Sharpness"}`), preventing reverse-engineering of scoring coefficients.
* **Rate Limiting:** API requests are throttled (e.g., 30 recalculations/minute per user) to prevent data scraping.

## 2. UI Execution Rules
* **No Repertoire Math:** The React UI must NEVER contain logic related to calculating utility, generating tree stats, Expectiminimax backpropagation, or move volatility.
* **Presentation Only:** The client's sole responsibility is to render the chess board (`chessground`), handle user interactions (`chessops` for basic localized legality), and display the JSON responses received from the backend API.
* **API Schema Dependency:** The exact shape of the JSON consumed by the frontend is defined entirely by the `opening-explorer` backend (via generated Swagger/OpenAPI). The frontend must align its TypeScript interfaces to that external schema.

## 3. Neuroscience-Backed Training UI
* **Prediction Error-Driven Learning:** The UI hides blunder continuations initially, prompting the user: *"Predict the opponent's common mistake here"* before showing the refutation.
* **Contrastive Visual Encoding:** Side-by-side rendering comparing the **Book Move** vs. the **Blunder/Refutation**.
* **Interleaved Active Recall:** Training decks mix Defensive Awareness and Offensive Refutation using an SM-2 / Leitner Spaced Repetition engine.


## 4. Proposed Frontend Technology Stack [PROPOSED / UNDER EVALUATION]
> **Status:** Proposed Target Stack. Currently under evaluation for `prepchess-ui`.
The "Hollow Frontend" evaluates the following tools to handle chess logic and presentation without breaking the architectural constraints:
* **Base Framework:** React + Vite, inspired by the GPL-3 `OpeningTree` codebase architecture.
* **Chess Logic:** `chess.js` handles move validation and localized board logic.
* **Board Rendering:** `react-chessboard` renders the FEN and graphical overlays (arrows/squares).
* **PGN & Annotation Parsing (PENDING-REVIEW):** `@mliebelt/pgn-parser` is being evaluated for parsing backend-generated PGNs. Unlike `chess.js`, it natively builds an AST supporting deeply nested variations, comments, NAG evaluation symbols (`!`, `?`), and Lichess-style graphical arrow tags (`%cal`, `%csl`). This is a delicate technical decision.
* **Graph Rendering (ALTERNATIVE IDEA):** If the Node Graph approach is adopted, `react-d3-tree` could be used to render the interactive node-graph alternative to standard PGN notation. The tree would dynamically load a vision-ahead of 4 moves while keeping a strict depth boundary (e.g., 16 moves) to prevent browser freezing.
