def multiplicative_num(*args):
    multiplicative = 1
    for item in args:
        multiplicative *= item
    return multiplicative

print(multiplicative_num(1,2,3))
