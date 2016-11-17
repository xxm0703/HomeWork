import time, math
def recursion(n):
    if n <= 2:
        return 1
    else:
        return recursion(n-1) + recursion(n-2)

def loop(n):
    a = 0
    b = 1
    c = a + b
    while n > 2:
        a = b
        b = c
        c = a + b
        n -= 1
    return c

n = input("Please enter n: ")
n = int(n)
print("Recursion...")
recursion_start = time.time()
print("The %d number of fibonacci is: %d"%(n, recursion(n)))
recursion_end = time.time()
recursion_time = recursion_end-recursion_start
print("Time to execute recursion: {}" .format(recursion_time))
print("\n\n")
print("Loop...")
loop_start = time.time()
print("The %d number of fibonacci is: %d"%(n, loop(n)))
loop_end = time.time()
loop_time = (loop_end - loop_start)
print("Time to execute loop: {}" .format(loop_time))