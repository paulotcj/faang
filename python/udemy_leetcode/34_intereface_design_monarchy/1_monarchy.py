# https://leetcode.com/discuss/post/302164/google-phone-screen-monarchy-by-anonymou-odum/

#-------------------------------------------------------------------------
class Monarchy:
    #-------------------------------------------------------------------------
    def __init__(self, king_name):
        self.king = king_name
        self.family = {king_name: []}  # parent -> list of children
        self.alive = set([king_name])  # set of alive people
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def birth(self, child, parent):
        if parent not in self.family:
            self.family[parent] = []
        self.family[parent].append(child)
        self.family[child] = []
        self.alive.add(child)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def death(self, name):
        self.alive.discard(name)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def getOrderOfSuccession(self):
        order = []
        def dfs(person):
            if person in self.alive:
                order.append(person)
            for child in self.family.get(person, []):
                dfs(child)
        dfs(self.king)
        return order
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
    print(f'Test 1     :{result}')
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
    print(f'Test 2     :{result}')
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
    print(f'Test 3     :{result}')
    print(f'  expected : {expected_result}')
    print(f'  Is the result the expected outcome? {result == expected_result}')
    print('----------')
    # Expected: ['King', 'Ken', 'William', 'Bob', 'Alex', 'Asha', 'Catherine']
#-------------------------------------------------------------------------

test1()
test2()
test3()