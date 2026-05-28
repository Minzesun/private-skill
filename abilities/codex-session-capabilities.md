# Codex Session Capabilities

Generated on 2026-05-28 11:09:26.

## Enabled Plugin Families

- Browser
- Chrome
- Documents
- GitHub
- Presentations
- Spreadsheets
- Superpowers

## Current Tool/Ability Surface

- PowerShell shell commands and local filesystem operations
- Patch-based file editing
- Task planning updates
- Workspace dependency discovery for documents, sheets, slides, PDFs, and images
- DOCX/PDF workflow support through bundled runtimes and Microsoft Word/PyMuPDF fallback rendering
- Browser automation for local and authenticated browser tasks when plugin tools are available
- GitHub work through local git, GitHub API/credential manager, or GitHub plugin workflows when available
- Academic search MCP: paper search, DOI/PMID/arXiv lookup, citation formatting, MeSH lookup
- Node REPL MCP for JavaScript execution
- Image generation/editing tool access
- Recurring automation management through Codex app automation tools

## Local Skills Mirrored

| Skill | Source | Description |
|---|---|---|
| `imagegen` | `skills/.system/imagegen/SKILL.md` | Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas. |
| `openai-docs` | `skills/.system/openai-docs/SKILL.md` | Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains. |
| `plugin-creator` | `skills/.system/plugin-creator/SKILL.md` | Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, valid manifest defaults, and personal-marketplace entries by default. Use when Codex needs to create a new personal plugin, add optional plugin structure, generate or update marketplace entries for plugin ordering and availability metadata, or update an existing local plugin during development with the CLI-driven cachebuster and reinstall flow. |
| `skill-creator` | `skills/.system/skill-creator/SKILL.md` | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations. |
| `skill-installer` | `skills/.system/skill-installer/SKILL.md` | Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos). |
| `helloagents-launcher` | `skills/helloagents-launcher/SKILL.md` | Use when the user wants to start, run, launch, or use the local HelloAgents setup from Codex on this machine. |
| `helloagents-orchestrator` | `skills/helloagents-orchestrator/SKILL.md` | Use when the user wants Codex to hand a task to the local HelloAgents orchestrator so it can dispatch work to Claude Code and persist task state on this machine. |
| `nature-academic-search` | `skills/nature-academic-search/SKILL.md` | >- |
| `nature-citation` | `skills/nature-citation/SKILL.md` | >- |
| `nature-data` | `skills/nature-data/SKILL.md` | >- |
| `nature-figure` | `skills/nature-figure/SKILL.md` | >- |
| `nature-paper2ppt` | `skills/nature-paper2ppt/SKILL.md` | Build a complete but efficient Nature-style Chinese PPTX presentation from a scientific paper, preprint, PDF, article text, abstract, figure legends, or reading notes. Use this skill whenever the user asks to make slides/PPT/PPTX for journal club, group meeting, paper sharing, thesis seminar, lab meeting, department report, or academic presentation from a research paper, not only medical papers. It identifies the paper type and argument, selects only the figures needed for the story, writes Chinese slide content and speaker notes, creates the actual .pptx deck, and runs an explicit self-review/corrective revision loop focused on figure quality, text overflow prevention, and non-template visual design before delivery. |
| `nature-polishing` | `skills/nature-polishing/SKILL.md` | Polish, restructure, or translate academic prose into Nature-leaning English using writing-strategy principles, curated Nature/Nature Communications article patterns, and phrase-level support from Academic Phrasebank. Use whenever the user asks to polish a manuscript paragraph, abstract, introduction, results, discussion, conclusion, title, methods section, or Chinese academic draft for publication-quality English. |
| `nature-reader` | `skills/nature-reader/SKILL.md` | Build full-paper Chinese-English side-by-side, figure/table-aware, source-grounded Markdown readers for journal or conference papers from PDF, DOI, arXiv, publisher HTML, or pasted text. Use whenever the user asks to translate or read a paper, make 中英文对照/原文对照/全文翻译解读, extract figures or tables into the right positions, preserve figure/table placement near relevant prose, or keep exact source anchors for every block. This skill must not degrade into a summary-only output unless the user explicitly asks for a summary. |
| `nature-response` | `skills/nature-response/SKILL.md` | >- |
| `nature-writing` | `skills/nature-writing/SKILL.md` | Draft, restructure, or plan Nature-style manuscript sections from author-provided claims, results, figures, notes, Chinese drafts, or Chinese Word thesis/report formatting needs. Use when the user wants to write or rebuild an abstract, introduction, results narrative, discussion, conclusion, title, full manuscript argument, or Chinese academic DOCX style. |
| `obsidian-paper-kb` | `skills/obsidian-paper-kb/SKILL.md` | Use when working with the user's Obsidian vault for academic paper reading, Zotero local API imports, Zotero citekeys, PDF literature notes, research concept cards, thesis knowledge summaries, topic maps, or Chinese/English scholarly note organization. |
| `planning-with-files` | `skills/planning-with-files/SKILL.md` | Use when planning, tracking, or recovering a multi-step task, research effort, or implementation that will span many tool calls or sessions. |
| `brainstorming` | `skills/superpowers/brainstorming/SKILL.md` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation. |
| `dispatching-parallel-agents` | `skills/superpowers/dispatching-parallel-agents/SKILL.md` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `executing-plans` | `skills/superpowers/executing-plans/SKILL.md` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `finishing-a-development-branch` | `skills/superpowers/finishing-a-development-branch/SKILL.md` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup |
| `receiving-code-review` | `skills/superpowers/receiving-code-review/SKILL.md` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `requesting-code-review` | `skills/superpowers/requesting-code-review/SKILL.md` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `subagent-driven-development` | `skills/superpowers/subagent-driven-development/SKILL.md` | Use when executing implementation plans with independent tasks in the current session |
| `systematic-debugging` | `skills/superpowers/systematic-debugging/SKILL.md` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `test-driven-development` | `skills/superpowers/test-driven-development/SKILL.md` | Use when implementing any feature or bugfix, before writing implementation code |
| `using-git-worktrees` | `skills/superpowers/using-git-worktrees/SKILL.md` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification |
| `using-superpowers` | `skills/superpowers/using-superpowers/SKILL.md` | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| `verification-before-completion` | `skills/superpowers/verification-before-completion/SKILL.md` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always |
| `writing-plans` | `skills/superpowers/writing-plans/SKILL.md` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `writing-skills` | `skills/superpowers/writing-skills/SKILL.md` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

## Plugin Skill Metadata Only

| Skill | Cached Source | Description |
|---|---|---|
| `browser` | `openai-bundled/browser/26.519.81530/skills/browser/SKILL.md` | Browser automation for the Codex in-app browser. Use to open, navigate, inspect, test, click, type, screenshot, or verify local targets such as localhost, 127.0.0.1, ::1, file://, the current in-app browser tab, and websites shown side by side inside Codex. |
| `Chrome` | `openai-bundled/chrome/26.519.31651/skills/chrome/SKILL.md` | Browser automation for the user's Chrome browser. Use for browser tasks that require the user's cookies, logged-in sessions, existing tabs, extensions, or remote authenticated sites. |
| `Chrome` | `openai-bundled/chrome/26.519.41501/skills/chrome/SKILL.md` | Browser automation for the user's Chrome browser. Use for browser tasks that require the user's cookies, logged-in sessions, existing tabs, extensions, or remote authenticated sites. |
| `Chrome` | `openai-bundled/chrome/26.519.81530/skills/chrome/SKILL.md` | Browser automation for the user's Chrome browser. Use for browser tasks that require the user's cookies, logged-in sessions, existing tabs, extensions, or remote authenticated sites. |
| `Chrome` | `openai-bundled/chrome/latest/skills/chrome/SKILL.md` | Browser automation for the user's Chrome browser. Use for browser tasks that require the user's cookies, logged-in sessions, existing tabs, extensions, or remote authenticated sites. |
| `gh-address-comments` | `openai-curated/github/11b5af68/skills/gh-address-comments/SKILL.md` | Address actionable GitHub pull request review feedback. Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implement selected fixes. Use the GitHub app for PR metadata and flat comment reads, and use the bundled GraphQL script via `gh` whenever thread-level state, resolution status, or inline review context matters. |
| `gh-fix-ci` | `openai-curated/github/11b5af68/skills/gh-fix-ci/SKILL.md` | Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin for PR metadata and patch context, and use `gh` for Actions check and log inspection before implementing any approved fix. |
| `github` | `openai-curated/github/11b5af68/skills/github/SKILL.md` | Triage and orient GitHub repository, pull request, and issue work through the connected GitHub app. Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more specific GitHub workflow. |
| `yeet` | `openai-curated/github/11b5af68/skills/yeet/SKILL.md` | Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR through the GitHub app from this plugin, with `gh` used only as a fallback where connector coverage is insufficient. |
| `brainstorming` | `openai-curated/superpowers/11b5af68/skills/brainstorming/SKILL.md` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation. |
| `dispatching-parallel-agents` | `openai-curated/superpowers/11b5af68/skills/dispatching-parallel-agents/SKILL.md` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `executing-plans` | `openai-curated/superpowers/11b5af68/skills/executing-plans/SKILL.md` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `finishing-a-development-branch` | `openai-curated/superpowers/11b5af68/skills/finishing-a-development-branch/SKILL.md` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup |
| `receiving-code-review` | `openai-curated/superpowers/11b5af68/skills/receiving-code-review/SKILL.md` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `requesting-code-review` | `openai-curated/superpowers/11b5af68/skills/requesting-code-review/SKILL.md` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `subagent-driven-development` | `openai-curated/superpowers/11b5af68/skills/subagent-driven-development/SKILL.md` | Use when executing implementation plans with independent tasks in the current session |
| `systematic-debugging` | `openai-curated/superpowers/11b5af68/skills/systematic-debugging/SKILL.md` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `test-driven-development` | `openai-curated/superpowers/11b5af68/skills/test-driven-development/SKILL.md` | Use when implementing any feature or bugfix, before writing implementation code |
| `using-git-worktrees` | `openai-curated/superpowers/11b5af68/skills/using-git-worktrees/SKILL.md` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback |
| `using-superpowers` | `openai-curated/superpowers/11b5af68/skills/using-superpowers/SKILL.md` | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| `verification-before-completion` | `openai-curated/superpowers/11b5af68/skills/verification-before-completion/SKILL.md` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always |
| `writing-plans` | `openai-curated/superpowers/11b5af68/skills/writing-plans/SKILL.md` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `writing-skills` | `openai-curated/superpowers/11b5af68/skills/writing-skills/SKILL.md` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |
| `documents` | `openai-primary-runtime/documents/26.521.10419/skills/documents/SKILL.md` | Create, edit, redline, and comment on `.docx`, Word, and Google Docs-targeted document artifacts inside the container, with a strict render-and-verify workflow. Use `render_docx.py` to generate page PNGs (and optional PDF) for visual QA, then iterate until layout is flawless before delivering the final document. |
| `Presentations` | `openai-primary-runtime/presentations/26.521.10419/skills/presentations/SKILL.md` | Build PowerPoint PPTX decks with artifact-tool presentation JSX |
| `Spreadsheets` | `openai-primary-runtime/spreadsheets/26.521.10419/skills/spreadsheets/SKILL.md` | Use this skill when a user requests to create, modify, analyze, visualize, or work with spreadsheet files (`.xlsx`, `.xls`, `.csv`, `.tsv`) or Google Sheets-targeted spreadsheet artifacts with formulas, formatting, charts, tables, and recalculation. |

## Safety Note

This manifest is intended for private backup. Before making the repository public, audit bundled skills for third-party licensing and project-specific paths.

