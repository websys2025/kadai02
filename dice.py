import random
import statistics                                #平均値を求める関数をインポート


l = []                                           #平均値を求めるためのリストを定義
for i in range(10):
    x = random.randint(1,6)
    print(str(i+1)+"回目："+str(x))
    l.append(x)                                  #リストに値を追加
else:
    print("平均値："+ str(statistics.mean(l)))    #平均値の結果を表示
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
