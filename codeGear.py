i = 0
while i < 5:
    score = int(input("Enter your score: "))
    if score >= 70:
        print('excellent')
    elif score >= 60:
        print('good')
    elif score >= 50:
        print('fair')
    elif score >= 45:
        print('okay')
    else:
        print('bad')
    i += 1
