x = 1
y = 1
print('turtle pose: [1, 1]')
while True:
  print('Enter command (up, down, left, right): ', end = '')
  oper = input()
  if oper == 'up':
    y += 1
  elif oper == 'down':
    y -= 1
  elif oper == 'left':
    x -= 1
  elif oper == 'right':
    x += 1
  else:
    print("Invalid command, please try again")
    continue
  print('New turtle pose: ['+str(x)+', '+str(y)+']')

    
