import random
total = 0
for i in range(10):
    x = random.randint(1,6)
    total += x
    print(str(i+1)+"回目："+str(x))
average = total/10
print("平均値:" + str(average))
# 出力結果例
"""
1回目：3
2回目：1
3回目：6
4回目：3
5回目：6
6回目：6
7回目：6
8回目：4
9回目：5
10回目：6
平均値:4.6
"""
