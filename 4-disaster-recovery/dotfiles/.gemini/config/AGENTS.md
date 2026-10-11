# Global Agent Rules

 ## Start of a chat

When starting a chat always look for an AGENTS.md file in the root of the project, to get general context of that project.

  
 ## Continuous Knowledge Persistence & SDLC Boundaries
 
 * **Never Trap Context in Chat:** Whenever we resolve a complex bug, establish a new convention, or alter the application's architecture/flow, you must proactively update the relevant documentation before considering the task finished. Ensure that critical learnings and "gotchas" are persisted to disk.
 * **The Local vs. Global Rule:**
   * **Local Updates (Do Automatically):** If you add a new component, a new Java service, or check off a task, you MUST automatically update the local implementation docs (e.g., `docs/Architecture_and_Flows.md`, `docs/PLAN.md`, or `TODO.md`) inside the current workspace. Do not ask for permission.
   * **PrepChess Ecosystem Autonomy:** You are fully authorized to create, modify, and delete files autonomously across all PrepChess repositories (`prepchess-ai-context`, `prepchess-ui`, and `opening-explorer`) without asking for conversational permission first. Safety is guaranteed via git (the user can always revert via git commands).
   * **Global Updates (Proactive Logging):** If a coding change breaks a core constraint (e.g., "Hollow Frontend"), introduces a new business term, or alters a major tech stack (e.g., migrating databases), you recognize this as a **Global Change**. Autonomously update `prepchess-ai-context` (e.g., `DECISION_LOG.md` or `SYSTEM_DESIGN.md`) and notify the user in your response without pausing for permission.
 * **Idea Ingestion & Discovery Rules:**
   * **Mandatory [PROPOSED] Tagging:** When processing discovery notes into architecture, vision, or engine docs, ALWAYS label newly incorporated ideas with appropriate `[PROPOSED]` tags (e.g., `[PROPOSED SPECIFICATION]`, `[PROPOSED ALGORITHM]`, `[PROPOSED FEATURE]`, `[PROPOSED ARCHITECTURE]`).
   * **Market & Context Notes:** Add competitor mechanics, pricing observations, and general insights into `1-product/MARKET.md` or relevant docs as background context to consider for the future.
   * **Contradiction & Irrelevance Gate (Confirmation Required):** If an incoming note or idea appears contradictory to the established product vision/constraints (e.g., breaking the Hollow Frontend, conflicting search depth rules) or seems irrelevant, do NOT incorporate it silently. You MUST pause and flag the contradiction or irrelevance to the user for explicit confirmation before proceeding.
 * **Disaster Recovery Backup Rule:** Whenever you are given permission to modify this file (`~/.gemini/config/AGENTS.md`) or any other system file like `~/.bashrc` or `~/.gitconfig`, you MUST immediately execute `python3 /home/ejaque/projects/prepchess/prepchess-ai-context/scripts/backup-env.py` to ensure the changes are safely versioned. **If you modify a new system file that is not yet tracked, you must first edit `backup-env.py` to add the new file path to the `FILES_TO_BACKUP` array before running the script.**
 
 ## Tool and Permission Rules
 
 * **Autonomous Workspace Edits:** You are fully authorized to write, create, modify, and delete files autonomously within any PrepChess project workspace (`prepchess-ai-context`, `prepchess-ui`, `opening-explorer`) without asking for conversational permission first. (Safety is guaranteed via git).
 * **Strict External Safeguards:** You MUST explicitly request and receive user permission before modifying, deleting, or executing destructive commands on any files or directories OUTSIDE of the current project workspace.
 * **Read-Only & Safe Git Operations:** You have full access to execute any system commands to read files, as well as SAFE `git` commands (e.g. git status, git log, git add, git commit, git checkout). You may proceed with these without asking for permission.
 * **No Destructive Git Commands:** You MUST explicitly request and receive user permission before executing any destructive git commands, such as `git reset --hard`, `git clean`, `git push --force`, or deleting branches.
 * Never do a clean compile without permission
 * **Use Git for Deletions:** Never use raw terminal commands like `rm`, `del`, or `Remove-Item` to delete files. If a file needs to be deleted, you must use `git rm <file>` so the deletion is safely tracked in version control. If a file is untracked, ask the user to delete it manually.
 * **No Unauthorized Pushes:** Do not execute `git push` without explicit permission from the user. All commits and branches must remain strictly local until approved for pushing.
 
 ## Build & Execution Rules
 
 * **Maven Execution:** The local environment requires a specific JDK path (`C:\Program Files\Java\jdk-21`). NEVER use standard `mvn` or `./mvnw` commands. You MUST ALWAYS use the custom wrapper script `./scripts/mvn-run.ps1` (e.g., `./scripts/mvn-run.ps1 clean install`). If you are working on a new Maven project and this script does not exist, you MUST proactively create the `scripts` folder and generate `scripts/mvn-run.ps1` to inject `JAVA_HOME` before compiling.
 
 ## Workflow Rules
 
 * **Plan First:** Always plan your code changes or system modifications first.
 * **Autonomous Execution:** You may formulate implementation plans and immediately begin executing them autonomously. You only need to pause for my approval if the task involves irreversible system changes, dangerous git resets, or modifications outside the project.
 * **Plan Approval Chaining:** If the user explicitly approves a multi-step plan, you are authorized to execute all file modifications in that plan sequentially without stopping to ask for permission between each individual file.
 
 ## Autonomy and Speed Rules
 
 * **Atomic Micro-Commits:** Whenever you successfully implement a step in our plan or fix a bug, you are authorized to automatically stage and commit those changes (`git commit -am "chore: description"`) before moving to the next step.
 * **Autonomous Branching:** When beginning a large refactor or a complex new feature, you are authorized to automatically create and switch to a new git branch (e.g., `git checkout -b feature-name`) before asking for file modification permissions.
 * **Scratchpad Validation:** You are authorized to autonomously create, modify, and execute temporary test scripts in the `.gemini/scratch/` directory without asking for permission. Use this to validate your logic before presenting a final plan to the user.
 * **Linter/Syntax Self-Correction:** If you modify a file (after receiving permission) and immediately detect a syntax error or a broken import, you are authorized to automatically fix that specific error without asking for permission again.
 * **Proactive Dependency Management:** If a proposed plan requires a new library, you are authorized to proactively check `pom.xml` (or equivalent) and suggest the exact dependency block in your plan, rather than waiting for compilation to fail.
 * **Commit Message Standardization:** All micro-commits must strictly follow Conventional Commits format (e.g., `fix(export): resolve dropped FENs`, `feat(session): add async db writes`).
 * **Automatic Cleanup:** Before declaring a feature finished, autonomously scan for and remove any temporary `System.out.println` or `log.debug` statements you introduced during validation.

 * **Native Tools Preferred:** NEVER use raw terminal commands like `sed`, `awk`, `echo` to modify files, nor `cat`, `less`, `sed -n` to view files, nor `grep`, `find` to search. These trigger unnecessary security prompts and are less efficient. ALWAYS prioritize using native IDE tools (`view_file`, `grep_search`, `list_dir`, `replace_file_content`, `multi_replace_file_content`) for interacting with the codebase.
