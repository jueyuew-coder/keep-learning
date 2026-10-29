papers=[{"title": "ReAct", "year": 2022, "venue": "ICLR", "score": 0.9},
    {"title": "ReAct (v2)", "year": 2022, "venue": "ICLR", "score": 0.9},
    {"title": "CoT", "year": 2022, "venue": "NeurIPS", "score": 0.8},
    {"title": "Toolformer", "year": 2023, "venue": "NeurIPS", "score": 0.85},
]
for p in papers:
    if p["venue"]=="NeurIPS":
        print(p)
