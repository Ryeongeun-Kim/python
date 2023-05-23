class Rectangle :
  def __init__(self, x1, y1, x2, y2) :
    self.__x1 = x1
    self.__y1 = y1
    self.__x2 = x2
    self.__y2 = y2
  def show(self):
    print(f'좌측 상단 꼭지점이 ({self.__x1}, {self.__y1})이고 우측 상단 꼭지점이 ({self.__x2}, {self.__y2})인 사각형입니다.')
  def getWidth(self):
    width = self.__x2 - self.__x1
    return width

  def getHeight(self):
    height = self.__y2 - self.__y1
    return height

  def getArea(self):
    area = (self.__x2 - self.__x1) * (self.__y2 - self.__y1)
    return area
  def getPerimeter(self):
    perimeter = (self.__x2 - self.__x1)*2 + (self.__y2 - self.__y1)*2
    return perimeter


r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'넓이는 {a}, 둘레는 {p}')
