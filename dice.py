import random
ave = 0
s = 0
for i in range(10):
    x = random.randint(1,6)
    s += x
    print(str(i+1)+"回目："+str(x))
    ave = s / (i+1)  
print("平均値："+ str(ave))

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
