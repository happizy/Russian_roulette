# Russian_roulette

## Un programme qui détruit le pc windows avec une probabilité de 1/6

---

# à vos risques et périls (à exécuter en tant qu'admin) :

```py
import random
import os

if random.randint(0, 6) == 1:
    print("mort")
    # os.remove("C:\Windows\System32")
else:
    print("bien joué t'as survécu")
```
