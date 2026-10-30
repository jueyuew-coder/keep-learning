
import csv
import time
import requests
from pathlib import Path
from dataclasses import dataclass, asdict

@dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: list
    year: int
    summary: str
    pdf_url: str

    def short(self) -> str:
        return f"[{self.year}] {self.title} ({self.arxiv_id})"


p = Paper(
    arxiv_id="2210.03629",
    title="ReAct: Synergizing Reasoning and Acting in Language Models",
    authors=["Shunyu Yao"],
    year=2022,
    summary="Large language models...",
    pdf_url="https://arxiv.org/pdf/2210.03629",
)

print(p.short())

# 确保 data 文件夹存在
Path("data").mkdir(exist_ok=True)

# 写入 CSV
with open("data/papers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(asdict(p).keys()))
    writer.writeheader()
    writer.writerow(asdict(p))


# 带重试机制的网络请求函数
def fetch(url, params=None, retries=3, timeout=10):
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, params=params, timeout=timeout)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            print(f"第 {attempt} 次失败：{e}")
            if attempt < retries:
                time.sleep(3 * attempt)

    raise RuntimeError(f"重试 {retries} 次仍失败：{url}")
