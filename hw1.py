def get_radius():
    r = int(input('넓이를 구하고자 하는 원의 반지름은?'))
    return r

get_radius
result = get_radius()
print('반지름', result,'인 원의 넓이 = 3.14 x', result, 'x', result,'=', result*result*3.14)


def get_circle_area(num):
  area = num*num*3.14
  return area

input_num = int(input('넓이를 구하고자 하는 원의 반지름은?'))
result = get_circle_area(input_num)
print('원의 넓이는 :', result)
