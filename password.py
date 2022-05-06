import random

while True:
  password = ''
  sum = int(input('Введите количество символов для пароля: '))
  symbol = input('Введите символы из который будет состоять пароль: ')

  for x in range(sum):
      password = password + random.choice(list(symbol)) 
  print('Сгенерированный пароль: ', password, "\n")