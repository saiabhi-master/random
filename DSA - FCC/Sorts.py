def merge_sort(list):
    """
    Sorts a given list in an ascending order
    Returns a new sorted list
    Overall run time - O(kn log n) - split X merge
    Space complexity - linear
    """
    # split - Runs in O(k log n) - logarithmic time
    # k - because of slicing ( not constant )

    # merge - O(n) - linear time
    #  space : at most will require 'n', it goes through left half first, deletes after each step

    if len(list) <= 1:
        return list
    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - Left and Right
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    # to fix: take away slicing

    return left, right

def merge(left, right):
    """
    merges two lists sorting them in the process
    and returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

listy = [54, 79, 30]
listy = merge_sort(listy)
print(verify_sorted(listy))










