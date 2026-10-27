import requests
url="https://export.arxiv.org/api/query"
params={"search_query":"ti:AI agent paper reading OR abs:AI agent paper reading","start":0,"max_results":3,"sortBy":"submittedDate","sortOrder":"descending"}
resp=requests.get(url,params=params)
print(resp.url)
print(resp.status_code)
