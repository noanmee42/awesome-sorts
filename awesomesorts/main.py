from random import randint, shuffle
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

# CPython's Undeniable Notable Tuff Sort but cooler (CUNT but cooler). O(n log(n))
def cunt(arr):
    return sorted(arr)

# Anti-bogosort - lowkey like bogosort, but anti.
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def antibogosort(arr):
    if len(arr) == 1:
        return "bro fuck you"
    while True:
        shuffle(arr)
        if not is_sorted(arr):
            return arr

# Miracle Sort. "He said "Somehow, Someway it's gonna get ..."" (C) Rod Stewart. O(∞)
def miracle_sort(arr):
    if len(arr) == 1:
        return arr
    while True:
        sleep(1)
        if is_sorted(arr):
            return arr


# Binary sort. Sorts all 0s and 1s in the array. O(n)
def binary_sort(arr):
    arr01 = []
    for i in range(len(arr)):
        if arr[i] == 1:
            arr01.append(1)
        elif arr[i] == 0:
            arr01.insert(0, 0)
    return arr01

