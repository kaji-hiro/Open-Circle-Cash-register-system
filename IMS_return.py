import csv

clothes_list = []
clothes_num = []

with open('clothdata.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        clothes_list.append(row)
for i in range(len(clothes_list)):
    clothes_num.append(int(clothes_list[i][0]))

return_num = int(input('返品商品番号:'))
return_money = 0

try:
    returning_num = clothes_num.index(return_num)
    if clothes_list[returning_num][7] == 'selling':
        print("この商品は販売中です")
    else:
        clothes_list[returning_num][7] = 'selling'
        return_money += int(clothes_list[returning_num][6].replace(',', ''))
except ValueError:
    print('その番号の商品はありません')
    return_value = 'error'

print('返金額:', return_money)

# ファイルにsold outを書き込み
with open('clothdata.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(clothes_list)
