class CountingSort:

    def sort(self,input_array):
        # Find the maximum element in the inputArray
        maxEl = max(input_array)

        countArrayLength = maxEl+1

        # Initialize the countArray with (max+1) zeros
        countArray = [0] * countArrayLength

        # Step 1 -> Traverse the inputArray and increase 
        # the corresponding count for every element by 1
        for el in input_array: 
            countArray[el] += 1

        # Step 2 -> For each element in the countArray, 
        # sum up its value with the value of the previous 
        # element, and then store that value 
        # as the value of the current element
        for i in range(1, countArrayLength):
            countArray[i] += countArray[i-1] 

        # Step 3 -> Calculate element position
        # based on the countArray values
        outputArray = [0] * len(input_array)
        i = len(input_array) - 1
        while i >= 0:
            currentEl = input_array[i]
            countArray[currentEl] -= 1
            newPosition = countArray[currentEl]
            outputArray[newPosition] = currentEl
            i -= 1

        return outputArray


        


        


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