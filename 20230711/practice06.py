# 実習6 practice06 2023/07/11
# 以下は、Pythonで指定されたURLにアクセスし、公開中の作品の一覧を取得するプログラムの例です。
# https://www.aozora.gr.jp/index_pages/person35.html#sakuhin_list_1
# この例では、requestsとBeautifulSoup4というライブラリを使用しています。
##############
# 下記のプログラムでは、指定したURLのページにアクセスし、そのHTMLをBeautifulSoupで解析しています。
# ロゴ画像のCSSセレクタを特定するために、find()メソッドを使用して最初の<img>要素を取得します。
# その後、該当のロゴ画像のCSSセレクタを特定するために、select_one()メソッドを使用して該当の<img>要素を指定します。
# もしロゴが見つかれば、そのCSSセレクタを取得して表示します。見つからない場合は、
# 「ロゴのCSSセレクタが見つかりませんでした。」と表示されます。
# ただし、各ウェブサイトのHTML構造やCSSクラスの設計は異なるため、
# 正確なロゴのCSSセレクタを特定する必要があります。
# プログラムが正しく動作しない場合は、ウェブサイトのHTML構造やCSSセレクタを確認し、適切な方法で特定してください。
##############
# command
# python -m venv myenv
# myenv\Scripts\activate
# pip install requests
# pip install beautifulsoup4
# まず、これらのライブラリをインストールする必要があります。
##############
# 文字化け対応
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import requests
from bs4 import BeautifulSoup

# URLの取得
url = "https://www.aozora.gr.jp/index_pages/person35.html#sakuhin_list_1"

# ページのHTMLを取得
response = requests.get(url)
# 日本語部分が文字化け
html_text = response.text   
# 日本語部分が文字化け response.txtをresponse.contentへ変更
html_cont = response.content

# 取得した値からBeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(html_cont, "html.parser")

# ロゴ画像のCSSセレクタを特定
# すべてのliタグを検索して、その文字列を表示する
count = 0
for element in soup.find_all("li"):    # すべてのliタグを検索して表示
    count += 1
    buff = str(count) + ' : ' + element.text
    print(buff)
    # print(count)
    # print(element.text)

