def read_single_digit(digit):
    kornum = {0: '영', 1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
    return kornum[digit]

def read_number(number):
    h = number // 100
    t = (number % 100) // 10
    o = number % 10
    if h == 0:
        if t == 0:
            return read_single_digit(o)
        else:
            if o == 0:
                return read_single_digit(t) + ' '
            else:
                return read_single_digit(t) + ' ' + read_single_digit(o)
    else:
        if t == 0:
            if o == 0:
                return read_single_digit(h) + ' ' + '영' + ' ' + '영'
            else:
                return read_single_digit(h) + ' 영 ' + read_single_digit(o)
        else:
            if o == 0:
                return read_single_digit(h) + ' ' + read_single_digit(t) + ' ' + '영'
            else:
                return read_single_digit(h) + ' ' + read_single_digit(t) + ' ' + read_single_digit(o)

if __name__ == '__main__':
    number = int(input('세 자리 정수 입력: '))
    print(read_number(number))
