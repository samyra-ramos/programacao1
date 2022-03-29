guess_secret = 13

guess_count = 0

while guess_count < 5:
    guess = int(input('Guess: '))
    guess_count = guess_count + 1
    if guess == guess_secret: 
        print('Congrats')
        break 
else: 
    print('Try again')
    

