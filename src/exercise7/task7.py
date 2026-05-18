def solve():
    try:
        n, m = map(int, input().split())

        field = []

        for _ in range(n):
            row = list(map(int, input().split()))

            if len(row) != m:
                return "Error: Invalid row size."

            field.append(row)
        # field = [list(map(int, input().split())) for _ in range(n)]

    except ValueError:
        return "Error: Invalid input format."

    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = field[0][0]
    # Row 1
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + field[0][j]

    # Column 1
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + field[i][0]

    # Remaining
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + field[i][j]

    return (dp[n - 1][m - 1])


print(solve())
