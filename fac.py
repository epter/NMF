import csv
import numpy as np

row2 = list() 
mapp = np.zeros((400,400))              # 配列数　400ⅹ400　배열수 
countzero = 0                           # 訪れなかった箇所の数 시작 수
maxcount = 2365                         # 총 배열의 수를 기입 

csvfile = open("allpd.csv", encoding="shift-jis")  #CSVファイルの読み込み
for row in csv.reader(csvfile):
    print(row)
    row2.append(row)

for i in range(0,400):
    for j in range(0,400):
        for k in range(0,maxcount):
            if i == int(row2[k][2]) and j == int(row2[k][3]):
                mapp[i][j] += 1
                print(i,j)
        # if mapp[i][j] == 0:
            # countzero += 1
# print(9600 - countzero)


csvfile2 = open("apdhikone.csv","w",encoding="shift-jis")
writer = csv.writer(csvfile2)
writer.writerows(mapp)
