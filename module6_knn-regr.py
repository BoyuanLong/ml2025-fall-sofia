# knn_mod.py
import numpy as np
from typing import List, Tuple

class KNNRegressor1D:
    """
    Simple 1D k-NN regressor: features are scalar x; target is scalar y.
    Prediction is the mean y of the k nearest points by |x - X|.
    """

    def __init__(self) -> None:
        self._xs: List[float] = []
        self._ys: List[float] = []
        self.x: np.ndarray | None = None
        self.y: np.ndarray | None = None

    def add_point(self, x: float, y: float) -> None:
        self._xs.append(float(x))
        self._ys.append(float(y))

    def fit(self) -> None:
        """Finalize internal NumPy arrays."""
        self.x = np.asarray(self._xs, dtype=float)
        self.y = np.asarray(self._ys, dtype=float)

    def predict(self, X: float, k: int) -> float:
        """
        Predict y for scalar X using k nearest neighbors by L1 distance on x.
        Returns the mean of the k neighbors' y values.
        Raises ValueError if k <= 0, no data, or k > N.
        """
        if self.x is None or self.y is None:
            self.fit()
        assert self.x is not None and self.y is not None

        n = self.x.shape[0]
        if n == 0:
            raise ValueError("No data points have been added.")
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        if k > n:
            raise ValueError(f"k ({k}) cannot be greater than N ({n}).")

        # Vectorized distances |x_i - X|
        dists = np.abs(self.x - float(X))

        # Indices of k smallest distances (O(n)), order within the slice not guaranteed
        k_idx_unsorted = np.argpartition(dists, kth=k - 1)[:k]

        # For a stable, human-friendly behavior, sort those k by distance (then index)
        k_idx = k_idx_unsorted[np.argsort(dists[k_idx_unsorted], kind="stable")]

        return float(np.mean(self.y[k_idx]))
