# Dependencies and portable paths

The installer needs Python 3.10+; cloning/updating needs Git and access to the private GitHub repository. It uses copy installation on every OS. You do not need to install optional helper tools just to use the planning trio.

## Teaching workspaces

The portable teaching copies resolve paths at task time:

| Setting | Resolution |
|---|---|
| `LLM_COURSE_ROOT` | Explicit workspace in the request, then this environment variable, then the current curriculum workspace, then `Documents/LLMs` under the current user's home |
| `GPT_REFERENCE_ROOT` | This environment variable or `Documents/git_repos/how-to-train-your-gpt` under the current user's home |
| `AI_REFERENCE_ROOT` | This environment variable or `Documents/education/ai` under the current user's home |

These are filesystem locations for separate repositories/data; installation does not clone them. Honor the selected course's AGENTS.md and curriculum. If required reference material is absent, report the missing dependency rather than inventing source evidence. Configure environment variables using the shell conventions on the destination system, or give the agent the path in the request.

`teach-technical` references its sibling `teach-course` using a relative path. All supporting lesson templates, CSS and validation scripts are included. Existing lesson-format differences are preserved and documented, not silently merged as part of packaging.

## Optional tools

| Skill | Additional capability needed |
|---|---|
| Planning, review, design and research | Agent file/shell/browser tools as required by the task; no separate package for the prose workflow |
| lavish | Node/npm and the lavish-axi CLI, plus a browser for review |
| playwright-cli | The matching Playwright CLI and browser runtime; install according to its own instructions |
| notebooklm | notebooklm-py, the selected authentication method and Google account access; keep credentials outside Git |
| Teaching skills | The course's Python/uv/Jupyter environment and requested numerical libraries |
| system-design speech | Optional Bash helper; native `say`/audio playback is macOS-specific. Use text mode on other systems unless a supported voice setup is explicitly configured |
| tradingview-chart-analysis | An accessible TradingView chart session and supported browser/chart tools |

Some helpers are platform-specific even though the skill folders and installer are portable. The installer neither invokes these helpers nor installs their dependencies.

## Bundled skills and plugins

System skills such as skill-creator, skill-installer, imagegen and openai-docs come from Codex and should be supplied by the target Codex installation. Restore artifact, Google Drive, Sites, visualization, deep-research and ARS capabilities through the target app's supported plugin workflow. Plugin versions and access may differ by system. Do not copy caches or authentication files to simulate an installed plugin.

The repo does not promise a complete clone of the desktop app's account connections, model access, permissions or external services.
