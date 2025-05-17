
class MyHash:
    def __init__(self, size) -> None:
        self.data = [ None ] * size
        self.data_len = size
        # print(self.data)
        
    def hash(self, key):
        hash = 0
        for i in range(0, len(key) ):
            hash = ( hash + ord(key[i]) * i ) % self.data_len
            # print(f"i:{i} - hash: {hash}")
        return hash
    
    def set_v(self, key, value):
        address = self.hash(key)
        if self.data[address] == None:
            self.data[address] = []
        
        temp = [key , value]

        self.data[address].append( temp )
        return self.data
    
    def print_me(self):
        for i in range(0,self.data_len):
            
            print(f"address: {i} - data:{ self.data[i] }")
            
    def get_v(self,key):
        address = self.hash(key)
        bucket = self.data[address]
        
        if bucket != None :
            for i in bucket:
                if i[0] == key:
                    return i[1]
              
        return None
    
    def get_k(self):
        keys = []
        
        for i in self.data: #loop through the slots
            if i == None: continue
            for j in i: #loop through possible collisions in the slot
                keys.append(j[0])
        
        return keys

            

x = MyHash(10)
# test hash
# print(x.hash('Ken'))
# print(x.hash('Bob'))
# print(x.hash('Kim'))
# print(x.hash('Tom'))
# print(x.hash('Jerry'))
# print(x.hash('Pfutzenreuter'))
# print(x.hash('Mia'))
# print(x.hash('Alice'))


x.set_v(key='Ken',value = 11)
x.set_v(key='Bob',value = 22)
x.set_v(key='Kim',value = 33)
x.set_v(key='Tom',value = 44)
x.set_v(key='Jerry',value = 55)
x.set_v(key='Pfutzenreuter',value = 66)
x.set_v(key='Mia',value = 77)
x.set_v(key='Alice',value = 88)

x.print_me()


print( x.get_v(key = 'Jerry') )
print( x.get_v(key = 'Otto') )
keys = x.get_k()

print(f"keys: {keys}")