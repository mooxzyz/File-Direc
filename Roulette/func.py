import random

def thegame():
    print(f'Your Selected Number Is: {number}')
    time.sleep(4)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    print(random.randint(1,10))
    time.sleep(0.1)
    finalnumber = print(random.randint(1,10))
    if finalnumber == number:
        os.system('shutdown /p')
    else:
        print("""
        Luck
        Play Again?
        (y/n)
        """)
        playagain = str(input('y/n: ')).lower()
        if playagain == 'y':
            thegame()
        elif playagain == 'n':
            print('ok')
            time.sleep(3)
        else:
            print('Answer treated as n')

def hello():
    print('hello world')
