def pib(n):
    if n <= 1:
        return n
    else:
        return (pib(n-1) + pib(n-2))

print(pib(5))