import random
kaisuu = [10, 100, 1000, 10000, 1000000] # 平均値用のリスト

def roll_average(trial):
    average = 0 # 平均値の初期化
    total = 0 # サイコロの出目の合計値を記録する変数
    for n in range(trial): # trial分だけループ処理
        pass # この部分に具体的な処理を書く
    return average # 関数の戻り値は平均値

# リスト[kaisuu]までの平均値を求める処理
for i in kaisuu:
    print(str(i)+"回試行の平均値："+str(roll_average(i)))