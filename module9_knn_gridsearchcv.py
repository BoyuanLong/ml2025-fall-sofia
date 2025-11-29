import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def read_dataset(name):
    n = read_positive_int(f"Enter number of pairs for {name} (positive integer): ")
    
    X = np.zeros((n, 1), dtype=float)  # feature: real number
    y = np.zeros(n, dtype=int)         # label: non-negative integer
    
    print(f"Now enter {n} (x, y) pairs for {name}:")
    for i in range(n):
        while True:
            try:
                x_val = float(input(f"{name} pair {i+1} - enter x (real number): "))
                y_val = int(input(f"{name} pair {i+1} - enter y (non-negative integer): "))
                if y_val < 0:
                    print("y must be a non-negative integer. Please re-enter this pair.")
                    continue
                X[i, 0] = x_val
                y[i] = y_val
                break
            except ValueError:
                print("Invalid input. Please re-enter this pair.")
    return X, y

def main():
    # Read training set
    train_X, train_y = read_dataset("TrainS")
    
    # Read test set
    test_X, test_y = read_dataset("TestS")
    
    # Determine k range, ensuring k <= number of training samples
    max_k = min(10, train_X.shape[0])
    if max_k == 0:
        print("No training data provided. Exiting.")
        return
    
    best_k = None
    best_accuracy = -1.0
    
    print("\nEvaluating kNN for k = 1 to", max_k)
    for k in range(1, max_k + 1):
        # Create and train kNN classifier
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(train_X, train_y)
        
        # Predict on test set
        y_pred = knn.predict(test_X)
        
        # Compute accuracy
        acc = accuracy_score(test_y, y_pred)
        print(f"k = {k}: Test accuracy = {acc:.4f}")
        
        # Track best k (if tie, keep the smaller k)
        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k
    
