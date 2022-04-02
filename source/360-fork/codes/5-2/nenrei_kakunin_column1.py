print("年齢確認のプログラムを開始します")
nenrei = 19  # 年齢を変更
if nenrei > 20:
    print(f"{nenrei}歳はお酒が買える年齢です")
elif nenrei == 20:
    print("成人おめでとう！お酒が買える年齢です")
elif nenrei == 19:  # 追加
    print("お酒が買える年齢ではありません。成人まであと1年です")  # 追加
else:
    print(f"{nenrei}歳はお酒が買える年齢ではありません")
print("プログラムを終了します")
