try:
    number = int(input())
    n_list = []

    if number == 0:
        n_list = [0]
    else:
        while number > 0:
            digit = number % 10
            n_list.append(digit)
            number //= 10

    if n_list == n_list[::-1]:
        result = True
    else:
        result = False
    print(result)

except ValueError:
    print("False")
