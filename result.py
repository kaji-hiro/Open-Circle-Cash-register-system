import csv

x = 1
clothes_list = []
clothes_status = []
clothes_num = []
group = [0,0,0,0,0,0,0,0]

with open('clothdata.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        clothes_list.append(row)

for i in range(len(clothes_list)):
    clothes_status.append(clothes_list[i][7])

for i in range(len(clothes_list)):
    clothes_num.append(int(clothes_list[i][0]))

for i in range(8):
    for j in range(len(clothes_num)):
        if clothes_status[j] == 'sold out':
            group[i] += int(clothes_list[j][6].replace(',', ''))
        if int(clothes_list[j][0]) / 1000 > x:
            x += 1
            break

print('売上総額')

print('Unfowld  :', group[0])
print('Keio     :', group[1] - group[0])
print('Uni–Share:', group[2] - group[1])
print('Add      :', group[3] - group[2])
print('FDL      :', group[4] - group[3])
print('ENJI     :', group[5] - group[4])
print('AFA      :', group[6] - group[5])
print('Replus   :', group[7] - group[6])
