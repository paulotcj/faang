
class Factorial:
    def __init__(self) -> None:
        pass
    def factorial_recursive(self, number):
        # 5! = % * 4 * 3 * 2 * 1 ... when does it stop?
        #this could go forever, so we must put a stopping clause:
        if number == 2: return 2

        return number * self.factorial_recursive(number - 1)
    
    def factorial_iterative(self, number):
        #5! = 5 * 4 * 3 * 2 * 1, but it's also: 5! = 1 * 2 * 3 * 4 * 5

        answer = 1 #initial condition

        #since we used the initial condition we start at 2
        # and range is non-incluse, so we add 1 to the number
        for i in range(2, number+1): 
            answer *= i

        return answer
    
#------------------------------------------------------------

x = Factorial()
num = 8
result = x.factorial_recursive(num)
print(f'factorial recursive of {num} : {result}')
result = x.factorial_iterative(num)
print(f'factorial iterative of {num} : {result}')