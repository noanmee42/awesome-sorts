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

# No sort - who even cares about sorting? Let's agree that it's sorted. O(0)
def nosort(arr):
    return arr

# Fastest Unifier of Common Keylists (AKA "FUCK") - fastest sorting algorithm of all time.
# It's so fast u can't access its results. O(-1)
def fuck(arr):
    pass

# non-binary search - since everyone wants to have an identity. O(n)
def nonbinary_search(arr):
    nonbinaries = [6, 7, 42, 52, 67, 69, 161, 228, 420, 666, 777, 1161, 1337, 1488]
    for i in range(len(arr)):
        if arr[i] in nonbinaries:
            return {arr[i]: i}
    