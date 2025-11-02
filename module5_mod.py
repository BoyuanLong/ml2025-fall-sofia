# module5_mod.py

class NumberCollection:
    def __init__(self, size):
        """Initialize collection with expected size."""
        self.size = size
        self.numbers = []

    def insert_number(self, value):
        """Insert a number into the collection."""
        if len(self.numbers) < self.size:
            self.numbers.append(value)
        else:
            raise ValueError("Cannot insert more numbers than the declared size.")

    def find(self, target):
        """Return 1-based index of target or -1 if not found."""
        for i, num in enumerate(self.numbers):
            if num == target:
                return i + 1
        return -1
