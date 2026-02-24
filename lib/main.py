# Communisort (v1) - everyone gets mean
def communisort(arr):
    eq = round(sum(arr) / len(arr))
    for i in range(len(arr)):
        arr[i] = eq
    return arr