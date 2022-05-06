import random

while True:
  try:
    b = input("Введите имя файла: ")
    l = open(b,'r')
    c = 'ШFM{8щЬнDмhmPКо}UJAРk,чa0g;&сWwыцЫдRлЦЕЖ!]@=-Мp"d(БXА)+O3Эя|Ё6[рСй7е%<qbjt9ЗВэxYriтёKcЪEyS?№HИBzVу5ДLZ_шЮ хиfuьn4жЙФз2/#вЧQЯlпкюГаIПТo1TЛGeъН>\:УХОЩNs*бvгCф.'
    d = int(input("Выберите операцию - 1) Шифрование; 2) Дешифрование: "))
    
    e = l.read()
    res = []
    len_c = len(c)

    if (d == 1):
      a = random.randint(1, 1000)
  
      for i in e:
        res.append(c[(c.find(i)+a)%len_c])
      print('Файл успешно зашифрован, a ключ записан в key.txt\n')

      f = open('key.txt','w')
      f.write(str(a))
      f.close()

      r = open(b,'w')
      u = ''.join(res)
      r.write(u)
      r.close()

    elif (d == 2):
      a = int(input("Введите ключ: "))
  
      for i in e:
        res.append(c[(c.find(i)-a)%len_c])
      print('Файл успешно расшифрован.\n')

      r = open(b,'w')
      u = ''.join(res)
      r.write(u)
      r.close()
      
    else:
      print('Данной операции нет.\n')

  except FileNotFoundError:
    print("Файл не найден.\n")