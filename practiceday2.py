papers=["ReAct: Synergizing Reasoning and Acting",
    "Chain-of-Thought Prompting",
    "LLM Powered Autonomous Agents","react:reasoning and acting",]
print(f"共{len(papers)}篇论文，第二篇是：{papers[1]}")
for i,title in enumerate(papers):
    print(f"{i+1}.{title}")
keyword="Reasoning"
for title in papers:
    if keyword.lower() in title.lower():
        print(f"命中：{title}")
print(papers[:2])
for title in papers:
    if len(title)>25:
        print(title)
for i in range(1,6):
    print(f'第{i}天')
