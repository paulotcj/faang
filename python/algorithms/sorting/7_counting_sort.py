class CountingSort:
    def __explanation_and_collapsable():
        pass
        # Counting sort is a sorting algorithm that operates by counting the number of objects that possess distinct key values 
        # and the number of occurrences of each key, in order to determine the positions of each key in a final and sorted array.
        #
        # Its running time is linear O(n+k), and it's important to highlight Counting Sort is not a comparison sort type of algorithm.
        #
        # Counting sort is suitable for cases where the unique keys (key variation) are relatively small compared to the 
        # number of elements in the array    
        #
        # Suppose we have the following array as input:
        # input = [1,0,3,1,3,1]
        #
        # We would then count the number of times each element appears in the array, we could use a dictionary for that:
        # count = {0:1, 1:3, 3:2}
        #
        # Then we create an array with up to the size of the 'maximum element value + 1' (since we are using base 0 array)
        # And then we would end up with 
        # mapped = [0,0,0,0]
        #
        # Then we map where each element count to their equivalent index in the array
        #           0 1 2 3  -> indexes
        # mapped = [1,3,0,2]
        #
        # Now we start to calculate the offset. The offset is calculated by adding the current element count with the previous element count
        # mapped = [1,4,4,6]
        #
        # And now we shift the offset to the left by one position. By doing this, and considering this example, the first item will start at
        #  the index 0, and not 1 (which is the value of the first element in the array)
        #           0 1 2 3  -> indexes
        # mapped = [0,1,4,4]
        #
        # Now we know that value '0' start at position '0', value '1' start at index 1, value '3' start at index 4
        #  One detail here, is that since the value 2 is not present, the offset of value '2' is mapped to index 4, but so is
        #  the offset of value '3'. This has no impact in our sorting algorithm since '2' will never be fetched in the first place.
        #
        # Now we start to place the numbers in the sorted array. And as we place them, we increment the value of the offset by 1
        #  as this will be the position of the next element with the same value
        #          0 1 2 3 4 5                0 1 2 3                        0    1    2    3    4    5
        # input = [1,0,3,1,3,1]     mapped = [0,1,4,4] ----> sorted_array = [None,1   ,None,None,None,None]    (note: mapped[1] will increment to 2)
        #          ^                            ^                                 ^
        #
        #          0 1 2 3 4 5                0 1 2 3                        0    1    2    3    4    5
        # input = [1,0,3,1,3,1]     mapped = [0,2,4,4] ----> sorted_array = [0   ,1   ,None,None,None,None]
        #            ^                        ^                              ^
        #
        #          0 1 2 3 4 5                0 1 2 3                        0    1    2    3    4    5
        # input = [1,0,3,1,3,1]     mapped = [1,2,4,4] ----> sorted_array = [0   ,1   ,None,None,3   ,None]
        #              ^                            ^                                            ^         
        #    
        #          0 1 2 3 4 5                0 1 2 3                        0    1    2    3    4    5
        # input = [1,0,3,1,3,1]     mapped = [1,2,4,5] ----> sorted_array = [0   ,1   ,1   ,None,3   ,None]
        #                ^                      ^                                      ^
        #        
        #          0 1 2 3 4 5                0 1 2 3                        0    1    2    3    4    5
        # input = [1,0,3,1,3,1]     mapped = [1,3,4,5] ----> sorted_array = [0   ,1   ,1   ,None,3   ,3   ]
        #                  ^                        ^                                                 ^
        #            
        #          0 1 2 3 4 5                0 1 2 3                        0    1    2    3    4    5
        # input = [1,0,3,1,3,1]     mapped = [1,3,4,6] ----> sorted_array = [0   ,1   ,1   ,1   ,3   ,3   ]
        #                    ^                  ^                                           
        # DONE!
        # The sorted array is: sorted_array = [0   ,1   ,1   ,1   ,3   ,3   ]


    def sort(self,input_array):
        #---------
        #First we count the number of times each element appears in the array
        count_dict = {}
        max_v = 0
        for i in input_array:
            if i in count_dict: count_dict[i] += 1
            else: count_dict[i] = 1
            max_v = max(max_v,i)
        #---------
        #Then we map where each element count to their equivalent index in the array
        array_placing = [0] * (max_v+1) #zero based array
        for k,v in count_dict.items():
            array_placing[k] = v
        #---------
        # And now we calculate the preliminary offset (note: we are not done with offset yet)
        for i in range(0,len(array_placing)):
            if i == 0: continue
            array_placing[i] += array_placing[i-1]
        #---------
        #At the end of this step we shold be done with the offset
        array_placing = [0] + array_placing[:-1]
        #---------

        #Now we run through the input array, and through the 'array_placing' we know where to place each element
        # after placing the element we increment the offset for the next time we see this element
        sorted_array = [0] * len(input_array)
        for i in input_array:
            position_to_place = array_placing[i]
            sorted_array[ position_to_place  ] = i

            array_placing[i] += 1 #we increment the offset for the next time we see this element

        return sorted_array


        


        


#-------------------------------------------------------------------------


numbers =  [18,6,27,2,30,9,15,21,4,25,11,12,0,8,3,22,14,7,16,20,28,1,19,26,10,17,5,23,13,29,24]
expected = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

x = CountingSort()
numbers = [1,0,3,1,3,1]
expected = [0,1,1,1,3,3]
numbers = x.sort(numbers)

print(f'Count sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')

#-----
numbers =  [18,6,27,2,30,9,15,21,4,25,11,12,0,8,3,22,14,7,16,20,28,1,19,26,10,17,5,23,13,29,24]
expected = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
numbers = x.sort(numbers)
print(f'Count sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')

#-----

numbers =  [1, 0, 3, 1, 3, 1, 4, 5, 1, 3, 4, 1, 5, 5, 1, 3, 1, 3]
expected = [0, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5]
numbers = x.sort(numbers)
print(f'Count sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')