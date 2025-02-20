import random

# Three different ways to generate a random Boolean
bool1 = random.choice([True, False])
bool2 = bool(random.getrandbits(1))
bool3 = random.randint(0, 1) == 1

print(bool1, bool2, bool3)
