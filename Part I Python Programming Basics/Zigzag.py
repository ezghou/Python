# Write your code here :-)
import time, sys

reset = 20

try:
    while True:
        while reset != 0:
            space = reset
            while space != 0:
                print(' ', end = '')
                space -= 1
            print('****************')
            time.sleep(0.1)

            reset -= 1

        reset += 1

        while reset < 20:
            bar = 5
            reset += 1
            space = reset
            while space != 0:
                print(' ', end = '')
                space -= 1
            print('****************')
            time.sleep(0.1)

        reset -= 1

except KeyboardInterrupt:
    sys.exit()










