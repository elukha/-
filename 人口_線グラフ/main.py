import csv
import itertools
import matplotlib.pyplot as plt

calendar = []
population = []

def country():
    # C:\\Users\\kidz8\\Desktop\\Python\\mekaru\\kadai4\\export.csv
    # CSVを2次元配列に変換
    filename = "export.csv"
    with open(filename, encoding="utf-8", newline="") as f:
        csvreader =csv.reader(f)
        content = []
        for row in csvreader:
            content.append(row)

    # 2次元配列を1次元に直す
    data = list(itertools.chain.from_iterable(content))

    # 西暦と人口に分ける
    for i in range(len(data)):
        if i % 2 == 0:
            calendar.append(int(data[i]))
        else:
            population.append(int(data[i]))
    return population, calendar


def ranking(population, calendar):
    d = {}
    datalist = []
    for i in range(len(population)):
        d[population[i]] = calendar[i]
    population.sort()
    for n in range(1, 6):
        datalist.append(str(n) + "位: " + str(calendar[n]) + "年" + "\n")

    return datalist


def write_text(datalist):
    f = open("rainkingu.txt", "w", encoding="UTF=8")
    f.writelines(datalist)
    f.close

population, calendar = country()
datalist = ranking(population, calendar)
write_text(datalist)


# 折れ線グラフ出力
plt.plot(population, calendar)
plt.savefig("data.png")
plt.show()