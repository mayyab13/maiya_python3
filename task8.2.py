m = int(input("Array length: "))
A = []

for i in range(m):
    A.append(int(input("element: ")))

print("Original:", A)

A[0], A[-1] = A[-1], A[0]

print(A)
