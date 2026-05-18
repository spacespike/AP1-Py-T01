def different_numbers(n: int) -> int:
    numbers = list(int(input()) for _ in range(n))
    unique_numbers = set(numbers)
    return len(unique_numbers)


n = int(input())
answer = different_numbers(n)
print(answer)
