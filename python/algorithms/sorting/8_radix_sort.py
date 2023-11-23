class CountingSort:
    #-------------------------------------------------------------------------
    def sort(self,input_array):
        # Find the maximum element in the input_array
        max_v = max(input_array)

        len_count_array = max_v+1
        len_input_array = len(input_array)

        #---------
        # Initialize the count_array with (max+1) zeros
        count_array = [0] * len_count_array

        #---------
        # Step 1 -> Traverse the input_array and increase 
        # the corresponding count for every element by 1
        for i in input_array: 
            count_array[i] += 1

        #---------
        # Step 2 -> For each element in the count_array, 
        # sum up its value with the value of the previous 
        # element, and then store that value 
        # as the value of the current element
        array_placing = count_array.copy()
        for i in range(1, len_count_array):
            array_placing[i] += array_placing[i-1] 

        # #---------
        # # Step 3 -> Calculate element position
        # # based on the array_placing values
        # output_array = [0] * len_input_array
        # for i in reversed(range(len_input_array)):
        #     current_element = input_array[i]
        #     array_placing[current_element] -= 1
        #     new_position = array_placing[current_element]
        #     output_array[new_position] = current_element

        array_placing = [0] + array_placing[:-1]
        #---------

        #Now we run through the input array, and through the 'array_placing' we know where to place each element
        # after placing the element we increment the offset for the next time we see this element
        sorted_array = [0] * len(input_array)
        for i in input_array:
            position_to_place = array_placing[i]
            sorted_array[ position_to_place  ] = i

            array_placing[i] += 1 #we increment the offset for the next time we see this element        

        #---------
        return sorted_array
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def countingSortForRadix_old(self,input_array, digit_selector):
        # We can assume that the number of digits used to represent
        # all numbers on the digit_selector position is not greater than 10
        count_array = [0] * 10
        len_input_array = len(input_array)
        len_count_array = len(count_array)

        #---------
        # place_element is the value selector for the digit. e.g.( number: 123, digit_selector:10, place_element: 2 )
        # place_element is the value of the current place value of the current element, e.g. if the current element is
        # 123, and the place value is 10, the place_element is equal to 2
        for input_el in range(len_input_array): 
            place_element = self.__radix_place_element(input_array[input_el], digit_selector)
            count_array[place_element] += 1

        #---------
        array_placing = count_array.copy()
        for input_el in range(1, len_count_array): #10 digits max, start from 1 (first element will always be at 0)
            array_placing[input_el] += array_placing[input_el-1]

        #---------
        array_placing = [0] + array_placing[:-1]

        #---------
        sorted_array = [0] * len(input_array)
        for input_el in input_array:
            #---
            position_in_placing_arr = self.__radix_place_element(input_el, digit_selector) #refactor position to place to take into account the digit selector
            position_in_sorted_arr = array_placing[position_in_placing_arr]
            #---
            sorted_array[ position_in_sorted_arr  ] = input_el
            array_placing[position_in_placing_arr] += 1 #we increment the offset for the next time we see this element        
            #---
        #---------   
                
        return sorted_array    
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def __radix_place_element(self, value, digit_selector = None):
        return_v = (value // digit_selector) % 10 # the %10 at the end ensures that it's a single digit
        return return_v
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __count(self, input_array, digit_selector):
        # We can assume that the number of digits used to represent
        # all numbers on the digit_selector position is not greater than 10        
        count_array = [0] * 10
        # place_element is the value selector for the digit. e.g.( number: 123, digit_selector:10, place_element: 2 )
        # place_element is the value of the current place value of the current element, e.g. if the current element is
        # 123, and the place value is 10, the place_element is equal to 2
        for input_el in range(len(input_array)): 
            place_element = self.__radix_place_element(input_array[input_el], digit_selector)
            count_array[place_element] += 1

        return count_array

    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __array_placing(self, count_array):
        array_placing = count_array.copy()
        for input_el in range(1, len(count_array)): #10 digits max, start from 1 (first element will always be at 0)
            array_placing[input_el] += array_placing[input_el-1]

        #---------
        array_placing = [0] + array_placing[:-1]

        return array_placing
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __map_sortedArray(self, input_array, array_placing, digit_selector):
        sorted_array = [0] * len(input_array)
        for input_el in input_array:
            #---
            position_in_placing_arr = self.__radix_place_element(input_el, digit_selector) #refactor position to place to take into account the digit selector
            position_in_sorted_arr = array_placing[position_in_placing_arr]
            #---
            sorted_array[ position_in_sorted_arr  ] = input_el
            array_placing[position_in_placing_arr] += 1 #we increment the offset for the next time we see this element        
            #---

        return sorted_array
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def countingSortForRadix(self,input_array, digit_selector):
        #---------
        count_array = self.__count(input_array=input_array, digit_selector=digit_selector)

        #---------
        array_placing = self.__array_placing(count_array=count_array)

        #---------
        sorted_array = self.__map_sortedArray(input_array=input_array, array_placing=array_placing, digit_selector=digit_selector)
        
        #---------   
                
        return sorted_array    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def radixSort(self, input_array):
        # Step 1 -> Find the maximum element in the input array
        max_value = max(input_array)

        # Step 2 -> Find the number of digits in the `max` element
        max_v_num_digits = len(str(max_value))
        
        # Step 3 -> Initialize the place value to the least significant place
        digit_selector = 1

        # Step 4
        outputArray = input_array.copy()
        for _ in range(max_v_num_digits):
            outputArray = self.countingSortForRadix(outputArray, digit_selector)
            digit_selector *= 10        

        return outputArray
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



#-------------------------------------------------------------------------

numbers =  [18,6,27,2,30,9,15,21,4,25,11,12,0,8,3,22,14,7,16,20,28,1,19,26,10,17,5,23,13,29,24]
expected = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

x = CountingSort()
#-----
numbers = [2,20,61,997,1,619]
expected = [1, 2, 20, 61, 619, 997]
numbers = x.radixSort(numbers)

print(f'Radix sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')

#-----
numbers = [1,0,3,1,3,1]
expected = [0,1,1,1,3,3]
numbers = x.radixSort(numbers)

print(f'Radix sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')

#-----
numbers = [1,0,3,1,3,12]
expected = [0,1,1,3,3,12]
numbers = x.radixSort(numbers)

print(f'Radix sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')


#-----
numbers =  [18,6,27,2,30,9,15,21,4,25,11,12,0,8,3,22,14,7,16,20,28,1,19,26,10,17,5,23,13,29,24]
expected = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
numbers = x.radixSort(numbers)
print(f'Radix sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')

#-----

numbers =  [1, 0, 3, 1, 3, 1, 4, 5, 1, 3, 4, 1, 5, 5, 1, 3, 1, 3]
expected = [0, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5]
numbers = x.radixSort(numbers)
print(f'Radix sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')