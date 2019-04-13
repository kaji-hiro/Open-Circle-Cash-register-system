import csv
from function import cloth_price
from function import magazine

status = 'y'
fee_sum = 0
price_list = []
while status == 'y':
    price = cloth_price()
    if price == 'error':
        print('続けますか？　はい：y\n　　　 　　　 いいえ：n')
        status = input()
    else:
        fee_sum += price
        price_list.append(price)
        print('続けますか？　はい：y\n　　　 　　　 いいえ：n')
        status = input()

fee_sum += int(magazine())
print('\n')

print('合計金額:', fee_sum)
get_money = 0
get_money = int(input('お預かり金額:'))
while get_money < fee_sum:
    print('足りません')
    get_money = int(input('お預かり金額:'))

print('お釣り:', get_money - fee_sum)
