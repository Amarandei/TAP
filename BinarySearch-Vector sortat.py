def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		if arr[mid] < x:
			low = mid + 1

		elif arr[mid] > x:
			high = mid - 1

		else:
			return mid

	return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, x)

if result != -1:
	print('Key found', str(result))
else:
	print('Key not found')