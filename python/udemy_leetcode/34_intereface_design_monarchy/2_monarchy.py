# https://leetcode.com/discuss/post/302164/google-phone-screen-monarchy-by-anonymou-odum/

from typing import List, Dict, Set

#-------------------------------------------------------------------------
class Monarchy : 
    #-------------------------------------------------------------------------
    def __init__(self, monarch : str) -> None:
        self.monarch : str = monarch
        
        # adjacency list. parent -> list of children
        self.family_adj_list : Dict[str, List[str]] = {monarch : []}
        
        ''' we need to wrap 'king_name' in a list because we want to access it as
          a whole string. If we were to do : self.alive = set( king_name )  the
          result would be a set with individual chars, as in: {'H', 'e', 'n', 'r', 'y'} '''
        self.alive : Set[str] = set([monarch])
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def birth(self, child : str , parent : str) -> None:
        self.family_adj_list[parent].append(child)
        self.family_adj_list[child] = [] # add a new member to the adjacency list
        self.alive.add(child)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def death(self, name : str) -> None:
        self.alive.remove(name) #you can use discard if you are not sure the name is present in the set
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def getOrderOfSuccession(self) -> List[str]:
        self.order_of_succession : List[str] = []
        
        self.__dfs(person = self.monarch)
        
        return self.order_of_succession
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __dfs(self, person : str):
        if person in self.alive:
            self.order_of_succession.append(person)
            
        for child in self.family_adj_list[person]:
            self.__dfs(person = child)
    #------------------------------------------------------------------------- 
#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
def test1():
    m = Monarchy("King")
    m.birth("Andy", "King")
    m.birth("Bob", "King")
    m.birth("Catherine", "King")
    m.birth("Matthew", "Andy")
    m.birth("Alex", "Bob")
    m.birth("Asha", "Bob")
    expected_result = ['King', 'Andy', 'Matthew', 'Bob', 'Alex', 'Asha', 'Catherine']
    result = m.getOrderOfSuccession()
    print(f'Test 1     : {result}')
    print(f'  expected : {expected_result}')
    print(f'  Is the result the expected outcome? {result == expected_result}')
    print('----------')
    # Expected: ['King', 'Andy', 'Matthew', 'Bob', 'Alex', 'Asha', 'Catherine']
#-------------------------------------------------------------------------
def test2():
    m = Monarchy("King")
    m.birth("Andy", "King")
    m.birth("Bob", "King")
    m.birth("Catherine", "King")
    m.birth("Matthew", "Andy")
    m.birth("Alex", "Bob")
    m.birth("Asha", "Bob")
    m.death("Bob")
    expected_result = ['King', 'Andy', 'Matthew', 'Alex', 'Asha', 'Catherine']
    result = m.getOrderOfSuccession()
    print(f'Test 2     : {result}')
    print(f'  expected : {expected_result}')
    print(f'  Is the result the expected outcome? {result == expected_result}')
    print('----------')
    # Expected: ['King', 'Andy', 'Matthew', 'Alex', 'Asha', 'Catherine']
#-------------------------------------------------------------------------
def test3():
    m = Monarchy("King")
    m.birth("Andy", "King")
    m.birth("Bob", "King")
    m.birth("Catherine", "King")
    m.birth("Matthew", "Andy")
    m.birth("Alex", "Bob")
    m.birth("Asha", "Bob")
    m.birth("Ken", "Matthew")
    m.birth("William", "Matthew")
    m.death("Matthew")
    m.death("Andy")
    expected_result = ['King', 'Ken', 'William', 'Bob', 'Alex', 'Asha', 'Catherine']
    result = m.getOrderOfSuccession()
    print(f'Test 3     : {result}')
    print(f'  expected : {expected_result}')
    print(f'  Is the result the expected outcome? {result == expected_result}')
    print('----------')
    # Expected: ['King', 'Ken', 'William', 'Bob', 'Alex', 'Asha', 'Catherine']
#-------------------------------------------------------------------------

print('\n\n')
print('----------')
test1()
test2()
test3()