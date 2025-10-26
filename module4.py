# Ask for number of elements
N = int(input("Enter N (positive integer): "))

# Read N numbers one by one
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Ask for X
X = int(input("Enter X: "))

# Check if X exists and print result
if X in numbers:
    print(numbers.index(X) + 1)  # +1 for 1-based index
else:
    print(-1)
