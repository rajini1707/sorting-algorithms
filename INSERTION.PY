arr = []
print("Enter 5 numbers:")
for i in range(5):
    arr.append(int(input()))

for i in range(1, 5):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted array:", arr)