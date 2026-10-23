import json
from pathlib import Path
papers = [
    "ReAct: Synergizing Reasoning and Acting",
    "Chain-of-Thought Prompting",
    "LLM Powered Autonomous Agents",
]
path=Path("papers.json")
path.write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding="utf-8")
loaded=json.loads(path.read_text(encoding="utf-8"))
print(loaded)
