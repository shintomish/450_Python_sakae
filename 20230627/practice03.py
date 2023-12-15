# 実習3 practice03 2023/06/27
# 以下は、Pythonで指定されたURLにアクセスし、HTMLの構造を確認するプログラムの例です。
# https://www.aozora.gr.jp/#main
# この例では、requestsとBeautifulSoup4を使用しています。
##############
# プログラムを実行すると、下記のエラーが出る。これを解決したい 
#  File "C:\400_Python\20230627\practice03.py", line 28, in <module>
#     print(soup.prettify())
# UnicodeEncodeError: 'cp932' codec can't encode character '\xe9' in position 288: illegal multibyte sequence
# エラーメッセージから推測すると、
# Windowsのデフォルトのエンコーディングである"cp932"が特定の文字を処理できないためにエラーが発生しています。
# このエラーを解決するには、標準出力のエンコーディングをUTF-8に変更する必要があります。
# 以下のように、sysモジュールを使用して標準出力のエンコーディングをUTF-8に設定することで、問題を解決できます。
##############
# 文字化け対応
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import sys
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

# 標準出力のエンコーディングをUTF-8に変更
sys.stdout.reconfigure(encoding='utf-8')

# HTMLの構造を表示
print(soup.prettify())

# このプログラムでは、requestsモジュールを使用して指定されたURLのページを取得し、
# そのHTMLをBeautifulSoupモジュールで解析します。
# 解析した結果をprettify()メソッドを使って整形して表示することで、
# HTMLの構造を確認できます。
# ただし、取得したHTMLは非常に長くなる場合があるため、
# 表示する範囲を絞りたい場合は適宜編集してください。
# また、ウェブサイトの構造が変更されると、
# プログラムの実行結果も変わる可能性がありますので、注意してください。
##############
# UnicodeEncodeError: 'cp932' codec can't encode character '\xe9' in position 288: illegal multibyte sequence
# Python3内部                  Windows標準出力(入力)
# ==========                  ===================
#   UTF-8  ---------------------->  CP932
#  (str型)   str.encode('CP932')   (byte型)
#          <----------------------
#            byte.decode('CP932')
# printできない原因は何か？
# 実は、Pythonは明示的に変換しなくても、標準出力等をする場合、自動的にシステムのエンコーディングに変換してから出力しようとする。
# Windowsの場合は、CP932へ変換しようとするため、CP932に変換出来ない場合は、UnicodeEncodeError例外が発生する。
##############