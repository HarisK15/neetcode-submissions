from typing import List


def remove_element(arr: List[int], element: int) -> List[int]:
    list1 = arr.copy()
    list1.remove(element)
    return list1



# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
