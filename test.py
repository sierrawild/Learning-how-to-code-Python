def factorio(n):
    if n == 1:
        return 1
    else:
        return n * factorio(n -1)
    

print(factorio(4))