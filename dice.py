import random

total = 0

for i in range(10):
    x = random.randint(1,6)
    total += x
    print(str(i+1)+"回目："+str(x))

average = total / 10
print("平均値:" + str(round(average,1)))

実行結果：
1回目：2
2回目：4
3回目：5
4回目：4
5回目：6
6回目：3
7回目：2
8回目：6
9回目：2
10回目：1
平均値:3.5
