import matplotlib.pyplot as plt
import numpy as np

pp = []
todouhuken = []

def get():
    for i in range(0, 2):
        k = input()
        n = int(input())
        pp.append(k)
        todouhuken.append(n)
    return pp, todouhuken
        
def graph(pp, todouhuken):
    plt.bar(pp, todouhuken)
    plt.show()


pp, todouhuken = get()
graph(pp, todouhuken)