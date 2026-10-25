from datetime import date
def make_note():
    title=input("请输入标题：")
    year=input("请输入年份：")
    research_question=input("请输入研究问题：")
    method=input("请输入研究方法：")
    conclusion=input("请输入结论：")
    today=date.today().strftime("%Y-%m-%d")
    md_content=f"""
### {title}
记录日期：{today}
文献年份：{year}
**研究问题**：{research_question}
**研究方法**：{method}
**结论**：{conclusion}
"""
    with open("reading_log.md","a",encoding="utf-8")as f:f.write(md_content)
    print("笔记已经追加写入 reading_log.md")
if __name__=="__main__":
    make_note()
