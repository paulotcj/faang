

def first_recurring(arr_list):
    dict = {}
    for i in arr_list:
        if i in dict:
            return i
        else:
            dict[i] = 1
            
    return None

def first_recurring2(arr_list):
    for i in range(0,len(arr_list)):
        if arr_list[i] in arr_list[i+1:]:
            return arr_list[i]  
    return None



x = [2,5,1,2,3,5,1,2,4]
result = first_recurring(x)
print(f"first recurring is: {result}")
print('-------------------------')

x = [2,5,5,2,3,5,1,2,4]
result = first_recurring(x)
print(f"first recurring is: {result}")
print('-------------------------')

x = [2,5,5,2,3,5,1,2,4]
result = first_recurring2(x)
print(f"first recurring is: {result}")
print('-------------------------')