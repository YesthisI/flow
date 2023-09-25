import numpy as np

class new:
    def __init__(
        self,
        types: float,
        flow: int):
        bit = types
        self.tls = flow
        self.stack = np.zeros(shape=self.tls, dtype=bit)
        self.index = []
        for data in self.stack:
            self.index.append([data])
