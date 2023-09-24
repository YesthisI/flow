# Introduction

`flowgo`  is a module for creating and working with individual threads in the local memory of each.
When threads are created, the system allocates an array of dtype values for thread local storage (TLS), which are initialized to NULL values. 
Before an index can be used, one of the threads must be assigned. Each thread stores its index data in an array of TLS slots. 
If the data associated with the index matches a value of type dtype , you can store the data directly in the TLS slot.

![alt text](https://github.com/YesthisI/flow/blob/main/images/Process.jpg)

# Installation
```
pip install flowgo
```
# Import
```python
from flowgo import new
```

#User Example
```python
>>>from flowgo import new
>>> d = new(float,10)
>>> d.index
[[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]
>>>import random
>>>class neuron:
	def key(self):
		self.f = random.random()
		return self.f
>>> g = neuron()
>>> g
<__main__.neuron object at 0x000001E4183EE3D0>
>>>for y in range(0,10,1):
	d.index[y] = neuron()
	print(d.index[y])


<__main__.neuron object at 0x000001E4183C4D90>
<__main__.neuron object at 0x000001E4183C4DF0>
<__main__.neuron object at 0x000001E4183C4FA0>
<__main__.neuron object at 0x000001E4183C4D60>
<__main__.neuron object at 0x000001E4183C4E50>
<__main__.neuron object at 0x000001E4183C4F10>
<__main__.neuron object at 0x000001E4183C4FD0>
<__main__.neuron object at 0x000001E4183EE100>
<__main__.neuron object at 0x000001E4183EE160>
<__main__.neuron object at 0x000001E4183EE1C0>

>>> for y in range(0,10,1):
	d.index[y] = g.key()
	print(d.index[y])


0.44911829971109984
0.799771054321658
0.9866593046500528
0.5261054909048434
0.584669797754662
0.45202100815352386
0.9676910835103338
0.8198882778445146
0.7652557520179178
0.043740125797619434

>>> d.index
[0.44911829971109984, 0.799771054321658, 0.9866593046500528, 0.5261054909048434, 
0.584669797754662, 0.11103911368026942, 0.9732179960637262, 0.45910841138678904, 
0.4323464306091388, 0.017103767583308005]
>>> for y in range(3,10,1):
	d.index[y] = neuron().key()
	print(d.index[y])

0.736735454198254
0.5561266578913844
0.14408739831419615
0.6957408632107883
0.04113475552348311
0.1883360140198398
0.3012576585293536
>>> d.index.insert(5,neuron())
>>> d.index
[[0.0], [0.0], [0.0], 0.736735454198254, 0.5561266578913844, <__main__.neuron object at 0x000001E411A9E8E0>, 
0.14408739831419615, 0.6957408632107883, 0.04113475552348311, 0.1883360140198398, 0.3012576585293536]
```
