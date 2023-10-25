class Fibonacci:
    def __init__(self) -> None:
        pass

    # Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones
    # 0 = 0
    # 1 = 0 + 1 = 1
    # 2 = 0 + 1 = 1
    # 3 = 1 + 1 = 2
    # 4 = 1 + 2 = 3
    # 5 = 2 + 3 = 5
    # 6 = 3 + 5 = 8

    def fib_recursive(self,value):
        if value == 0: return 0
        if value == 1: return 1

        #then the min number is 2, so value-1 = 1 and value-2 = 0 -> still valid
        return self.fib_recursive(value - 1) + self.fib_recursive(value - 2)
    
    def fib_iterative(self,value):
        if value == 0: return 0
        if value == 1: return 1

        # setting up the initial conditions
        a = 0 #first number is 0 from the sequence: 0, 1, 1, 2, 3, ...
        b = 1 #second numbe is 1 from the sequence: 0, 1, 1, 2, 3, ...
        #---
        c = None #this is just the sum, so the start value is None

        # Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones
        for i in range(2, value+1):
            c = a + b #this is fibonacci right here
            #-----
            a = b #now we move the variables to a more updated state
            b = c

        return c

#------------------------------------------------------------

x = Fibonacci()
num = 38
result = x.fib_iterative(num)
print(f'fib iterative of {num} : {result}')

result = x.fib_recursive(num)
print(f'fib recursive of {num} : {result}')

