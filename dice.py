import random

total = 0

for i in range(10):
    x = random.randint(1,6)
    print(str(i + 1)+ "回目："+str(x))
    total += x

average = total / 10
print("平均値" + str(average)) 
