import random

total = 0
for i in range(10):
    x = random.randint(1,6)
    print(str(i+1)+"回目："+str(x))
    total += x
    
average = total / 10
print("平均値:" + str(round(average, 2)))
# 期待される出力結果例
"""
1回目：2
2回目：6
3回目：3
4回目：3
5回目：6
6回目：5
7回目：6
8回目：3
9回目：5
10回目：5
平均値:4.4
"""
