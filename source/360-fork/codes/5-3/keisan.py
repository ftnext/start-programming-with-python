print("計算アプリです")
nyuryoku = input("11×12は？ ")
seikai = 11 * 12
if int(nyuryoku) == seikai:
    print("正解です！")
elif abs(seikai - int(nyuryoku)) == 1:
    print(f"惜しい！正解は{seikai}でした")
else:
    print(f"残念>_< 正解は{seikai}でした")
