# import random
# import math

# def numbers():
#     mylist = []
#     cutlist = []

#     for i in range(5):
#         eded_random = random.randint(20, 50)
#         mylist.append(eded_random)
        
#         if eded_random % 2 == 0:
#             a = int(math.pow(eded_random, 2))
#             cutlist.append(a)
    
#     return mylist, cutlist

# random_numbers, number = numbers()
# print("Reqemler:", random_numbers)
# print("Kvadrata yukseldilmis cut reqemler:", number)

# ---------------------------------------------------------------------
# import random
# import math
# def numbers():
#     mylist = [random.randint(20, 50) for  i in range(5)]
#     cutlist = [int(math.pow(num, 2)) for num in mylist if num % 2 == 0]
#     return mylist, cutlist

# random_numbers, number = numbers()
# print("Reqemler:", random_numbers)
# print("Kvadrata yukseldilmis cut reqemler:", number)
