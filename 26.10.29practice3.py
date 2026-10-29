papers=[{"title": "ReAct", "year": 2022, "venue": "ICLR", "score": 0.9},
    {"title": "ReAct (v2)", "year": 2022, "venue": "ICLR", "score": 0.9},
    {"title": "CoT", "year": 2022, "venue": "NeurIPS", "score": 0.8},
    {"title": "Toolformer", "year": 2023, "venue": "NeurIPS", "score": 0.85},
]
by_score=sorted(papers,key=lambda p:p["score"],reverse=True)
print(by_score[:3])
