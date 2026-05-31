# flowgo

![Tests](https://github.com/YesthisI/flow/actions/workflows/test.yml/badge.svg)
![Coverage](https://codecov.io/gh/YesthisI/flow/branch/main/graph/badge.svg)

A module for creating and working with individual threads in local memory...

## Installation

```bash
pip install flowgo
Features
Thread-local storage simulation
Mixed-type indexing via .index
Methods: get, set, push, pop, clear
Memory capacity inspection
Full test coverage & CI/CD

>>> from flowgo import new
>>> d = new(float, 10)
>>> d.index
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

>>> import random
>>> class neuron:
...     def key(self):
...         self.f = random.random()
...         return self.f
...
>>> g = neuron()
>>> for y in range(10):
...     d.index[y] = neuron()
...     print(d.index[y])
<__main__.neuron object at 0x...>
...

>>> for y in range(10):
...     d.index[y] = g.key()
...     print(d.index[y])
0.449...
...

>>> d.push(neuron())        # OK
>>> d.pop(5)                # Remove element at 5
>>> d.clear()               # Clear all
>>> d._py_capacity()        # Show memory capacity
