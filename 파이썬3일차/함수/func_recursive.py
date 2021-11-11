# def count(num):
#     if num >= 1:
#         print(num, end=' ')
#         count(num - 1)
#     else:
#         return


# count(10)
# count(20)


# def factorial(num):
#     if num <= 1:
#         return num
#     else:
#         return num * factorial(num - 1)


# print(factorial(4))
# print(factorial(10))

def genFunc():
    yield 1
    yield 2
    yield 3


print(list(genFunc()))
