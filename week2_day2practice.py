import requests
url="https://httpbin.org/get"
params={"q":"AI agent","year":2024}
resp=requests.get(url,params=params,timeout=10)
print("请求URL：",resp.url)
resp.raise_for_status()
print("Content_type:",resp.headers.get("content-type"))
data=resp.json()
print("查询参数：",data["args"])
