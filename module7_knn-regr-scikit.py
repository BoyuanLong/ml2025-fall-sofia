import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    # Read N (number of training points)
    while True:
        try:
            N = int(input("Enter N (number of training samples, positive integer): "))
            if N <= 0:
                print("N must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer for N.")

    # Read k (number of neighbors)
    while True:
        try:
            k = int(input("Enter k (number of neighbors, positive integer): "))
            if k <= 0:
                print("k must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer for k.")

    # Initialize arrays for data using NumPy
    # X is 2D (N x 1) because scikit-learn expects 2D feature arrays
    X_train = np.zeros((N, 1), dtype=float)
    y_train = np.zeros(N, dtype=float)

    print("\nEnter the training points (x, y):")
    for i in range(N):
        while True:
            try:
                x_val = float(input(f"  Enter x value for point {i + 1}: "))
                break
            except ValueError:
                print("    Invalid input. Please enter a real number for x.")
        while True:
            try:
                y_val = float(input(f"  Enter y value for point {i + 1}: "))
                break
            except ValueError:
                print("    Invalid input. Please enter a real number for y.")

        X_train[i, 0] = x_val
        y_train[i] = y_val

    # Compute variance of labels (y values) in the training dataset using NumPy
    # This is the population variance (ddof=0). If you want sample variance, use ddof=1.
    label_variance = np.var(y_train)

    # Read query X for prediction
    while True:
        try:
            X_query = float(input("\nEnter X value for prediction: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number for X.")

    # Check if k <= N
    if k > N:
        print("\nError: k cannot be greater than N (number of training samples).")
        return

    # Create and train k-NN regressor using scikit-learn
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, y_train)

    # Predict Y for the given X_query
    X_query_array = np.array([[X_query]])  # shape (1, 1)
    y_pred = knn_regressor.predict(X_query_array)[0]

    # Output the result
    print(f"\nPredicted Y for X = {X_query} using k-NN Regression (k = {k}): {y_pred}")
    print(f"Variance of labels (y) in the training dataset: {label_variance}")

if __name__ == "__main__":
    main()
