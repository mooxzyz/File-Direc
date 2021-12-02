import random
import time
import os

def proc(i, chance):
    num = int(input('Number: '))
    if num <= 10:
        print(f'i = {i}')
        print(f'chance = {chance}')
        print(f'num is {num}')
        time.sleep(3)
        num1 = random.randint(1,10)
        while True:
            time.sleep(0.1)
            if num != num1:
                num1 = random.randint(0, 10)
                print(num1)
                chance += 1
            else:
                break
        print('--------------------------------')
        print(f'{num} is a 1/{chance} chance')
        print("""
        Would You Like To Play Again?
        (y/n)
        ---------------------------------------
        """)
        yn = input('y/n: ').lower()
        if yn == 'y':
            os.system('cls')
            proc(0, 0)
        else:
            print('ok')
            time.sleep(5)
    else:
        print('error')

proc(0, 0)


