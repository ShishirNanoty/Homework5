primenos = [2]
print(1)
print('Prime',2)
def ckPrime(i):
    prm_ini = True
    prm_sec = True
    for nos in primenos:
        # print('in for', i,nos)
        if prm_ini == True and prm_sec == True:
            # print('in if prm')
            while i % nos == 0:
                prm_sec = False
                # print('in while', nos)
                break
    if prm_sec == False:
        prm_sec = False
        # print('NP',i)
    else:
        prm_sec = True
        primenos.append(i)
        # print('P',i)
    return prm_sec
    # print(primenos)
for i in range(3,101):
    x = ckPrime(i)
    if x == True:
        print("Prime",i)
    # For FizzBuzz print
    elif i%3 == 0 and i%5 ==0:
        print('FizzBuzz',i)
    elif i%5 == 0:
        print('Buzz',i)
    elif i%3 == 0:
        print('Fizz',i)
    else: print(i)
