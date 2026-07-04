# 🛠️ Build Your First AI Crew — CrewAI (Lesson 1)

The full code from the video: a **team of three AI agents** that takes one coding job and ships it.
🦉 **Architect** designs → 🦫 **Engineer** writes the code → 🐈 **Reviewer** hunts the bugs.

▶️ Watch the video · Channel: **@techfluencer-eval**

---

## 🚀 Run it in 60 seconds

```bash
uv init agentic-crew
uv add crewai "crewai[azure-ai-inference]"
# copy .env.example -> .env and fill in your keys
uv run main.py
```

> Using Azure OpenAI here, but CrewAI runs on any model — change the one `LLM(...)` line.

---

## 🧠 CrewAI Cheat-Sheet (one page)

| Piece | What it is | Key fields |
|---|---|---|
| **`Agent`** | a worker with a job | `role`, `goal`, `backstory`, `llm` |
| **`Task`** | one assignment for an agent | `description`, `expected_output`, `agent` |
| **`Crew`** | the manager / orchestrator | `agents=[]`, `tasks=[]`, `process` |
| **`process`** | how tasks run | `Process.sequential` (relay) · `Process.hierarchical` (boss agent) |
| **`crew.kickoff(inputs={...})`** | start the run | fills the `{placeholders}` |

**The mental model:** don't make one AI do everything — hire specialists that collaborate.

**Golden rules**
- Give every agent a *specific* `backstory` (not "a helpful assistant").
- Always set `expected_output` — it keeps the hand-off between agents clean.
- Split big jobs across a crew; keep `verbose=True` while learning.

---

## 📂 Files
- `main.py` — the 3-agent crew (this episode)
- `.env.example` — copy to `.env`, add your keys
- `pyproject.toml` — deps (managed by `uv`)

## 🎯 Your challenge
Add a **4th agent** — a Documentation Writer that turns the final code into a README. (role · goal · backstory · a task · add to the crew · run.)

---
*Next lesson: the **Boss Agent** — hierarchical crews.*
