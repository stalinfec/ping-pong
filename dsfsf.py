sl =  [450, 520, 610, 400]

def increse(number):
 return round(number * 1.12)

sl_12 = list(map(increse, sl))

print(sl_12)

