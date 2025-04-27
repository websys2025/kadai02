import random

total=0  add:totalを0に初期化
for i in range(10):
    x = random.randint(1,6)
    print(str(i+1)+"回目："+str(x))
    total +=x add:出力された数字を合わせた合計を算出

ave=(total)/10  add:算出した合計から平均を求める
print("平均値：",ave)
# 期待される出力結果例
"""
1回目：4
2回目：1
3回目：1
4回目：5
5回目：1
6回目：1
7回目：5
8回目：6
9回目：4
10回目：6
平均値：3.4
"""
