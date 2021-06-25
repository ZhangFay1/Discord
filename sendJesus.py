import random
from jesusWords import jesus

def get_jesus():
  n = random.randrange(len(jesus))
  return jesus[n]