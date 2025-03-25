import math

import funksionetAritm as f #f - shkurtese


#from funksionetAritm import mbledhja

number = math.sqrt(55)

print(round(number,2))

rrezja = 6

perimetri = 2 * math.pi * rrezja
print("Perimetri i rrethit me rreze 6 eshte: ", perimetri)

faktorieli = math.factorial(7)

print("Fakroriel i numrit 7 eshte: ", faktorieli)

print(f.mbledhja(5,6))
print(f.zbritja(5,6))
print(f.shumezimi(5,6))
print(f.pjestimi(5,6))