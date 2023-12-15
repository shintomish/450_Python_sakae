# 引数で指定した日付（形式：YYYY/MM/DD）に日数を加算し、結果を表示する
# sysモジュールを使用して、引数で指定された日付と日数を取得しています。
# datetimeモジュールを使用して、日付の文字列をdatetimeオブジェクトに変換しています。
# timedeltaクラスを使用して、日数を加算しています。そして、strftime()メソッドを使用して、
# 結果を文字列として表示しています。strftime()メソッドでは、
# 引数に指定したフォーマットで日付を文字列に変換することができます。
# 下のプログラムでは、フォーマットに'%Y/%m/%d'を指定しています。
# これは、年月日をスラッシュ区切りで表示するフォーマットです。
import sys
from datetime import datetime, timedelta

# 引数で指定された日付と日数を取得する
date_str = sys.argv[1]
days = int(sys.argv[2])

# 日付の文字列をdatetimeオブジェクトに変換する
date_obj = datetime.strptime(date_str, '%Y/%m/%d')

# 日数を加算する
result_date = date_obj + timedelta(days=days)

# 結果を表示する
print(result_date.strftime('%Y/%m/%d'))