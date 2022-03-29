command = input('>').lower()
previous_command = "" 
while command != 'quit':
    if command == 'help':
        print('''
              start - to start
              stop - to stop 
              quit - to quit''')
    elif command == 'start':
        if previous_command == 'start':
            print('the car has started')
        else:
            print('Car started!')
    elif command == 'stop':
        if previous_command == 'stop':
            print('the car has stopped')
        else:
            print('stop')
    else: 
        print('I do not understand.')

    if command == 'start'or command == 'stop':
        previous_command = command
    command = input('>').lower()
else: 
    print('you quit the game')
        