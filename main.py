import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

# 課題１

def medical_subject():
    d = {}
    get = []

    for page in range(1, 162):
        url = f"http://imuutina.pref.okinawa.lg.jp/searches/result/page:{page}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        page_na = soup.findAll(class_ = "kamoku")

        #リストの要素をdivタグ内のテキストに変換
        for a in page_na:
            get.append(a.text)

        #辞書型に科目をまとめる
        for i in get:
            if i not in d:
                d[i] = 1
            elif i in d:
                d[i] += 1

        #空白の要素を削除    
        del d[""]

        #リスト型に変換
        subject = d.keys()
        number = d.values()
    print(d)

    return subject, number



subject, number = medical_subject()

textprops={"weight":"bold", "color":"white", "size":"large"}
plt.pie(number,
        labels=subject,
        startangle=90,
        counterclock=False,
        rotatelabels=True,
        labeldistance=0.3,
        textprops=textprops,
        radius=2
        )
plt.show()

