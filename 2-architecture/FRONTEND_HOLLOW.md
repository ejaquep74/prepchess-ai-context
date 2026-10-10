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
