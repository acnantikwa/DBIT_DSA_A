def reverse_list(lst):
    return lst[::-1]

def rotate_list_left(lst, k):
    if not lst or k == 0:
        return lst
    k = k % len(lst)  # Handle cases where k > len(lst)
    return lst[k:] + lst[:k]

def rotate_list_right(lst, k):
    if not lst or k == 0:
        return lst
    k = k % len(lst)  # Handle cases where k > len(lst)
    return lst[-k:] + lst[:-k]

list= [1, 2, 3, 4, 5]
print(list)
print(reverse_list(list))