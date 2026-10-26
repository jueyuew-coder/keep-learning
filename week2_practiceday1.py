import requests
resp=requests.get("https://httpbin.org/get",timeout=10)
print(resp.status_code)
print(resp.headers["content-type"])
print(resp.text[:200])
