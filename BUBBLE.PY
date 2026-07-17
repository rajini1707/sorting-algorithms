arr = []
print("Enter 5 numbers:")
for i in range(5):
    arr.append(int(input()))

for i in range(5):
    for j in range(0, 4 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)