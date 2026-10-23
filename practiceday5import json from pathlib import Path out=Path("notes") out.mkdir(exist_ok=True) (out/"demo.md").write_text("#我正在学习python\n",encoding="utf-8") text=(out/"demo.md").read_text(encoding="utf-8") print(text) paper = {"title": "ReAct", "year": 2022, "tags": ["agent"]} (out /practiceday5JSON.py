import json
from pathlib import Path
out=Path("notes")
out.mkdir(exist_ok=True)
(out/"demo.md").write_text("#我正在学习python\n",encoding="utf-8")
text=(out/"demo.md").read_text(encoding="utf-8")
print(text)
paper = {"title": "ReAct", "year": 2022, "tags": ["agent"]}
(out / "demo.json").write_text(
    json.dumps(paper, ensure_ascii=False, indent=2),   # ensure_ascii=False 才能正常显示中文
    encoding="utf-8",
)
loaded = json.loads((out / "demo.json").read_text(encoding="utf-8"))
print(loaded["title"], loaded["tags"])
