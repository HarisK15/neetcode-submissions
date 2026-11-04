from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    list1 = []
    while len(arr) > 0:
        k = arr[-1]
        list1.append(k)
        arr.pop()
    return list1


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
