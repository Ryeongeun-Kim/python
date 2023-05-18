def buy(bag) :
    print('[구입]')
    item = input('상품명? ')

    if item == '' :
        return False
    else :
        num = input('수량은? ')
        bag[item] = num
        print(f'장바구니에 {item} {num}개가 담겼습니다.')
        print()
        
def show(bag) :
    print()
    print('>>>장바구니 보기:', bag)
    print()
    
def find(bag) :
    print('검색')
    find = input('장바구니에서 확인하고자 하는 상품은? ')
    if find in bag :
        print(f'{find}은(는) {bag[find]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {find}은(는) 없습니다.')

shopping_bag = {}

while True :
    if buy(shopping_bag) == False :
        break

show(shopping_bag)
find(shopping_bag)
