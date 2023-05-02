shopping_bag = []
nums_item = {}

print('[구입]')
while True:
  item = input('상품명? ')
  if item == '' : break
  shopping_bag.append(item)
  nums = int(input('수량은? '))
  print(f'장바구니에 {item} {nums}개가 담겼습니다.')
  nums_item[item] = nums
  print()

print(f'\n>>>장바구니 보기:{nums_item}')
print('\n[검색]')
want = input('장바구니에서 확인하고자 하는 상품은?')
print(f'{want}은(는) {nums_item.get(want)}개 담겨 있습니다.')
