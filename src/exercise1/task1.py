vector1 = list(map(float, input().split()))
vector2 = list(map(float, input().split()))
result = 0


def scalar_product(v1, v2, res):
    for i in range(len(v1)):
        res += v1[i] * v2[i]
    print(res)


scalar_product(vector1, vector2, result)
