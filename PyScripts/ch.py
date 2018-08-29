def even(a):
    for i in range(1, len(a)):
        if a[i] % 2 == a[i-1] % 2:
            return False
    return True
