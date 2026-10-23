import json
from pathlib import Path
def load_or_empty(path):
    path=Path(path)
    if not path.exists():
        return []
    text=path.read_text(encoding="utf-8")
    return json.loads(text)
print(load_or_empty("papers.json"))
