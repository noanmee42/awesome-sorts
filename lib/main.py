from random import randint
from time import sleep
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

# LGBTQuickSort - no natural numbers around here. O(n log(n))
def is_natural(n):
    if type(n) == int and n > 0:
        return True
    return False

def lgbtquicksort(arr):
    non_natural = [x for x in arr if not is_natural(x)]
    return sorted(non_natural)

# homofobian sort - only naturals. O(n log(n))
def homofobian_sort(arr):
    natural = [x for x in arr if is_natural(x)]
    return sorted(natural)

# Jesus sort - everything is wine. he can randomly die tho. Maybe it won't be sorted at all that's not my fault judge him O(n)
def jesusort(arr):
    for i in range(len(arr)):
        if randint(0, 100) == 42:
            return arr
        arr[i] = "wine"
    return arr

# Buddha Sort - yeah you'll definetely get sorted array. Eventually. O(n log n) + 49 days
def buddhasort(arr):
    arr = sorted(arr)
    print("Almost done! Hold on...")
    sleep(4_234_000)
    return arr