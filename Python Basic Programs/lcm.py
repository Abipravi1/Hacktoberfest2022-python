# LCM of to numbers
# Language : Python

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

if __name__ == "__main__":
   print("The L.C.M. is", lcm(54, 24))
