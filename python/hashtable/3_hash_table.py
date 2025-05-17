class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with empty buckets
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        # Simple hash function: sum of character codes modulo table size
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        # Insert or update the key-value pair
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Insert new key

    def get(self, key):
        # Retrieve value by key
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found.")

    def __str__(self):
        # For easy visualization
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return str(dict(items))

    def remove(self, key):
        # Remove a key-value pair
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found.")

# Example usage:
if __name__ == "__main__":
    ht = HashTable()
    ht.set("apple", 5)
    ht.set("banana", 3)
    print(ht.get("apple"))   # Output: 5
    print(ht)                # Output: {'apple': 5, 'banana': 3}
    ht.remove("banana")
    print(ht)                # Output: {'apple': 5}