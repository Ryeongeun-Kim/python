def get_fixed_price(m):
    discount = int(dis)
    return int(m / ((100 - discount)/ 100))

dis = input('할인율은?')
am = int(input('A 상품의 할인된 가격은?'))
bm = int(input('B 상품의 할인된 가격은?'))
m = am
print('A 상품의 정가는', get_fixed_price(am), '원')
m = bm
print('B 상품의 정가는', get_fixed_price(bm), '원')



