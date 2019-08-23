def pib_m2(n):
    a, b = 1, 0
    while(range(n)):
        a, b = b, a + b
    return b

print(pib_m2(5))