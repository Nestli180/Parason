import time
a,b = 1000,7

while True:
    if a > 0:
        print(f'{a} - {b} = {a - b}')
        a -= b
        time.sleep(0.03)
    else:
        break    