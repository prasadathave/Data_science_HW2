import numpy as np
class countsketch:
    def __init__(self,no_of_hashes,depth):
        self.no_of_hashes = no_of_hashes
        self.depth = depth
        self.arr = np.zeros([no_of_hashes,depth])
    def insert_stream(self):
        # deal with stream
        pass


cs = countsketch(5,100)


