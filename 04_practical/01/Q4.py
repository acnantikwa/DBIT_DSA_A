def sum_tail_recursion(n, accumulator=0):
    if n <= 0:
        return accumulator
    return sum_tail_recursion(n - 1, accumulator + n)

print(sum_tail_recursion(5))
