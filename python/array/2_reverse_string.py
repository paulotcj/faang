
def reverse_string1(str_input):
    if str_input == None or isinstance(str_input,str) == False:
        return None
    elif len(str_input) < 2:
        return str_input
    
    
    rev_list = []
    
    for i in range(len(str_input), 0, -1):
        item = str_input[ i-1 ]

        rev_list.append( item )
        
    rev_str = ''.join(rev_list)
    return rev_str
    
    
def reverse_string2(str_input):
    if str_input == None or isinstance(str_input,str) == False:
        return None
    elif len(str_input) < 2:
        return str_input
    
    return str_input[::-1]
    
    
def reverse_string3(str_input):
    if str_input == None or isinstance(str_input,str) == False:
        return None
    elif len(str_input) < 2:
        return str_input
    
    rev_str = ''.join(reversed(str_input))
    return rev_str


def reverse_string4(str_input):
    if str_input == None or isinstance(str_input,str) == False:
        return None
    elif len(str_input) < 2:
        return str_input
    
    rev_str = ''
    for c in str_input:
        rev_str = c + rev_str
        
    return rev_str
    
    
print(f" reverse_string1('John') : {reverse_string1('John')} ")
print(f" reverse_string2('John') : {reverse_string2('John')} ")
print(f" reverse_string3('John') : {reverse_string3('John')} ")
print(f" reverse_string4('John') : {reverse_string4('John')} ")