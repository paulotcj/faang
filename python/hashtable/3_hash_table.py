from typing import List, Tuple, Any


#-------------------------------------------------------------------------
class HashTable:
    #-------------------------------------------------------------------------
    def __init__(self, size : int = 10) -> None:
        # initialize the hash table with empty buckets
        self.size : int = size
        self.buckets : List[list[Tuple[str, Any]]] = [ [] for _ in range(size) ]
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
    def set(self, key : str , value : Any) -> None:
        # insert or update the key-value pair
        index : int = self._hash(key)
        
        # note that we are only extracting a single elements from self.buckets, and this element
        #   is a spot that contains a list, which can store 1 key/value pair or a list of key/value
        #   pairs in this index in case of hash collision
        bucket_single_spot : List[ Tuple[str, Any] ] = self.buckets[index]
        
        #-----------------------------------
        for i, (k,v) in enumerate(bucket_single_spot):
            if k == key: # we are updating an existing key
                bucket_single_spot[k] = value
                return
        #-----------------------------------
        
        # else, this is a new item with hash collision. Add to the list
        bucket_single_spot.append( (key, value) )
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def get(self, key : str) -> Any:
        # retrieve value by key
        index : int = self._hash(key = key)
        bucket : List[Tuple[str, Any]] = self.buckets[index]
        #-----------------------------------
        for i, (k,v) in enumerate(bucket):
            if key == k: return v
        #-----------------------------------
        raise KeyError(f'Key {key} not found.')
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def remove(self, key : str) -> None:
        index : int = self._hash(key = key)
        bucket : List[Tuple[int, Any]] = self.buckets[index]
        
        #-----------------------------------
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        #-----------------------------------
        raise KeyError(f'Key {key} not found')
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __str__(self) -> str:
        # for easy visualization
        
        ''' here's the picture: You have self.buckets as in:
        0 = [('apple', 5)]
        1 = []
        2 = []
        3 = []
        4 = []
        5 = []
        6 = []
        7 = []
        8 = []
        9 = [('banana', 3), ('ananab', 11)] 
        
        and then you put them into a list:
        [('apple', 5), ('banana', 3), ('ananab', 11)]
        
        but we want to show the key/value pairing so we convert them to a dict:
        "{'apple': 5, 'banana': 3, 'ananab': 11}"
        and then finally into a string
        '''
        items : List[Tuple[str, Any]] = []
        #-----------------------------------
        for bucket in self.buckets:
            items.extend( bucket )
        #-----------------------------------
        return_obj : str = str( dict(items) )
        return return_obj
        
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