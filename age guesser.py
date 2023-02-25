#Can guess your age provided if you give the right inputs :)
down = 0
up = 100

for i in range(1,10):
    guessed_age = int((up+down)/2)
    answer = input('Are you ' + str(guessed_age) + 'years old? ')

    if answer == 'correct' :
        print("Nice")
        break
    elif answer == 'No, it\'s less' :
        up = guessed_age
    elif answer == 'No it\'s more' :
        down = guessed_age
    else :
        print('Wrong Answer')