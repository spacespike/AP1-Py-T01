import math

try:
    rows = int(input())
    if rows <= 0:
        print("Natural number was expected")
    else:
        def combination(n):
            for k in range(n + 1):
                print(int((math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))), end=' ')


        for i in range(rows):
            combination(i)
            print()


except  ValueError:
    print("Natural number was expected")
