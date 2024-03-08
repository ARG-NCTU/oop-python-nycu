def turtle_move():
    turtle_position = [1,1]
    print('turtle position: ',turtle_position)
    while True:
        move = input('Enter command (up, down, left,right):')
        if move == 'up':
            turtle_position[1]+=1
            print('tutle position: ',turtle_position)
        elif move == 'right':
            turtle_position[0]+=1
            print('tutle position: ',turtle_position)
        elif move == 'down':
            turtle_position[1]-=1
            print('tutle position: ',turtle_position)
        elif move == 'left':
            turtle_position[0]-=1
            print('tutle position: ',turtle_position)
        elif move == 'end':
            break
        else:
            print('Invalid command, please try again')

turtle_move()
