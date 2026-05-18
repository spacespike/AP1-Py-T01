def solve():
    try:
        first_line = input().split()
        if not first_line:
            return
        n = int(first_line[0])
        x_val = float(first_line[1])

        coefficients = []
        while len(coefficients) < n + 1:
            line = input().split()
            if not line:
                break
            coefficients.extend([float(c) for c in line])

        if len(coefficients) < n + 1:
            return

        # Horner's method
        derivative_sum = 0.0
        polynomial_sum = 0.0

        for i in range(n):
            polynomial_sum = polynomial_sum * x_val + coefficients[i]
            derivative_sum = derivative_sum * x_val + polynomial_sum

        print(f"{derivative_sum:.3f}")

    except EOFError:
        pass


if __name__ == '__main__':
    solve()
