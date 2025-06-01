class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [[] for _ in range(self.size)]

    def _get_hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        h = self._get_hash(key)
        for idx, (k, v) in enumerate(self.map[h]):
            if k == key:
                self.map[h][idx] = (key, value)
                return
        self.map[h].append((key, value))

    def get(self, key):
        h = self._get_hash(key)
        for k, v in self.map[h]:
            if k == key:
                return v
        return None

    def delete(self, key):
        h = self._get_hash(key)
        for idx, (k, _) in enumerate(self.map[h]):
            if k == key:
                del self.map[h][idx]
                return True
        return False

hmap = HashMap()
hmap.set("name", "Bob")
print(hmap.get("name"))  
hmap.delete("name")
print(hmap.get("name"))  
