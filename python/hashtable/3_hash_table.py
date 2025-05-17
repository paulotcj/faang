from typing import List, Tuple, Any


#-------------------------------------------------------------------------
class HashTable:
    #-------------------------------------------------------------------------
    def __init__(self, size : int = 10) -> None:
        # Initialize the hash table with empty buckets
        self.size : int = size
        self.buckets : List[list[Tuple[str, int]]] = [ [] for _ in range(size) ]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _hash(self, key : str) -> int :
        return_val : int = sum ( 
            ord(char) # unicode val for one single char
            for char in key 
        ) % self.size # must fit the bucket size
        
        return return_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def set(self, key: str, value: Any) -> None:
        # Insert or update the key-value pair
        index: int = self._hash(key)
        bucket: List[Tuple[str, Any]] = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Insert new key
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def get(self, key: str) -> Any:
        # Retrieve value by key
        index: int = self._hash(key)
        bucket: List[Tuple[str, Any]] = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found.")
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __str__(self) -> str:
        # For easy visualization
        items: List[Tuple[str, Any]] = []
        for bucket in self.buckets:
            items.extend(bucket)
        return str(dict(items))
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def remove(self, key: str) -> None:
        # Remove a key-value pair
        index: int = self._hash(key)
        bucket: List[Tuple[str, Any]] = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found.")
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


ht = HashTable()
ht.set("apple", 5)
ht.set("banana", 3)
ht.set("ananab", 11)
print(ht.get("apple"))   # Output: 5
print(ht)                # Output: {'apple': 5, 'banana': 3}
ht.remove("banana")
print(ht)                # Output: {'apple': 5}