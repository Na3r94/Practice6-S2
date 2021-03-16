import datetime


s = int(input())
saat = datetime.timedelta(seconds=s)
print(saat)

import math

Hour = int(input())

H = math.floor(Hour/3600)

Min = Hour - H * 3600

M = math.floor(Min/60)

S = Hour - H * 3600 - M * 60

A = [H , M , S]


Saat = ':'.join(A)

print(Saat)