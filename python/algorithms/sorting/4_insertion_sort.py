class InsertionSort:
    def __explanation_and_collapsable():
        pass    
        # The basic structure of this algorithm is: We have 2 partitions inside the array list, one is sorted and the other is unsorted.
        #   Then we loop through the array list, and we pick 1 element from the unsorted list and add them to the END of the sorted list. 
        #   In the process of adding to the sorted list, we compare the new element with the elements already in the sorted list, and if
        #   the new element is smaller than the element in the sorted list, we swap them. We keep doing this until the unsorted list is sorted
        #Ex:
        # 9,8,7,6,5,4,3,2,1,0
        # 9,8 -> 8,9 | 7,6,5,4,3,2,1,0
        # 8,9,7 -> 8,7,9 -> 7,8,9 | 6,5,4,3,2,1,0
        #
        # Insertion Sort is another sorting algorithm that takes O(n^2) time complexity. It's an in-place sorting algorithm and tends to be 
        #   more efficient than other O(n^2) sorting algorithms.
        #
        # Some other characteristics:
        # - Simple implementation
        # - Efficient for small data sets
        # - More efficient for small data sets than other O(n^2) algorithms
        # - Efficient for data sets that are somewhat already sorted
        # -Stable: Does not change the relative order of elements with equal key
        # - In-Place: only requires a constant amount of memory O(1)

    #-------------------------------------------------------------------------
    def sort(self,numbers):
        for i in range(1,len(numbers)):
            self.find_order(numbers, i)
        return numbers
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def find_order(self,numbers, from_idx): 

        while from_idx > 0:
            if numbers[from_idx - 1] > numbers[from_idx]:
                self.swap(numbers, from_idx - 1, from_idx)
            elif numbers[from_idx-1] < numbers[from_idx]:
                break
            #---
            from_idx -= 1

    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def swap(self,numbers, index1, index2):
        temp = numbers[index1]
        numbers[index1] = numbers[index2]
        numbers[index2] = temp
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

numbers = [18, 6, 27, 2, 30, 9, 15, 21, 4, 25, 11, 12, 0, 8, 3, 22, 14, 7, 16, 20, 28, 1, 19, 26, 10, 17, 5, 23, 13, 29]
x = InsertionSort()
result = x.sort(numbers)
print(f'Insertion sort result: {result}')
