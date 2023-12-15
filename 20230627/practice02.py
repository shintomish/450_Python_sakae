# 実習2 practice02 2023/06/27
# # 国土交通省土地総合情報システムAPIを使用して、
# 2019年1月〜12月の北海道札幌市の不動産取引価格情報を取得する
# https://www.land.mlit.go.jp/webland/api.html
# Pythonプログラムの例を以下に示します。
# この例では、requestsモジュールを使用してAPIにリクエストを送信し、
# 取得したデータを処理しています。
# まず、APIキーの取得とrequestsライブラリのインストールが必要です。

# -----------------------
# import requests

# from_id = '20191'
# to_id = '20194'
# city_id = '01100'

# url='https://www.land.mlit.go.jp/webland/api/TradeListSearch?'

# params = {'from':from_id,'to':to_id,'city':city_id,}
# r = requests.get(url, params=params)
# print(params)
# data_all=r.json()

# print(data_all['data'][:10])
# -----------------------

import requests
from_id = '20191'
to_id = '20194'
city_id = '01100'
# # APIキー
# api_key = "Your_API_Key"

# # APIエンドポイントのURL
url = 'https://www.land.mlit.go.jp/webland/api/TradeListSearch?'
# # パラメータ
params = {
    'from':from_id,
    'to':to_id,
    'city':city_id,
}
# params = {
#     'from': '20191',
#     'to': '201912',
#     'city': '01100',  # 札幌市のエリアコード
#     # "format": "json",
#     # "key": api_key,
# }
# # APIリクエストの送信
response = requests.get(url, params=params)

# # レスポンスのJSONデータを取得
data = response.json()
# print(data['data'][:10])

# # # 取引情報の表示
if 'data' in data:
    # transactions = data['data']
    transactions = data['data'][:10]
    for transaction in transactions:
        # print(transaction)
        print('日付:', transaction['Period'])
        print('地区:', transaction['Prefecture'])
        print('市区町村名:', transaction['Municipality'])
        # print('用途:', transaction['Purpose'])
        print('取引価格:', transaction['TradePrice'], '円')
        print('-------------------------')
else:
    print('データの取得に失敗しました。')

##  上記のプログラムでは、APIキーの部分を"Your_API_Key"として置き換える必要があります。
##  APIキーは、国土交通省土地総合情報システムのウェブサイトで取得できます。
##  リクエストURLでは、以下のクエリパラメータを指定しています：

## from: 取得するデータの開始日（YYYYMM形式）
## to: 取得するデータの終了日（YYYYMM形式）
## area: 地域コード（北海道の場合は"01"）
## city: 市区町村コード（札幌市の場合は"01100"）
## format: レスポンス形式（この例ではJSON形式を指定）
## api_key: APIキー
## APIから取得したデータはJSON形式で返されます。
## プログラムでは、取得したデータを処理して必要な情報を表示しています。
## なお、APIの仕様やデータの形式は変更される可能性があるため、
## 動作しない場合は公式ドキュメントを参照して最新の仕様を確認してください。
# 国土交通省土地総合情報システムAPIを使用するためには、
# APIキーが必要です。APIキーは、国土交通省のウェブサイトで登録および発行する必要があります。
# ただし、私の知識は2021年9月までのものであり、APIキーの発行方法や仕様が変更されている可能性があります。
# 以下の手順は、2021年9月時点でのAPIキーの発行手順です。
# 1. 国土交通省のウェブサイトにアクセスし、
# API利用の申請ページに移動します。URLは以下の通りです: https://www.land.mlit.go.jp/webland/api.html
# 2. ページ内の「APIの利用登録手続き」をクリックします。
# 3. 利用規約を確認し、同意した場合は「同意する」を選択します。
# 4. 利用申請フォームに必要事項を入力し、申請を行います。
# 個人や法人によって必要な情報が異なるため、正確な情報を提供してください。
# 5. 申請が承認されると、指定した連絡先にAPIキーが送られてきます。
# 申請手続きに関する詳細や最新情報は、国土交通省のウェブサイトを参照してください。
# また、APIキーの発行手順が変更されている可能性もあるため、最新の情報を確認してください。
# なお、APIキーを取得した後に、以下の例のようなプログラムを使用して、北海道札幌市の不動産取引価格情報を取得できます。

# ```python
# import requests
# api_key = "ここに取得したAPIキーを入力"
# # APIエンドポイントのURL
# url = "https://www.land.mlit.go.jp/webland/api/TradeListSearch"
# # パラメータ
# params = {
#     "from": "201901",
#     "to": "201912",
#     "area": "01100",  # 札幌市のエリアコード
#     "format": "json",
#     "key": api_key,
# }
# # APIリクエストの送信
# response = requests.get(url, params=params)

# # レスポンスのJSONデータを取得
# data = response.json()

# # 取引情報の表示
# for transaction in data["data"]:
#     print(transaction["日付"], 
#           transaction["都道府県名"], 
#           transaction["市区町村名"], 
#           transaction["取引価格"])
# この例では、APIキーを`api_key`変数に代入し、`params`変数には必要なパラメータを設定しています。そして、`requests.get()`関数を使用