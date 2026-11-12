def fib(num):
    if num-1 < 2:
        return num-1
    return fib(num-1) + fib(num-2)


def surrogate(max_num):
    print("1. Apple")
    yield fib(1)
    print("2. Applu")
    yield fib(2)
    print("3. Appllu")
    yield fib(3)
    print("4. Appellu")
    yield fib(4)

# import time
# for res in surrogate(5):
#     print(res)
#     time.sleep(1)
gen = surrogate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))