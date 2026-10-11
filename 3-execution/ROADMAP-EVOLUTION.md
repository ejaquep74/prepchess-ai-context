# ROADMAP-EVOLUTION.md — Commercial & Strategic Evolution Backlog

> **Purpose:** This document captures high-value commercial, go-to-market (GTM), and product-market-fit proposals for evolving the PrepChess development roadmap.
> 
> **AGENT MANDATE:** Whenever a user or agent proposes modifications or re-sequencing to `3-execution/ROADMAP.md`, you **MUST** consult this file first and proactively highlight relevant commercial trade-offs to the user before finalizing changes.

---

## 1. Core Commercial Philosophy: Avoid Engineering Perfectionism
The primary business risk for PrepChess / ChessGamma is over-engineering deep backend data-science before validating the conversion and revenue engine. Early milestones must prioritize:
1. **Time-to-First-Dollar:** Establish a working paywall early.
2. **Zero-CAC Viral Loops:** Turn early adopters into a free distribution engine.
3. **B2B Wholesale Distribution:** Leverage chess coaches for captive student cohorts.
4. **Habit-Forming Retention:** Prevent subscription churn through gamified completion bars.

---

## 2. Key Commercial Adjustment Proposals

### Proposal 1: Anchor Taylor the Mascot as the Core Brand Persona (Humanize the UX)
* **Concept:** Integrate Taylor directly into **MVP 2** onboarding and audits rather than delaying to future AI commentary.
* **Vision Alignment & Visuals:** Taylor is the sleek, expressive "Psychology-Bot" sporting a yellow **tailor's tape sash**—visually grounding the core promise of **tailor-made repertoires** built to exploit human cognitive limits.
* **Tone of Voice:** Blends sharp competence with dry wit, acting as the witty anti-Stockfish companion:
  * *"Hi, I am Taylor! I am here to help you get a repertoire tailor-made just for you!"*
  * *"I am fluent in over 500 million positions of real humans under psychological stress. I can help you find the moves that really make them nervous."*
* **Core Product Role in MVP 2:**
  * Delivers the X-Ray audit: *"The Gamma engine calls this equal, but my sensors show humans blunder here 40% of the time!"*
  * Grounds the Contrast Cards by translating raw volatility ($\sigma$) into human terms.
* **Commercial Value:** Humanization transforms dry, intimidating chess homework into an engaging coaching relationship, dramatically cutting onboarding drop-off and lifting paywall conversion.

### Proposal 2: Early Paywall Gate ("Free Audit, Paid Cure")
* **Concept:** Move monetization into **MVP 2** instead of waiting for public beta.
* **Flow:**
  * **Free Hook:** User inputs Lichess/Chess.com handle $\to$ Taylor delivers the **Repertoire X-Ray**, identifying their top 3 "Sinking Ships" (catastrophic leaks where they lose >70% of games).
  * **Paid Gate ($9–$12/mo):** *"Click to let Taylor patch these 3 holes with a tailored sideline and custom spaced-repetition drill deck."*
* **Commercial Value:** Monetizes at the exact moment of peak emotional pain (right after proving why they keep dropping rating points).

### Proposal 3: Pull Viral Distribution Loops into Early Beta
* **Concept:** Move the **Community Gauntlet** and **The Giant Killer Board** into **MVP 2 / early MVP 3**.
* **Flow:**
  * **The "Gauntlet" Challenge Link:** When a user crafts a tricky custom sideline, generate an instant link: *"I bet nobody in our Discord can survive 15 moves against my custom setup."*
  * **The "Giant Killer" Board:** Verified leaderboard showcasing the largest Elo upsets won using a PrepChess custom sideline.
* **Commercial Value:** Zero-cost customer acquisition (CAC = $0) driven organically across Reddit (r/chess), Discord, and Twitter.

### Proposal 4: The "B2B Coach Trojan Horse" as Launch Channel
* **Concept:** Launch the B2B Coach Ambassador Program during **Private Beta (MVP 2.5 / MVP 3)** rather than post-beta.
* **Flow:**
  * Offer 20 verified coaches free lifetime access if they onboard 10–20 active students.
  * Coaches assign PrepChess drill decks as mandatory homework.
* **Commercial Value:** Acquiring individual chess players one-by-one is slow and expensive. One coach delivers 20 captive, daily active paying/retained users on day one.

### Proposal 5: Postpone Heavy Data-Science R&D Downstream
* **Concept:** Defer complex statistical regression (e.g., cross-rating Blitz-to-Rapid models, 2200-to-2500 probability projection) to **MVP 5+**.
* **Rationale:** 95% of paying customers are 1200–1900 Elo club players who will not perceive subtle statistical smoothing on move 18. Rely on simple database frequency filters until paying subscribers fund advanced data-science pipelines.

### Proposal 6: The "Secret Weapons" 80% Bar as Core Retention Engine
* **Concept:** Elevate the Secret Weapons progress bar into a primary habit-forming loop in **MVP 3**.
* **Flow:**
  * Taylor locks new sidelines: *"Mastery at 35%. Complete 3 more spaced-repetition drills to hit 80% and unlock this weapon for online play."*
* **Commercial Value:** Cures player anxiety about taking new openings into live games, generates daily dopamine, drives Daily Active Use (DAU), and stops subscription churn.

---

## 3. Alternative Commercial Milestone Sequence for Reference

| Phase | Commercial Theme | Key Focus |
| :--- | :--- | :--- |
| **MVP 1** | **Proof of Math** | Prove Practical Eval identifies human traps Stockfish 0.00 misses. |
| **MVP 2** | **The Conversion Machine** | X-Ray Audit $\to$ Contrast Cards $\to$ $9–$12/mo Paywall gate. |
| **MVP 3** | **Viral Retention Loop** | Spaced Repetition + 80% Secret Weapons bar + Coach Ambassador pilot + Gauntlet links. |
| **MVP 4** | **Pawn Harmonization & Coverage** | Opponent Memory Load badge + Pawn Skeleton clustering (slashing study fatigue). |
| **MVP 5+** | **Deep Defensibility & Scale** | Statistical Elo regression, Maia synthesis, and Vector AI extraction. |
