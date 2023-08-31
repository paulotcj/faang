def mergeSortedArrays(arr1, arr2):
    #validations
    if arr1 == None and arr2 == None: return None
    if arr1 is not None and (arr2 == None or len(arr2) == 0): return arr1
    if arr2 is not None and (arr1 == None or len(arr1) == 0): return arr2
    

    
    merged = []
    i_arr1 = 0
    i_arr2 = 0
    item1 = arr1[i_arr1]
    item2 = arr2[i_arr2]
    
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    
    while item1 is not None or item2 is not None:
        if item2 == None or (item1 is not None and item1 < item2):
            merged.append(item1)
            i_arr1 += 1
            if i_arr1 == len_arr1:
                item1 = None
            else:
                item1 = arr1[i_arr1]
        else:
            merged.append(item2)
            i_arr2 += 1
            if i_arr2 == len_arr2:
                item2 = None
            else:
                item2 = arr2[i_arr2]
            
            
    return merged


arr1 = [1,2,3,4,5,7,9,11,13,15]
arr2 = [6,8,10,12]

arr3 = mergeSortedArrays(arr1, arr2)

print(arr3)
    
print('--------------------')
arr1 = []
arr2 = [6,8,10,12]

arr3 = mergeSortedArrays(arr1, arr2)

print(arr3)

print('--------------------')
arr1 = [6,8,10,12]
arr2 = []

arr3 = mergeSortedArrays(arr1, arr2)

print(arr3)

print('--------------------')
arr1 = []
arr2 = []

arr3 = mergeSortedArrays(arr1, arr2)

print(arr3)
     
    
print('--------------------') 
arr1 = [6,8]
arr2 = [1,2,3,4,5,7,9,10,12,14]

arr3 = mergeSortedArrays(arr1, arr2)

print(arr3)

print('--------------------')
arr1 = None
arr2 = None

arr3 = mergeSortedArrays(arr1, arr2)

print(arr3)

print('--------------------')
arr1 = None
arr2 = []

arr3 = mergeSortedArrays(arr1, arr2)

print(arr3)

print('--------------------')
arr1 = []
arr2 = None

arr3 = mergeSortedArrays(arr1, arr2)

print(arr3)
     