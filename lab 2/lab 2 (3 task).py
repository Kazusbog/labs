def prime(n):
    for x in range(2,n):
        if n%x==0:
            return 0
        else:
            return 1
print(prime(5))