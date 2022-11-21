# N * log2N
def merge_list(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c

def split_and_merge_list(a):
    n = len(a) // 2
    a1, a2 = a[:n], a[n:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)


a = [9, 5, -3, 4, 7, 8, -8]
a = split_and_merge_list(a)

print(a)