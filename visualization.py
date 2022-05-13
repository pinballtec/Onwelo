import numpy as np
import matplotlib.pyplot as plt
import csv
from heapq import nlargest
filename = 'Demo3.csv'
with open(filename) as f:
    reader = csv.reader(f)

    header_row = next(reader)

    for row in reader:
        dollar = row[5:11]
        dollar = np.array(dollar)

    # dollar = [float(i) for i in dollar]

    res = nlargest(5, dollar)
    print(res)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    z1 = [-5, -10, -15, -20, -30]
    plt.bar(res, z1)
    plt.title("", fontsize=24)
    plt.xlabel('value', fontsize=16)
    plt.ylabel("valuation", fontsize=16)
    plt.tick_params(axis='both', which="major", labelsize=16)

    plt.show()



