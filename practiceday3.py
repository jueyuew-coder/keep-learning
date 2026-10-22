def count_words(text):
    words=text.strip().split()
    return len(words)
x=input("输入一句话：")
print(count_words(x))
def is_recent(year,since=2022):
    return year>=since
print(is_recent(2022))
print(is_recent(2019))
print(is_recent(2025))
print(is_recent(2021,2023))
print(is_recent(2025,2024))
def make_note(content,tags=None):
    if tags is None:
        tags=[]
    return {"content":content,"tags":tags}
print(make_note("阅读一些论文"))
print(make_note("我在南师学习python的天",["AI","上课"]))
