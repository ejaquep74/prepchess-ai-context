# SPEC-01: React UI Foundation & Initial Scaffold
> **Status:** IMPLEMENTED (See frontend `prepchess-ui` - currently on Stage 6)

## 1. Overview
This specification defines the initial "Hello World" scaffolding phase for the **PrepChess** web client. The goal of this phase is to establish a solid, scalable, and secure React foundation that aligns perfectly with the Java/Spring Boot "Hollow Frontend" architecture defined in `prepchess-ai-context/CONTEXT.md`.

## 2. Technology Stack
The foundational stack is locked as follows:
- **Build Tool:** Vite (for fast HMR and local development speed)
- **Framework:** React (Client-Side Rendering)
- **Language:** TypeScript (Highly recommended to strict-type the REST DTOs from the Java backend)
- **Chess Renderer:** `chessground`
- **Chess Logic & Rules:** `chessops`
- **State Management:** `zustand` (To manage the global repertoire tree state without causing React context re-render lag)
- **Styling:** Vanilla CSS (CSS Modules) focusing on a premium, dark-mode, glassmorphism aesthetic.
- **E2E Testing:** Playwright

## 3. Initial Project Structure
Once scaffolding is complete, the project structure should mirror this layout:

```text
prepchess-ui/
├── e2e/                     # Playwright automated UI tests
├── src/
│   ├── assets/              # Static assets (piece images, icons)
│   ├── components/          # Reusable UI components
│   │   ├── Chessboard/      # Wrapper for chessground
│   │   └── Layout/          # Main application layout
│   ├── store/               # Zustand global state (boardState, sliderState)
│   ├── styles/              # Global Vanilla CSS variables and tokens (index.css)
│   ├── types/               # TypeScript interfaces (mapping to Java DTOs)
│   ├── App.tsx              # Main entry point (The "Hello World" layout)
│   └── main.tsx             # Vite mount point
├── package.json
├── playwright.config.ts     # Playwright configuration
└── vite.config.ts
```

## 4. Phase 1 Execution Steps (What the AI Agent should do)

To successfully implement this specification, the AI Agent must execute the following commands in order:

### Step 4.1: Project Initialization
1. Run `npx create-vite@latest . --template react-ts` (inside the new UI folder).
2. Run `npm install` to install base dependencies.

### Step 4.2: Core Dependency Installation
1. Install chess dependencies: `npm install chessground chessops`
2. Install state management: `npm install zustand`
3. Install UI testing framework: `npm init playwright@latest` (select default options).

### Step 4.3: Global Aesthetic Setup
1. Wipe the default Vite `index.css` and `App.css`.
2. Create a new `index.css` implementing a **Premium Dark Mode** design system.
   - Define CSS variables for deep background colors (e.g., `#0f172a`), subtle borders (`rgba(255,255,255,0.1)`), and glowing accents for sacrifices.
   - Set a modern font (e.g., 'Inter', 'Outfit').

### Step 4.4: The "Hello World" Component
1. Modify `App.tsx` to render a basic Layout with a premium dark-mode background.
2. Render a centered `<div id="board-container">` with a "Hello World" title above it.
3. (Optional for Phase 1) Render a static `chessground` board in the starting position to verify the CSS and piece assets are loading correctly.

### Step 4.5: The UI Validation Test
1. Create a file `e2e/home.spec.ts`.
2. Write a Playwright test that navigates to `http://localhost:5173`.
3. Verify that the page loads, the title contains "PrepChess", and the `.cg-wrap` (chessground wrapper) or board container is visible.
4. Run `npx playwright test` to prove the setup is solid.

## 5. Security & Constraints
- **Strictly Hollow:** The UI must NOT contain any logic related to evaluating moves, generating tree statistics, or calculating the $U(n)$ utility function. 
- **Vanilla CSS:** Avoid introducing TailwindCSS unless specifically authorized, maintaining pure CSS control for premium aesthetics.
- **No Direct DOM Manipulation:** Outside of attaching `chessground` to its container ref, do not use vanilla DOM queries (`document.querySelector`) inside React components.
