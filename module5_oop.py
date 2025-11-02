class NumberCollection:
    def __init__(self, size):
        # initialize storage for up to 'size' numbers
        self.size = size
        self.numbers = []

    def insert_number(self, value):
        # add number to collection (assumes caller ensures not to exceed size)
        self.numbers.append(value)

    def find(self, target):
        # return 1-based index of first occurrence of target, or -1 if not found
        for i, num in enumerate(self.numbers):
            if num == target:
                return i + 1  # 1-based index
        return -1


def main():
    # 1. read N
    N = int(input("Enter N (positive integer): ").strip())

    # 2. initialize collection
    collection = NumberCollection(N)

    # 3. read N numbers one by one
    print(f"Enter {N} numbers:")
    for _ in range(N):
        value = int(input().strip())
        collection.insert_number(value)

    # 4. read X
    X = int(input("Enter X (integer to search): ").strip())

    # 5. search
    result = collection.find(X)

    # 6. output
    print(result)


if __name__ == "__main__":
    main()
