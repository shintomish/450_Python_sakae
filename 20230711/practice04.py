# 実習4 practice04 2023/07/11
# 以下は、Pythonで指定されたURLにアクセスし、サイトロゴのソースコードを特定するプログラムの例です。
# https://www.aozora.gr.jp/#main
# この例では、requestsとBeautifulSoup4というライブラリを使用しています。
##############
# 上記のプログラムでは、指定したURLのページにアクセスし、そのHTMLをBeautifulSoupで解析しています。
# ロゴ画像のソースコードを特定するために、find()メソッドを使用し、
# 対象のロゴのクラス名を指定します（"ここにロゴのクラス名を入力"の部分）。
# もしロゴが見つかれば、そのソースコードを取得して表示します。見つからない場合は、
# 「ロゴが見つかりませんでした。」と表示されます。
# ただし、各ウェブサイトのHTML構造は異なるため、正確なロゴのクラス名や要素を特定する必要があります。
# プログラムが正しく動作しない場合は、ウェブサイトのHTML構造を確認し、対応するクラス名や要素を適切に指定してください。
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

# import sys
import requests
from bs4 import BeautifulSoup

# URLの取得
url = "https://www.aozora.gr.jp/#main"

# ページのHTMLを取得
response = requests.get(url)
# 日本語部分が文字化け
html_text = response.text   
# 日本語部分が文字化け response.txtをresponse.contentへ変更
html_cont = response.content

# 取得した値からBeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(html_cont, "html.parser")

# ロゴ画像のソースコードを特定
# logo = soup.find("png", class_="titleLogo")
logo = soup.find(class_="titleLogo")
if logo:
    logo_source = logo["src"]
    print("ロゴのソースコード:", logo_source)
else:
    print("ロゴが見つかりませんでした。")
