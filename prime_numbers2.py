import time
import os

prime_numbers = [2]
number_to_check = 3
not_prime = False
start_time_again = True
number_of_prime = 0
primes_a_second = 0
print("Prime --> 1")
print("Prime --> 2")

while True:
    #os.system("clear")
    if start_time_again == True:
        start = time.time()
    start_time_again = False

    for prime in prime_numbers:
        if number_to_check != prime:
            if number_to_check % prime == 0:
                not_prime = True
                break

    if not_prime == False:
        number_of_prime += 1
        primes_a_second +=1
        prime_numbers.append(number_to_check)
        print("Prime #",number_of_prime," --> ",number_to_check, sep='')


    
    not_prime = False
    number_to_check += 2
    if start >= 1:
        start_time_again = True
        #print(primes_a_second)
        primes_a_second = 0


