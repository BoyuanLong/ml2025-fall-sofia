# module5_call.py

from module5_mod import NumberCollection

def main():
    N = int(input("Enter N (positive integer): ").strip())

    collection = NumberCollection(N)

    print(f"Enter {N} numbers:")
    for _ in range(N):
        value = int(input().strip())
        collection.insert_number(value)

    X = int(input("Enter X (integer to search): ").strip())

    result = collection.find(X)
    print(result)

if __name__ == "__main__":
    main()
