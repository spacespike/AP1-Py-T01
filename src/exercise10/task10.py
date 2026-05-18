import sys


def solve():
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        n, target_time = map(int, line1)
        if n < 0 or target_time < 0:
            raise ValueError
    except ValueError:
        print("Error: Invalid input for N or target time")
        return

    machines = []
    for _ in range(n):
        try:
            year, cost, run_time = map(int, sys.stdin.readline().split())
            if cost < 0 or run_time < 0:
                raise ValueError
            machines.append({'year': year, 'cost': cost, 'time': run_time})
        except ValueError:
            print("Error: Invalid machine data")
            return

    min_total_cost = float('inf')
    found = False

    for i in range(n):
        for j in range(i + 1, n):
            m1 = machines[i]
            m2 = machines[j]

            # case: same year  and total time
            if m1['year'] == m2['year'] and (m1['time'] + m2['time'] == target_time):
                current_cost = m1['cost'] + m2['cost']
                if current_cost < min_total_cost:
                    min_total_cost = current_cost
                    found = True

    if found:
        print(float(min_total_cost))


if __name__ == "__main__":
    solve()
