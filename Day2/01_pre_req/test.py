import sys
max_length = 10000
square_list = [x**2 for x in range(max_length)] # comprehension
# sizeof
print("list size:",sys.getsizeof(square_list))
print("sum of list:",sum(square_list))
print("="* 60)
square_gen = (x**2 for x in range(max_length)) # generator
print("generator size:",sys.getsizeof(square_gen))
print("sum of generator:",sum(square_gen))
