# SPEC-03: AI-Generated Interactive Plan Explanations

> **Status:** Specification (MVP 3 AI Commentary & Training)  
> **Target Component:** `opening-explorer` (Orchestrator) & `prepchess-ui` (Presentation)

---

## 1. Context & Purpose
Players often abandon opening trainers because they memorize moves without understanding the underlying structural plans. 

This specification defines the schema and data model for **AI-Generated Interactive Plan Explanations** (Taylor's Voice). The system pairs natural language strategic commentary with structured board metadata (outposts, maneuvers, open files, targets) that allow the frontend to render arrows, colored squares, and tactical highlights synchronized with the explanation.

---

## 2. Structural Data Contract

When an explanation is requested for a specific node in the opening tree, the backend orchestrator synthesizes the engine data and tree metadata into a structured JSON response:

```json
{
  "fen": "r1bq1rk1/1pp1bppp/p1np1n2/4p3/2B1P3/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 0 8",
  "planTitle": "The Central Counter-Strike (Nd5)",
  "commentary": "Instead of passively defending against the flank attack, plunge your knight directly into the d5 outpost ($1). If Black captures with ...Nxd5, recapture with cxd5 ($2), blunting their bishop and ripping open the c-file for your rook ($3).",
  "references": {
    "$1": {
      "type": "OUTPOST",
      "square": "d5",
      "highlightColor": "rgba(46, 204, 113, 0.4)"
    },
    "$2": {
      "type": "CAPTURE_STRUCTURAL",
      "move": "c4xd5",
      "pawnSkeleton": "cxd5"
    },
    "$3": {
      "type": "FILE_PRESSURE",
      "file": "c",
      "arrow": {
        "from": "b1",
        "to": "c1",
        "color": "#3498db"
      }
    }
  },
  "tacticalMetadata": {
    "openFiles": ["c"],
    "halfOpenFiles": ["e"],
    "outposts": ["d5"],
    "weakTargets": ["c7", "d6"],
    "keyManeuvers": [
      {
        "piece": "W_R",
        "path": ["b1", "c1"]
      },
      {
        "piece": "W_N",
        "path": ["c3", "d5"]
      }
    ],
    "criticalDiagonals": ["g2-a8"]
  },
  "candidateVariations": [
    {
      "name": "Variation A: Direct central strike",
      "movesSan": ["10. Nd5", "Nxd5", "11. cxd5", "Ne7", "12. Rbc1"]
    },
    {
      "name": "Variation B: Delayed strike after flank commit",
      "movesSan": ["10. a3", "f4", "11. Nd5", "Nxd5", "12. cxd5", "Ne7", "13. Rbc1"]
    }
  ]
}
```

---

## 3. Frontend Interactive Behavior (`prepchess-ui`)
1. **Interactive Text Highlighting:** The commentary text in the UI renders tokens like `$1` and `$3` as clickable or hoverable badges.
2. **Synchronized Board Graphics:** Hovering over an outpost badge highlights that square on `react-chessboard`. Hovering over a maneuver badge renders the directional arrow (%cal).
3. **Audio / Speech (Future):** Taylor’s voice can stream the `commentary` text while the frontend sequentially illuminates the referenced squares.
