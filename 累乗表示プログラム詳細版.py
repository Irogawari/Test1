print("-累乗表示プログラム-")

print("　")

print("mのn乗までを表示することができます。入力する値は4つで、mに当たる部分・nに当たる部分・初期値・x乗ずつ　です。")
print("m,nに当たる部分は、そのまま任意の値を入力してください。")
print("初期値は、「何乗から始めるか」を設定できます。")
print("x乗ずつは、「何乗飛ばしか」を設定できます。")
print("例）mに当たる値:5,nに当たる値:10,初期値:3,x乗ずつ:2の場合、[5の10乗までを、5の3乗から2乗飛ばしで表示する]となります。")

print("　")

m = int(input("mのn乗までを表示させます。mに当たる数字を入力してください>>>"))

n = int(input(str(m)+"のn乗まで表示させます。nに当たる数字を入力してください>>>"))

a = int(input("初期値を入力してください(デフォルト値：0)>>>"))

b = int(input("何乗ずつ表示するかを設定(デフォルト値：1)>>>"))

print("　")

print("===========" + str(m) + "の" + str(a)+"～" + str(n) + "乗===========")

print("　")

while a <= n:
    print(str(m)+"の" + str(a) + "乗" , end = "=")
    print(m**a)
    print("　")
    a += b

print("===============================")

print("　")

print("Enterを押すと終了します。")

int(input())
