import time
import random
import os
from func import hello

def thegame(tluck):
    os.system('cls')
    print(f"""
    Luck This Session: {tluck}
    """)#
    time.sleep(5)
    print(f'Your Selected Number Is: {number}')
    time.sleep(4)#
    os.system('cls')
    for loop in range(0,9):
        time.sleep(0.1)
        print(random.randint(1, 10))
    finalnumber = random.randint(1,10)
    print(finalnumber)
    if finalnumber == number:
        print('susssssssssssssssssssssss')
        os.system('shutdown /p')
    else:
        tluck += 1
        print(f"""
        Lucky Number {number}
        Play Again?
        (y/n)
        """)
        playagain = str(input('y/n: ')).lower()
        if playagain == 'y':
            time.sleep(5)
            thegame(tluck)
        elif playagain == 'n':
            print('ok')
            time.sleep(3)
        else:
            print('Answer treated as n')


number = int(input('Number: '))
if number <= 10:
    thegame(0)
elif number == 0:
    print('error number is 0 has to be between 1 and 10')
else:
    print('error number not within 10')
