import random
kaisuu = [10, 100, 1000, 10000, 1000000]

def roll_average(trial):
    average = 0
    total = 0
    for n in range(trial):
        total += random.randint(1,6)
        average = total / trial
    return average

for i in kaisuu:
    print(str(i)+"回試行の平均値："+str(roll_average(i)))
# 期待される実行結果例
""" 
10回試行の平均値：3.6
100回試行の平均値：3.38
1000回試行の平均値：3.462
10000回試行の平均値：3.5006
1000000回試行の平均値：3.501243
"""
