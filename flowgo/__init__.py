# flowgo/__init__.py
import numpy as np
import sys
from typing import Any, Union, List

class new:
    """
    A dynamic container for thread-like storage with typed initial values.
    Users interact primarily via `self.index`, a list that can store mixed types.

    Example:
        d = new(float, 10)
        d.index[0] = "hello"           # OK
        d.index[1] = neuron()          # OK
    """

    def __init__(self, dtype: Union[type, str, np.dtype], flow: int):
        """
        :param dtype: Initial data type for the base NumPy array (e.g., float, int)
        :param flow: Number of slots (capacity)
        """
        self.dtype = np.dtype(dtype)
        self.stack = np.zeros(shape=flow, dtype=self.dtype)  # Base numeric array
        self._index: List[Any] = [0.0] * flow  # User-facing list, mutable, mixed-type

        # Initialize with default zero values from stack
        for i, val in enumerate(self.stack):
            self._index[i] = float(val)  # Default init

    @property
    def index(self) -> List[Any]:
        """Public access to the dynamic list of objects/values."""
        return self._index

    @index.setter
    def index(self, value):
        if not isinstance(value, list):
            raise TypeError("Index must be assigned a list")
        self._index = value

    def get(self, idx: int) -> Any:
        """Get value at index."""
        if not 0 <= idx < len(self._index):
            raise IndexError(f"Index {idx} out of range [0, {len(self._index)})")
        return self._index[idx]

    def set(self, idx: int, item: Any) -> None:
        """Set value at index."""
        if not 0 <= idx < len(self._index):
            raise IndexError(f"Index {idx} out of range [0, {len(self._index)})")
        self._index[idx] = item

    def push(self, item: Any) -> None:
        """Append item to the end, resize if needed."""
        self._index.append(item)

    def pop(self, idx: int = -1) -> Any:
        """Remove and return item at index (default: last)."""
        if not self._index:
            raise IndexError("pop from empty list")
        if idx < 0:
            idx = len(self._index) + idx
        if not 0 <= idx < len(self._index):
            raise IndexError(f"Pop index {idx} out of range")
        return self._index.pop(idx)

    def clear(self) -> None:
        """Clear all data in index."""
        self._index.clear()

    def _py_capacity(self, x: List[Any] = None) -> int:
        """
        Estimate the structural capacity of a list in terms of number of elements it can hold.
        Uses memory size difference between full and empty list.
        """
        target = x if x is not None else self._index
        size_empty = sys.getsizeof([])
        size_full = sys.getsizeof(target)
        try:
            capacity = (size_full - size_empty) // 8  # Approximate for 64-bit pointers
            print("size of an empty list:", size_empty)
            print("size_total:", size_full)
            print("capacity of the list is:", max(capacity, len(target)))  # Cap at real length
            return max(capacity, len(target))
        except ZeroDivisionError:
            return 0

    def _capacity(self, size: int) -> None:
        """
        Resize the internal NumPy stack and extend _index accordingly.
        New slots are initialized to 0.0.
        """
        old_len = len(self._index)
        self.stack.resize(size, refcheck=False)

        if size > old_len:
            # Extend _index with zeros
            for i in range(old_len, size):
                self._index.append(float(self.stack[i]))
        elif size < old_len:
            # Trim _index
            self._index = self._index[:size]

    def __len__(self) -> int:
        return len(self._index)

    def __repr__(self) -> str:
        return f"new(dtype={self.dtype}, flow={len(self._index)})"

    def info(self) -> None:
        """Print detailed info about current state."""
        print(f"Length: {len(self._index)}")
        print(f"NumPy stack shape: {self.stack.shape}")
        self._py_capacity()
