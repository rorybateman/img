import random
import os
import subprocess

a = str(random.randint(1,10))
b = "\npython3 image.py "
c = b + a +".jpg"

print(c)
os.system(c)
