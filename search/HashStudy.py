
def hash(aString, tablesize):
    sum = 0
    for pos in range(len(aString)):
        sum = sum + ord(aString[pos])*(pos+1)
        print(sum)
    return sum%tablesize

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def put(self, key, data):
        keyhash = self.hashfunction(key, len(self.slots))
        if self.slots[keyhash] == None:
            self.slots[keyhash] = key
            self.data[keyhash] = data
        else:
            if self.slots[keyhash] == key:
                self.data[keyhash] = data
            else:
                newhash = self.rehash(keyhash, len(self.slots))
                while self.slots[newhash] != None and self.slots[newhash] != key:
                    newhash = self.rehash(newhash, len(self.slots))
                if self.slots[newhash] == None:
                    self.slots[newhash] = key
                    self.data[newhash] = data
                else:
                    self.data[newhash] = data

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        if self.slots[startslot] == key:
            return self.data[startslot]
        else:
            nextslot = self.rehash(key, len(self.slots))
            while self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))
                if nextslot == startslot:
                    return None
            return self.data[nextslot]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':
    # print(hash('cat', 11))
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    print(H[20])
    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H.data)
    print(H[99])