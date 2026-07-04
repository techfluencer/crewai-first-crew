from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM

# One shared brain (Azure OpenAI) for the whole crew.
# Reads AZURE_API_KEY / AZURE_API_BASE / AZURE_API_VERSION from .env
llm = LLM(model="azure/gpt-4o-mini")

# ---------------------------------------------------------------------------
# The crew: three specialists, each with a role, a goal, and a backstory.
# ---------------------------------------------------------------------------
architect = Agent(
    role="Software Architect (the Owl)",
    goal="Design a clean, simple approach for: {feature}",
    backstory=(
        "A wise owl of an engineer who always plans before a single line is written. "
        "You outline the function signature, the steps, and the edge cases — but you write NO code."
    ),
    llm=llm,
    verbose=True,
)

engineer = Agent(
    role="Python Engineer (the Beaver)",
    goal="Turn the architect's plan into correct, readable Python for: {feature}",
    backstory=(
        "A tireless builder who turns a plan into working code with a short docstring "
        "and no unnecessary cleverness."
    ),
    llm=llm,
    verbose=True,
)

reviewer = Agent(
    role="Code Reviewer (the Cat)",
    goal="Catch bugs and missed edge cases, then return the final improved Python for: {feature}",
    backstory=(
        "A sharp-eyed critic who mentally tests the code, fixes what's weak, "
        "and hands back the polished final version."
    ),
    llm=llm,
    verbose=True,
)

# ---------------------------------------------------------------------------
# The tasks: each declares exactly what 'done' looks like (expected_output).
# In a sequential crew, each task's output is passed as context to the next.
# ---------------------------------------------------------------------------
design_task = Task(
    description=(
        "Design the solution for: {feature}. "
        "List the function signature, the numbered steps, and at least three edge cases. "
        "Do NOT write the implementation yet."
    ),
    expected_output="A short design: the signature, numbered steps, and a bullet list of edge cases.",
    agent=architect,
)

build_task = Task(
    description="Using the architect's design, write the Python implementation for: {feature}.",
    expected_output="A single Python code block containing the function and a short docstring.",
    agent=engineer,
)

review_task = Task(
    description=(
        "Review the engineer's code for bugs and missed edge cases. "
        "Fix them and return the FINAL improved code, then one line on what you changed."
    ),
    expected_output="The final Python code block, followed by 'Changes:' and one short line.",
    agent=reviewer,
)

# ---------------------------------------------------------------------------
# The Crew orchestrates the agents, runs the tasks in order,
# and feeds each finished result to the next agent automatically.
# ---------------------------------------------------------------------------
crew = Crew(
    agents=[architect, engineer, reviewer],
    tasks=[design_task, build_task, review_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    feature = "a Python function is_palindrome(text) that ignores case, spaces, and punctuation"
    result = crew.kickoff(inputs={"feature": feature})
    print("\n\n===== FINAL =====\n")
    print(result)
