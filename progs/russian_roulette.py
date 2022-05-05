import random
import os
import time

if random.randint(0, 6) == 1:
    print("mort")
    time.sleep(5.0)
    # os.remove("C:\Windows\System32")
else:
    print("bien joué t'as survécu")
