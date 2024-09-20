import random

qstn = input('Question: ')

nro = random.randint(1,8)

if nro == 1:
  print('Magic 8 Ball:  Yes - definitely.')
elif nro == 2:
  print('Magic 8 Ball:  It is decidedly so.')
elif nro == 3:
  print('Magic 8 Ball:  Without a doubt.')
elif nro == 4:
  print('Magic 8 Ball:  Reply hazy, try again.')
elif nro == 5:
  print('Magic 8 Ball:  Ask again later.')
elif nro == 6:
  print('Magic 8 Ball:  Better not tell you now.')
elif nro == 7:
  print('Magic 8 Ball:  Outlook not so good.')
elif nro == 8:
  print('Magic 8 Ball:  Very doubtful.')