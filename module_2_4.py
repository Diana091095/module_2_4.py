numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(len(numbers)):
     print(numbers[i])
     x = numbers[i]
     if x > 1:
         for i in range(2, (x // 2) + 1):
             if x % i == 0:
                 print("число не простое")
                 break
         else:
             print("число простое")
     else:
         print("число не простое")

primes = [2, 3, 5, 7, 11, 13]
print('primes ', primes)
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]
print('not_primes ', not_primes)


# ПОЖАЛУЙСТА, СМОТРИТЕ ВЫШЕ.КОД НИЖЕ ОСТАВЛЕН КАК НАПОМИНАНИЕ. БЛАГОДАРЮ.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# for i in range(len(numbers)):
#     print(numbers[i])
#     x = numbers[i]
#     for i in range(2, x):
#         if x % i == 0:
#             print('число не простое')
#         else:
#             print('число простое')





