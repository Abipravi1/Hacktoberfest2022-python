latitude = 2818.647579
longitude = 07700.768767

def convertDMtoDD(value):
     value = value%100
     value_fraction = value 
     value_dd = value_fraction*100/60
     print(value_dd)
     return value_dd
convertDMtoDD(latitude)
print("\n")
convertDMtoDD(longitude)
