def primeornot():
    flg = False
    if i == 2:
        print('Prime',2)
    elif i > 1:
        for j in range(2,i):
            if i%j == 0:
                # print(i)
                flg = True
                return flg
                break
            else:
                print('Prime',i)
                break
    else: print(i)
for i in range(1,21):
    # print(i)
    if i%3 == 0 and i%5 ==0:
        print('FizzBuzz',i)
        x = primeornot()
        if x == False:
            print(i)
    elif i%5 == 0:
        print('Buzz',i)
        x = primeornot()
        if x == False:
            print(i)
    elif i%3 == 0:
        print('Fizz',i)
        x = primeornot()
        if x == False:
            print(i)
    else:
        x = primeornot()
        if x == True:
            print(i)
