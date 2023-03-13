def get_radius():
    r = int(input('넓이를 구하고자 하는 원의 반지름은?'))
    return r

def get_circle_area(s):
  area = s*s*3.14
  return area

s = get_radius()
result = get_circle_area(s)
print('원의 넓이는 :', result)
