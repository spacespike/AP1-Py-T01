def string_to_float(s):
    s = s.strip()
    if not s:
        return None

    # Handle sign
    sign = 1.0
    if s[0] == '-':
        sign = -1.0
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # Check for empty string after sign removal
    if not s:
        return None

    # Split into integer and fractional parts
    parts = s.split('.')
    if len(parts) > 2:
        return None

    int_part = parts[0]
    frac_part = parts[1] if len(parts) > 1 else ""

    # Validate that parts consist only of digits
    if int_part and not int_part.isdigit():
        return None
    if frac_part and not frac_part.isdigit():
        return None
    if not int_part and not frac_part:
        return None

    # Convert integer part manually using ASCII values
    # Formula: result = (result * 10) + current_digit
    res = 0.0
    for char in int_part:
        res = res * 10 + (ord(char) - ord('0'))

    # Convert fractional part manually
    # Formula: result += current_digit / (10 ^ position)
    if frac_part:
        divisor = 10.0
        for char in frac_part:
            res += (ord(char) - ord('0')) / divisor
            divisor *= 10

    return res * sign


def main():
    input_str = input().strip()

    result = string_to_float(input_str)

    if result is None:
        print("Error: Invalid input format.")
    else:
        # Multiply by 2 and print with 3 digits after the dot
        final_value = result * 2
        print(f"{final_value:.3f}")


if __name__ == "__main__":
    main()
