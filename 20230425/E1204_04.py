# 指定した入力ファイルの内容を行番号付きで指定した出力ファイルに書き込む
# sysモジュールを使用して、入力ファイル名と出力ファイル名を取得しています。
# with文を使用して、入力ファイルと出力ファイルを開いています。
# enumerate()関数を使用して、行番号を付与した上で入力ファイルの内容を読み込み、
# 出力ファイルに書き込んでいます。行番号を付与するには、
# enumerate()関数にstart引数を指定することで開始番号を指定することができます。
# このプログラムでは、開始番号を1に指定しています。
# 出力フォーマット [行内容]とあるので、文字列の末尾の改行コードを取り除くrstrip
# line.rstrip('\n')メソッドを使い、改行コード一旦削除し改行コードを付加
import sys

# 入力ファイル名と出力ファイル名を取得する
input_file = sys.argv[1]
output_file = sys.argv[2]

# 入力ファイルを開く
with open(input_file, 'r') as f_in:

    # 出力ファイルを開く
    with open(output_file, 'w') as f_out:

        # 行番号付きで入力ファイルの内容を出力ファイルに書き込む
        for i, line in enumerate(f_in):
            f_out.write(str(i+1) + ':[ ' + line.rstrip('\n') + ' ]\n' )