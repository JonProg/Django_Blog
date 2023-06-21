import string as s
import random

print(''.join(random.choices(s.ascii_letters + s.digits + s.punctuation, k=64))) 