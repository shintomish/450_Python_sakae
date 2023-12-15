# 実習1 practice01 2023/06/27
# 以下のURLのHTMLを取得し、記事のタイトルを抽出してください。
# https://news.yahoo.co.jp/topics/top-picks

# 以下は、Pythonで指定されたURLのHTMLを取得し、
# 記事のタイトルを抽出するプログラムの例です。
# この例では、requestsとBeautifulSoup4というライブラリを使用しています。
# pip install requests
# pip install beautifulsoup4
# まず、これらのライブラリをインストールする必要があります。

# このプログラムでは、requestsモジュールを使用して指定されたURLのページを取得し、
# そのHTMLをBeautifulSoupモジュールで解析します。
# 解析した結果から、記事のタイトルを抽出し、タイトルを表示します。
# ただし、注意点としては、ウェブサイトの構造が変更されると、
# プログラムの動作も影響を受ける可能性があることです。プログラムが正常に動作しない場合は、
# ウェブサイトの構造が変更されていないかを確認してください。
# C:\400_Python>python 20230627\practice01.py > 20230627\practice01.txt

import requests
from bs4 import BeautifulSoup

# URLの取得
url = "https://news.yahoo.co.jp/topics/top-picks"

# ページのHTMLを取得
response = requests.get(url)
html = response.text

# BeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(html, "html.parser")

# 記事のタイトルを抽出して表示
titles = soup.select(".newsFeed_item_title")
for title in titles:
    print(title.text)

