class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data #replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #replace

def hashfunction(self, key, size):
    return key%size

def rehash(self, oldhash, size):
    return(oldhash+1) % size


def get(self, key):
    startslot = self.hashfunction(key, len(self.slots))

    data = None
    stop = False
    found = False

    position = startslot

    while self.slots[position] != None and not found and not stop:
        if self.slots[position] == key:
            found = True
            data = self.data[position]

        else:
            position = self.rehash(position,len(self.slots))
            if position == startslot:
                stop = True

    return data

def __getitem__(self,key):
    return self.get(key)

def __setitem__(self,key,data):
    self.put(key,data)


H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
H.slots
H.data


'''
We stated earlier that in the best case hashing would provide a 𝑂(1), constant time search technique. 
However, due to collisions, the number of comparisons is typically not so simple. 
Even though a complete analysis of hashing is beyond the scope of this text, we can state some well-known 
results that approximate the number of comparisons necessary to search for an item.
The most important piece of information we need to analyze the use of a hash table is the load factor, 𝜆.
Conceptually, if 𝜆 is small, then there is a lower chance of collisions, meaning that items are more likely to be in the slots where they belong.
If 𝜆 is large, meaning that the table is filling up, then there are more and more collisions. 
This means that collision resolution is more difficult, requiring more comparisons to find an empty slot. 
With chaining, increased collisions means an increased number of items on each chain.
As before, we will have a result for both a successful and an unsuccessful search.
For a successful search using open addressing with linear probing, the average number of comparisons is approximately 12(1+11−𝜆) and an unsuccessful search gives 12(1+(11−𝜆)2)
If we are using chaining, the average number of comparisons is 1+𝜆2 for the successful case, and simply 𝜆 comparisons if the search is unsuccessful.
'''
