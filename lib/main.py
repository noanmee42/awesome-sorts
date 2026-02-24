# Communisort (v1) - everyone gets mean. O(n)
def communisort(arr):
    eq = round(sum(arr) / len(arr))
    for i in range(len(arr)):
        arr[i] = eq
    return arr

# Communisort (v2) - everyone gets nothing. O(1)
def communisort_v2(arr):
    new_array = []
    return new_array

# Nosort - who even cares about sorting? Let's agree that it's sorted. O(0)
def nosort(arr):
    return arr

# FastestUnifier_ofCommonKeylists (AKA "FUCK") - fastest sorting algorithm of all time.
# It's so fast u can't access its results. O(-1)
def fuck(arr):
    pass

