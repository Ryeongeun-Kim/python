def exchange(amount):
  m500 = amount // 500
  amount %= 500
  m100 = amount // 100
  amount %= 100
  m50 = amount // 50
  amount %= 50
  m10 = amount // 10
  print('500원 동전의 개수:', m500)
  print('100원 동전의 개수:', m100)
  print('50원 동전의 개수:', m50)
  print('10원 동전의 개수:', m10)

def get_integer(prompt):
  res = int(input(prompt))
  return res

question = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(question)
