papers=[{"title": "Attention Is All You Need",
    "year": 2017,
    "tags": ["Transformer", "Deep Learning", "NLP"]},
        {
    "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "year": 2019,
    "tags": ["BERT", "Pre-training", "NLP"]
  },{
    "title": "Language Models are Few-Shot Learners",
    "year": 2020,
    "tags": ["GPT-3", "Large Language Models", "Few-shot Learning"]
  },{
    "title": "Training Language Models to Follow Instructions with Human Feedback",
    "year": 2022,
    "tags": ["RLHF", "Instruction Tuning", "LLM"]
  },]
for p in papers:
    if p["year"]==2022:
        print(f'{p["title"]}')
    print(f'{p["year"]}-{p["title"]}')
print(papers[0])
