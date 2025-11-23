import numpy as np
from sklearn.metrics import precision_score, recall_score


def main():
    # Read N (number of samples)
    while True:
        try:
            n_str = input("Enter number of samples N (positive integer): ")
            N = int(n_str)
            if N <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for N.")

    # Initialize numpy arrays for ground truth (X) and predictions (Y)
    y_true = np.zeros(N, dtype=int)  # X values: ground truth labels
    y_pred = np.zeros(N, dtype=int)  # Y values: predicted labels

    print(f"\nPlease enter {N} (x, y) pairs.")
    print("X is the ground truth label (0 or 1).")
    print("Y is the predicted label (0 or 1).\n")

    # Read N (x, y) points
    for i in range(N):
        # Read X (ground truth)
        while True:
            try:
                x_str = input(f"Point {i + 1} - enter X (true label 0 or 1): ")
                x = int(x_str)
                if x not in (0, 1):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. X must be 0 or 1. Please try again.")

        # Read Y (prediction)
        while True:
            try:
                y_str = input(f"Point {i + 1} - enter Y (predicted label 0 or 1): ")
                y = int(y_str)
                if y not in (0, 1):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Y must be 0 or 1. Please try again.")

        # Insert into numpy arrays
        y_true[i] = x
        y_pred[i] = y

    # Compute Precision and Recall using scikit-learn
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    # Output the results
    print("\nResults:")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")


if __name__ == "__main__":
    main()
