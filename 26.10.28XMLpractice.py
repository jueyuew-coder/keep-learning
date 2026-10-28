import requests
import xml.etree.ElementTree as ET
url="https://export.arxiv.org/api/query"
params={"search_query":'(ti:"AI agent" OR abs:"AI agent")',
        "start":0,
        "max_results":3,
        "sortBy":"submittedDate",
        "sortOrder":"descending"}
resp=requests.get(url,params=params,timeout=10)
resp.raise_for_status()
print("状态码：",resp.status_code)
print("请求地址",resp.url)
root=ET.fromstring(resp.text)
ns={"atom":"http://www.w3.org/2005/Atom"}
for entry in root.findall("atom:entry",ns):
    title_node=entry.find("atom:title",ns)
    title=" ".join(title_node.text.split()) if title_node is not None and title_node.text else ""
    date_node = entry.find("atom:published", ns)
    published = date_node.text[:10] if date_node is not None and date_node.text else ""

    authors = []
    for a in entry.findall("atom:author", ns):
        name_node = a.find("atom:name", ns)
        if name_node is not None and name_node.text:
            authors.append(name_node.text.strip())

    summary_node = entry.find("atom:summary", ns)
    summary = (
        " ".join(summary_node.text.split())[:120]
        if summary_node is not None and summary_node.text
        else ""
    )
    author_display=",".join(authors) if authors else "未知作者"
    print(f"{published}|{title}|{author_display}")
    print(f"{summary}...")
