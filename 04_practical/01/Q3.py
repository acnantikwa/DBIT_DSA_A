def countdown_head_recursion(n, result=None):
    if result is None:
        result = []
    if n < 0:
        return result
    result.append(n)
    return countdown_head_recursion(n - 1, result)