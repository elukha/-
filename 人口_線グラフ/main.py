import csv
import itertools
import matplotlib.pyplot as plt

# CSVを2次元配列に変換
filename = "export.csv"
with open(filename, encoding="utf-8", newline="") as f:
    csvreader =csv.reader(f)
    content = []
    for row in csvreader:
        content.append(row)

# 2次元配列を1次元に直す
data = list(itertools.chain.from_iterable(content))


calendar = []
population = []

# 西暦と人口に分ける
for i in range(len(data)):
    if i % 2 == 0:
        population.append(int(data[i]))
    else:
        calendar.append(int(data[i]))

# 折れ線グラフ出力
plt.plot(population, calendar)
plt.show()