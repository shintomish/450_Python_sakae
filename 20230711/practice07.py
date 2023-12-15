# 実習7 practice07 2023/07/11
# 以下のURLからXMLファイルをダウンロードし、区ごとの防災拠点を表示するプログラムを作成してください。
# https://www.city.yokohama.lg.jp/kurashi/bousai-kyukyu-bohan/bousai-saigai/bosai/data/data.files/0006_20180911.xml
# 
##############
# このプログラムでは、requestsモジュールを使用して指定されたURLからXMLファイルをダウンロードします。
# その後、xmlモジュールのElementTreeを使用してXMLを解析します。
# XMLのルート要素（root）から区（Area）ごとにループを回し、区名と防災拠点（Shelter）の情報を表示します。
# 注意点として、プログラムが正しく動作するためには、指定されたURLが有効であり、
# XMLファイルのフォーマットが予想通りである必要があります。また、XMLの構造や要素名が変更されている場合は、
# プログラムを適宜修正する必要があります。
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
import xml.etree.ElementTree as ET

# XMLファイルのURL
url = "https://www.city.yokohama.lg.jp/kurashi/bousai-kyukyu-bohan/bousai-saigai/bosai/data/data.files/0006_20180911.xml"
# XMLの構造
# <LocationInformation>
# <Type>地域防災拠点</Type>
# <Definition>被災した住民の避難生活の場所、情報受伝達、備蓄機能を備えた拠点です。</Definition>
# <Name>戸塚中学校</Name>
# <Address>神奈川県横浜市戸塚区戸塚町4542</Address>
# <Lat>35.40122291</Lat>
# <Lon>139.523622</Lon>
# <Kana>トツカチュウガッコウ</Kana>
# <Ward>戸塚区</Ward>
# <WardCode>15</WardCode>
# </LocationInformation>

# XMLファイルのダウンロード
response = requests.get(url)
xml_content = response.content

# XMLを解析
root = ET.fromstring(xml_content)

# XMLのルート要素（root）から区（Area）ごとにループを回し、区名と防災拠点（Shelter）の情報を表示します。
# # 区ごとの防災拠点を表示
# for area in root.findall(".//Area"):
#     area_name = area.find("AreaName").text
#     shelters = area.findall(".//Shelter")
    # print("区名:", area_name)
    # for shelter in shelters:
    #     shelter_name = shelter.find("ShelterName").text
    #     print("- 防災拠点:", shelter_name)
    # print()
# 区ごとの防災拠点を表示
for area in root.findall('LocationInformation'):
    # area_name = area.find("Ward").text
    # shelters = area.find('Name').text
    # print("区名:", area_name)
    # print("- 防災拠点:", shelters)
    area_names = area.findall("地域防災拠点")
    shelters = area.findall(".//Ward")
    area_ = area.find("Ward").text
    print("区名:", area_)
    for shelter in shelters:
        shelter_name = area.find("Name").text
        print("- 防災拠点:", shelter_name)
    print()

