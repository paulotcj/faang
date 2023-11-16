#-------------------------------------------------------------------------
class BubbleSort:
    def __explanation_and_collapsable():
        pass    
        # Bubble sort is the simplest sorting algorithm that works by repeatedly swapping adjacent elements. 
        # This algorithm is not suitable for large data sets as its average and worst time complexity is O(n^2).
        # Most practical algorithms have substantially better worst-case or average complexity, usually O(n.log n). 
        # Even other O(n^2) algorithms, such as insertion sort run faster than bubble sort.

        # For instance, if we consider the array:
        # [5, 1, 4, 2, 8] 
        #
        #  We start with the first element and compare it against the next element, if the next element is smaller than the current element
        #  we swap them. Then we move to the next element and repeat the process. We keep doing this until we reach the end of the array.
        #      
        # [5, 1, 4, 2, 8] -> [1, 5, 4, 2, 8] -> [1, 4, 5, 2, 8] -> [1, 4, 2, 5, 8] -> [1, 4, 2, 5, 8]
        #  ^                     ^                     ^                     ^                     ^
        # Now repeat the previous step for the number of elements in the array and we will end up with a sorted array.
        # [1,2,4,5,8]
        #
        # One thing to consider is that at the end of every pass, the largest element will be pushed to the end of the array, so we don't
        # need to compare it again. So in the next pass we can ignore the last element.
        # We also could stop a the algorithm if during a full step no swap was made, this meaning the array is already sorted.



    #-------------------------------------------------------------------------
    def sort(self,plist):
        return_list = plist.copy()
        #---
        for i in range(len(return_list)): #this is the loop the pushes the largest number to the end
            for j in range(len(return_list)-1): #this is the loop that compares the numbers
                if return_list[j] > return_list[j+1]:
                    self.__swap(return_list, j, j+1)
            #---
        #---
        return return_list

    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __swap(self,plist, index1, index2):
        temp = plist[index1]
        plist[index1] = plist[index2]
        plist[index2] = temp
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

numbers = [18, 6, 27, 2, 30, 9, 15, 21, 4, 25, 11, 12, 0, 8, 3, 22, 14, 7, 16, 20, 28, 1, 19, 26, 10, 17, 5, 23, 13, 29]
# numbers = [9,5,3,1,2,6,8,7,4]
x = BubbleSort()
result = x.sort(numbers)

print(f'Bubble sort result: {result}')




