# SPEC-02: Dynamic Weighted Metrics & On-Demand Tree Generation

> **Status:** Specification (MVP 2 Core Backend & API)  
> **Target Component:** `opening-explorer` (Java 21 / Spring Boot) & `prepchess-ui` (React)

---

## 1. Context & Problem Statement
Previously, the repertoire tree was built upon application startup with static metric calculations baked directly into the database records. To deliver on the "Tailor-Made Repertoire" promise, users must be able to dynamically adjust how metrics are weighted (e.g., Complexity / Volatility vs. Practical Human Eval vs. Sacrifices) via debounced UI sliders.

The system must recalculate and serve these weighted values on the fly without breaking the tree structure or incurring costly re-explorations.

---

## 2. Decoupling Rules: Static vs. Dynamic Properties

1. **Static Invariant Properties (Database Layer):**
   * **Node Graph Structure:** Parents, children, FENs, and UCI moves.
   * **`accumulatedProbability`:** The cumulative path probability $P(path)$ is an intrinsic property of the tree depth and opponent historical move frequencies. It is **strictly independent** of user metric slider weights and must be calculated once and stored in the database.
   * **Isolated Raw Metrics:** $\mu$ (mean evaluation), $\sigma$ (volatility / standard deviation), and $Sac$ (sacrifice flags) are stored independently per node.

2. **Dynamic Properties (On-The-Fly Computation Layer):**
   * **Composite Utility Score $U(n)$:** Calculated dynamically when the client requests a tree traversal using the client-provided slider weights:
     $$U(n) = (w_\mu \cdot \mu(n)) + (w_\sigma \cdot \sigma(n)) + (w_{sac} \cdot Sac(n))$$
   * **Expectiminimax Backpropagation:** Traverses the cached in-memory/DB tree structure and propagates $U(n)$ from leaf nodes up to the root in real time.

---

## 3. API Contract Specifications

### Endpoint: `POST /api/repertoire/generate-tree`
Triggers an on-demand generation run based on user parameters, avoiding automatic startup generation.

#### Request Payload:
```json
{
  "startPgn": "1. d4 Nf6 2. c4 e6",
  "playerColor": "WHITE",
  "weights": {
    "humanEvalWeight": 0.5,
    "complexityWeight": 0.3,
    "sacrificeWeight": 0.2
  },
  "maxDepth": 20
}
```

#### Response:
Returns a `BuildSessionEntity` ID allowing the client to poll or stream status updates.

### Endpoint: `GET /api/repertoire/ai-moves` (Hollow Frontend Contract)
Returns sanitized node badges and evaluations derived from the dynamic backpropagation.

---

## 4. Performance & Caching Constraints
* In-memory Caffeine caching must guarantee that on-the-fly backpropagation across a 50,000-node tree executes in **$<15\text{ ms}$**.
* Database entities (`MoveNodeEntity`) are never mutated during dynamic recalculation; only the transient in-memory representation is re-scored.
