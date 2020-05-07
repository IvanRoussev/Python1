def check_geuss(geuss, answer):
    global score
    still_geussing = True
    attempt = 0
    while still_geussing and attempt < 3:
        if geuss.lower() == answer.lower():
            print('correct Answer')
            score = score + 1
            still_geussing = False
        else:
            if attempt < 2:
                geuss = input('sorry wrong answer. Try again ')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct answer is ' + answer)

score = 0
print('geuss the Animal')
geuss1 =input('Which bear lives in the north pole? ')
check_geuss(geuss1, 'polar bear')
geuss2 = input('Which is the fastest land Animal ')
check_geuss(geuss2, 'cheetah')
geuss3 = input('Which is the largest animal? ')
check_geuss(geuss3, 'blue whale')

print('Your score is ' + str(score))
