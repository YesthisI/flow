# tests/test_flowgo.py
import unittest
import sys
from flowgo import new

class TestFlowGo(unittest.TestCase):
    """Test suite for the flowgo.new class."""

    def test_initialization(self):
        """Test that new() initializes correctly."""
        d = new(float, 5)
        self.assertEqual(len(d.index), 5)
        self.assertTrue(all(x == 0.0 for x in d.index))
        self.assertEqual(d.stack.shape, (5,))
        self.assertEqual(d.stack.dtype, 'float64')

    def test_initialization_with_int(self):
        """Test initialization with int dtype."""
        d = new(int, 3)
        self.assertEqual(d.stack.dtype, 'int64')
        self.assertTrue(all(x == 0 for x in d.index))

    def test_get_and_set(self):
        """Test get() and set() methods."""
        d = new(float, 3)
        d.set(0, 10.5)
        d.set(1, "hello")
        d.set(2, [1, 2, 3])

        self.assertEqual(d.get(0), 10.5)
        self.assertEqual(d.get(1), "hello")
        self.assertEqual(d.get(2), [1, 2, 3])

        # Test index out of range
        with self.assertRaises(IndexError):
            d.get(10)

        with self.assertRaises(IndexError):
            d.set(10, "out of bounds")

    def test_push_and_pop(self):
        """Test push() and pop() methods."""
        d = new(float, 2)
        d.push("new item")
        self.assertEqual(len(d.index), 3)
        self.assertEqual(d.index[2], "new item")

        item = d.pop(2)
        self.assertEqual(item, "new item")
        self.assertEqual(len(d.index), 2)

        # Pop from end
        d.push("last")
        item = d.pop()
        self.assertEqual(item, "last")

        # Pop from empty
        d.clear()
        with self.assertRaises(IndexError):
            d.pop()

    def test_clear(self):
        """Test clear() method."""
        d = new(float, 3)
        d.set(0, "data")
        d.clear()
        self.assertEqual(len(d.index), 0)
        d.push("after clear")
        self.assertEqual(d.get(0), "after clear")

    def test_index_property(self):
        """Test direct access to d.index."""
        d = new(float, 2)
        d.index[0] = "direct"
        self.assertEqual(d.index[0], "direct")

        # Replace entire list
        d.index = ["a", "b", "c"]
        self.assertEqual(d.index, ["a", "b", "c"])

        with self.assertRaises(TypeError):
            d.index = "not a list"

    def test_py_capacity(self):
        """Test _py_capacity prints and returns reasonable value."""
        d = new(float, 5)
        d.push("large_object")
        cap = d._py_capacity()
        self.assertIsInstance(cap, int)
        self.assertGreaterEqual(cap, len(d.index))

    def test_capacity_resize_up(self):
        """Test _capacity increases size and extends index."""
        d = new(float, 2)
        d._capacity(5)
        self.assertEqual(len(d.index), 5)
        self.assertEqual(d.stack.shape, (5,))
        # New slots should be initialized
        self.assertEqual(d.index[2], 0.0)  # from stack zero

    def test_capacity_resize_down(self):
        """Test _capacity shrinks index."""
        d = new(float, 5)
        d.set(0, "keep")
        d.set(1, "me")
        d._capacity(2)
        self.assertEqual(len(d.index), 2)
        self.assertEqual(d.index[0], "keep")
        self.assertEqual(d.index[1], "me")
        self.assertEqual(d.stack.shape, (2,))

    def test_mixed_objects(self):
        """Test storing custom objects like neuron."""
        class Neuron:
            def __init__(self, name):
                self.name = name
            def __repr__(self):
                return f"Neuron({self.name})"

        d = new(float, 3)
        n1 = Neuron("A")
        n2 = Neuron("B")

        d.set(0, n1)
        d.push(n2)

        self.assertIs(d.get(0), n1)
        self.assertIs(d.get(3), n2)  # after push

    def test_len_and_repr(self):
        """Test len() and repr()."""
        d = new(int, 4)
        self.assertEqual(len(d), 4)
        self.assertIn("dtype=int64", repr(d))

        d.push(100)
        self.assertEqual(len(d), 5)

    def test_info_method(self):
        """Test info() method if added."""
        d = new(float, 1)
        # Capture print output
        from io import StringIO
        import contextlib

        with contextlib.redirect_stdout(StringIO()) as f:
            d.info()
        output = f.getvalue()
        self.assertIn("Length: 1", output)
        self.assertIn("NumPy stack shape: (1,)", output)


if __name__ == '__main__':
    unittest.main()
