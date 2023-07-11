import requests
from bs4 import BeautifulSoup
import re

# 發送 HTTP 請求
response = requests.get("https://sitcon.camp/2023/")

# 解析 HTML 文件
soup = BeautifulSoup(response.text, "html.parser")

# 定義正則表達式
pattern = re.compile(r"https?://\S+")

# 建立一個空的串列來儲存連結
links = []

# 遍歷所有的 HTML 標籤
for tag in soup.find_all():
    # 取得標籤的屬性字典
    attrs = tag.attrs
    # 遍歷所有的屬性值
    for value in attrs.values():
        # 如果屬性值是字串，且符合正則表達式
        if isinstance(value, str) and pattern.match(value):
            # 將連結加入到串列中
            links.append(value)

# 印出所有的連結
for link in links:
    print(link)
