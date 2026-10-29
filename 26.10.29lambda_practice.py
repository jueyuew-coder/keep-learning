papers=[{"title": "ReAct", "year": 2022, "venue": "ICLR", "score": 0.9},
    {"title": "ReAct (v2)", "year": 2022, "venue": "ICLR", "score": 0.9},
    {"title": "CoT", "year": 2022, "venue": "NeurIPS", "score": 0.8},
    {"title": "Toolformer", "year": 2023, "venue": "NeurIPS", "score": 0.85},
]
recent=[p for p in papers if p["year"]>2022]
titles=[p["title"] for p in papers]
by_score=sorted(papers,key=lambda p:p["score"],reverse=True)
seen,unique=set(),[]
for p in papers:
    key=p["title"].lower()
    if key not in seen:
        seen.add(key)
        unique.append(p)
print(len(papers),"->",len(unique))
