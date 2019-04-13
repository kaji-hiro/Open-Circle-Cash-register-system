import csv

def cloth_price():
    status = 'normal'
    clothes_list = []
    clothes_num = []

    with open('clothdata.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            clothes_list.append(row)

    for i in range(len(clothes_list)):
        clothes_num.append(int(clothes_list[i][0]))

    soldcloth_num = int(input('商品番号:'))

    try:
        selling_num = clothes_num.index(soldcloth_num)
        if clothes_list[selling_num][7] == 'sold out':
            print("この商品はすでに売却されました")
            return_value = 'error'
        else:
            x = 'y'
            print('販売団体:{0}\n部類　　:{1}\nブランド:{2}\n色　　　:{3}\n値段　　:{4}\n'.format(clothes_list[selling_num][1], clothes_list[selling_num][3], clothes_list[selling_num][4], clothes_list[selling_num][5], clothes_list[selling_num][6]))
            x = input('正しい:y\n間違い:n\n')
            if x == 'y':
                return_value = int(clothes_list[selling_num][6].replace(',', ''))
                clothes_list[selling_num][7] = 'sold out'
                # ファイルにsold outを書き込み
                with open('clothdata.csv', 'w', encoding="utf-8") as f:
                    writer = csv.writer(f, lineterminator='\n')
                    writer.writerows(clothes_list)
            else:
                return_value = 'error'
    except ValueError:
        print('その番号の商品はありません')
        return_value = 'error'

    return return_value

def magazine():
    return_value = 0
    clothes_list = []

    with open('clothdata.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            clothes_list.append(row)

    if int(clothes_list[-1][7]) > 0:
        print('雑誌を買いますか？　はい：y\n　　　 　　　 いいえ：n')
        x = input()
        if x == 'y':
            clothes_list[-1][7] = int(clothes_list[-1][7]) - 1
            # ファイルの販売数をデクリメント
            with open('clothdata.csv', 'w', encoding="utf-8") as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerows(clothes_list)
            return_value = 500

    return return_value
