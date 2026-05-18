def get_matrix():
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()
            matrix = [list(map(int, line.split())) for line in lines if line.strip()]
            return matrix

    except FileNotFoundError:
        return None


matrix = get_matrix()
n = len(matrix)

visited = [[False] * n for _ in range(n)]


def dfs(i, j):
    stack = [(i, j)]
    cells = []

    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue

        visited[x][y] = True
        cells.append((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    stack.append((nx, ny))

    return cells


squares = circles = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            comp = dfs(i, j)

            xs = [x for x, y in comp]
            ys = [y for x, y in comp]

            h = max(xs) - min(xs) + 1
            w = max(ys) - min(ys) + 1

            if h == w and len(comp) == h * w:
                squares += 1
            else:
                circles += 1

print(squares, circles)
