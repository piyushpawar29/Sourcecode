def binary_search(arr, x):
  """
  Performs binary search on a sorted array to find the index of a target element.

  Args:
    arr: The sorted array.
    x: The target element to search for.

  Returns:
    The index of the target element if found, otherwise -1.
  """

  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      low = mid + 1
    else:
      high = mid - 1

  return -1

# Example usage
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, x)

if result != -1:
  print("Element is present at index", str(result))
else:
  print("Element is not present in array")
