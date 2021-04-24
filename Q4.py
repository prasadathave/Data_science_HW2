
import hashlib
import array

# reference

# class CountMinSketch(object):
#     """
#     A class for counting hashable items using the Count-min Sketch strategy.
#     It fulfills a similar purpose than `itertools.Counter`.
#     The Count-min Sketch is a randomized data structure that uses a constant
#     amount of memory and has constant insertion and lookup times at the cost
#     of an arbitrarily small overestimation of the counts.
#     It has two parameters:
#      - `m` the size of the hash tables, larger implies smaller overestimation
#      - `d` the amount of hash tables, larger implies lower probability of
#            overestimation.
#     An example usage:
#         from countminsketch import CountMinSketch
#         sketch = CountMinSketch(1000, 10)  # m=1000, d=10
#         sketch.add("oh yeah")
#         sketch.add(tuple())
#         sketch.add(1, value=123)
#         print sketch["oh yeah"]       # prints 1
#         print sketch[tuple()]         # prints 1
#         print sketch[1]               # prints 123
#         print sketch["non-existent"]  # prints 0
#     Note that this class can be used to count *any* hashable type, so it's
#     possible to "count apples" and then "ask for oranges". Validation is up to
#     the user.
#     """

#     def __init__(self, m, d):
#         """ `m` is the size of the hash tables, larger implies smaller
#         overestimation. `d` the amount of hash tables, larger implies lower
#         probability of overestimation.
#         """
#         if not m or not d:
#             raise ValueError("Table size (m) and amount of hash functions (d)"
#                              " must be non-zero")
#         self.size_of_hashtables = m
#         self.number_of_hashtables = d
#         self.number_of_elements_added= 0
#         self.tables = []
#         for _ in xrange(d):
#             table = array.array("l", (0 for _ in xrange(m)))
#             self.tables.append(table)

#     def _hash(self, x):
#         md5 = hashlib.md5(str(hash(x)))
#         for i in xrange(self.number_of_hashtables):
#             md5.update(str(i))
#             yield int(md5.hexdigest(), 16) % self.size_of_hashtables

#     def add(self, x, value=1):
#         """
#         Count element `x` as if had appeared `value` times.
#         By default `value=1` so:
#             sketch.add(x)
#         Effectively counts `x` as occurring once.
#         """
#         self.number_of_elements_added+= value
#         for table, i in zip(self.tables, self._hash(x)):
#             table[i] += value

#     def query(self, x):
#         """
#         Return an estimation of the amount of times `x` has ocurred.
#         The returned value always overestimates the real value.
#         """
#         return min(table[i] for table, i in zip(self.tables, self._hash(x)))

#     def __getitem__(self, x):
#         """
#         A convenience method to call `query`.
#         """
#         return self.query(x)

#     def __len__(self):
#         """
#         The amount of things counted. Takes into account that the `value`
#         argument of `add` might be different from 1.
#         """
#         return self.n


from collections import Counter

class misra_gries:
    def __init__(self,k):
        self.count1 = Counter()
        self.k = k   

    def insert(self,value,count):
        for _ in range(count):
            #if space is empty then add it or increment if it already exists
            if value in self.count1 or len(self.count1)<self.k:
                self.count1[value] +=1
            else:
                #Remove one if you don't have one value
                for k1 in list(self.count1.keys()):
                    self.count1[k1]-=1
                    if(self.count1[k1]==0):
                        del self.count1[k1]

    def give_counts(self):
        return self.count1


class calculate_absolute:
    def __init__(self):
        self.count1 = Counter()
    
    def insert(self,value,count):
        self.count1[value]+=count

    def give_counts(self):
        return self.count1

class CountMinSketch:
  # it takes input and initiates the sketch
    def __init__(self, size_of_hashtables, number_of_hashtables):

        self.size_of_hashtables = size_of_hashtables
        self.number_of_hashtables = number_of_hashtables
        self.number_of_elements_added= 0
        self.hash_tables = []
        for _ in range(number_of_hashtables):
            table = [0 for _ in range(size_of_hashtables)]
            self.hash_tables.append(table)

    def _hash(self, x):
        # k-wise hash generation
        md5 = hashlib.md5(str(hash(x)))
        for i in range(self.number_of_hashtables):
            md5.update(str(i))
            yield int(md5.hexdigest(), 16) % self.size_of_hashtables
    
    def add(self, x, count):
        # function for adding a certain element
        self.number_of_elements_added+= count
        for table, i in zip(self.hash_tables, self._hash(x)):
            table[i] += count

    def get_count(self, x):
        #function for getting counts 
        return min(table[i] for table, i in zip(self.hash_tables, self._hash(x)))


    def __len__(self):
        # function for calculating number of elements from 
        return self.number_of_elements_added




class CountSketch:
  # it takes input and initiates the sketch
    def __init__(self, size_of_hashtables, number_of_hashtables):

        self.size_of_hashtables = size_of_hashtables
        self.number_of_hashtables = number_of_hashtables
        self.number_of_elements_added= 0
        self.hash_tables = []
        for _ in range(number_of_hashtables):
            table = [0 for _ in range(size_of_hashtables)]
            self.hash_tables.append(table)

    def _hash(self, x):
        # k-wise hash generation
        md5 = hashlib.md5(str(hash(x)))
        for i in range(self.number_of_hashtables):
            md5.update(str(i))
            yield int(md5.hexdigest(), 16) % self.size_of_hashtables

    def g(self,i):
        # getting the g for the each object
        if(i%2)==0:
            return -1
        else:
            return 1
    
    def add(self, x, count):
        # function for adding a certain element
        self.number_of_elements_added+= count
        for table, i in zip(self.hash_tables, self._hash(x)):
            table[i] += count*self.g(i)

    def get_count(self, x):
        #function for getting counts 
        return sum(table[i] for table, i in zip(self.hash_tables, self._hash(x)))/self.number_of_hashtables


    def __len__(self):
        # function for calculating number of elements from 
        return self.number_of_elements_added

w =5
karr = [100,200,500,1000,2000]
val = 100
file = open("matlab/train.data","r")
array_of_values = [i.strip() for i in file.readlines()]
absolute_counting = calculate_absolute()
misra_gries_counting = misra_gries(val*w)
CountMinSketch_counting = CountMinSketch(val,w)
CountMinSketch_counting = CountSketch(val,w)


