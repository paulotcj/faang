class ReverseStringRecursive:
    def reverse1(self, str):
        # abcd
        # reverse1(bcd) + a
        # reverse1(cd) + b
        # reverse1(d) + c
        # d
        # dc
        # dcb
        # dcba

        if len(str)== 1: return str #at 1 char len the function ejects from here
        #to reach this point the string must be at least 2 chars long
        return self.reverse1(str[1:]) + str[0]
    
    def __reverse2_inner(self, p_list):
        if len(p_list) >= 1: 
            self.reversed_list.append(p_list.pop())
            self.__reverse2_inner(p_list)
        
        else:
            return


    
    def reverse2(self, str):
        self.reversed_list = []
        temp_list= list(str)

        self.__reverse2_inner(temp_list)

        reversed_str = ''.join(self.reversed_list)
        return reversed_str



x = ReverseStringRecursive()
str = 'abcd'
result = x.reverse1(str)
print(f'reverse1 of {str} : {result}')

str = 'abcd'
result = x.reverse2(str)
print(f'reverse2 of {str} : {result}')

