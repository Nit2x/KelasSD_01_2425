def deret(n, m=None, i=2):
    if (m is None):
        m = n
    print(n, end=" ")  
    if n == 1 or i>m:
        return 
    elif n % 3 == 0:
        deret(n // 3, m, i + 1)
    else:
        deret(2 * n + 1, m, i + 1)

deret(6)
print()
deret(12)
