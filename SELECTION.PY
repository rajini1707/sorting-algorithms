arr = []
print("Enter 5 numbers:")
for i in range(5):
    arr.append(int(input()))

for i in range(5):
    smallest = i
    for j in range(i + 1, 5):
        if arr[j] < arr[smallest]:
            smallest = j
    arr[i], arr[smallest] = arr[smallest], arr[i]

print("Sorted array:", arr)