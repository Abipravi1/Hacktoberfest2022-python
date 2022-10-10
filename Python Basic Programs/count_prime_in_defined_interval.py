# Tanggal: 29 September 2022
# Deskripsi: Menentukan banyak bilangan prima dan bilangan prima terbesar dari rentang bilangan bulat yang di-input oleh user

# KAMUS
# a, b, max_prime, count, i, k : int
# prime : bool

# ALGORITMA
# input
a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))

# set initial condition
max_prime = 0
count = 0

for i in range(a, b+1): # start loop from a to b
    prime = True # set the initial prime condition to true
    k = 2 # k starts from 2 because dividing by 1 isn't necessary
    while(prime and k <= i): # will loop from 2 to i or until prime is false
        if i % k == 0 and k != i: prime = False # set the prime condition to false if it can be divided by k
        k += 1 # don't forget to increment k so that the loop can be stopped at some point i.e k = i+1
    
    if prime and i != 1: # 1 is not prime
        max_prime = i
        count += 1
        
# output
if count > 0:
    print("Banyaknya bilangan prima pada selang [{}, {}] adalah {}. Bilangan prima terbesar di selang tersebut adalah {}.".format(a, b, count, max_prime))

else:
    print("Tidak ditemukan bilangan prima pada selang [{}, {}]".format(a, b))
