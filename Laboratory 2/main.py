class HashTable:
    def __init__(self):
        self.c = 100
        self.size = 0
        self.table = {}


    def hash(self, key):
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
        return hashsum % self.c

    def insert(self, key, value):
        self.size = self.size + 1
        index = self.hash(key)
        if index not in self.table:
            self.table[index] = []
        self.table[index].append((key, value))

    def find(self, key):
        index = self.hash(key)

        for node in self.table[index]:
            if node[0] == key:
                return node[1]
        return None


table = HashTable()
table.insert("cb", "som")
table.insert("bc", "som")
print(table.find("bc"))