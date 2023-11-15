
#-------------------------------------------------------------------------
class QuickSort:
    # Quick Sort is an efficient sorting algorithm. Its average performance is O(n.log n), but the worst-case scenario is still O(n^2).
    # Quick Sort is a commonly used sorting algorithm, and is usually slightly faster than merge sort, particularly for larger data sets.
    #
    # The algorithm:
    #   Consider the array: [20,50,10,30,80,60,90,70,40]
    #   We pick a pivot, and for this example we will take the last element of the array, in this case: 40
    #    then we start from a given left index up to a given right index, and we compare the values with the pivot,
    #    if the value is less than the pivot, we swap the value, moving it to the left side. And we continue to do this for all
    #    the elements in the range.
    #    Eventually there will be a point where the last swap was made, meaning, all the values to the left are smaller than our pivot,
    #    and all the values to the right are larger than our pivot. So we swap the pivot with this last swap position.
    #
    #  So this would be:
    #   [20,50,10,30,80,60,90,70,40] -> [20,50,10,30,80,60,90,70,40] -> [20,50,10,30,80,60,90,70,40] ->  [20,10,50,30,80,60,90,70,40] -> 
    #    ^^                      P       ^  ^                    P          ^  ^                 P              ^  ^              P
    #
    #  [20,10,30,50,80,60,90,70,40] -> [20,10,30,50,80,60,90,70,40] -> [20,10,30,50,80,60,90,70,40] -> [20,10,30,50,80,60,90,70,40] -> 
    #            ^  ^           P                   ^  ^        P                      ^  ^     p                         ^  ^  p 
    #
    #  [20,10,30,50,80,60,90,70,40] -> DONE.  The last swap was where 50 is sitting right now, so we swap the pivot with 50.
    #                        ^^ P 
    #
    # [20,10,30,40,80,60,90,70,50] in this case, the pivot, 40, is in the correct position. Now we have to partition the array in two parts,
    #  left and right of the pivot, and repeat the process for each partition.
    #
    # LEFT PART = [20,10,30],  RIGHT PART = [80,60,90,70,50],  and then you repeat the process for each partition until all is sorted
    #
    # [20,10,30] -> [20,10,30] -> [10,20,30] -> DONE
    #  ^^    P       ^  ^  P          ^^ P
    #
    # Then you do the same for: [10,20]  which happens to be already sorted.
    # So far we have: [10,20,30,40,  80,60,90,70,50]
    #                  < sorted  >   <  unsorted  >
    #
    # [80,60,90,70,50] -> [80,60,90,70,50] -> DONE, no swap made, so we swap the pivot with the last swap position
    # [50,60,90,70,80]
    # 
    # Now we process [60,90,70,80] -> [60,90,70,80] -> [60,70,90,80] -> DONE, we swap the pivot with the last swap position
    # [60,70,80,90]
    #
    # Now we process [60,70] -> [60,70] -> DONE, we swap the pivot with the last swap position
    # [60, 70]
    #
    # Now we process [90] -> [90] -> DONE
    # 
    # Let's put all together: [10,20,30,40] + [60,70] + [80] + [90] =  [10,20,30,40,60,70,80,90]

    #-------------------------------------------------------------------------
    def __swap(self, array, idx1, idx2):
        temp = array[idx1]
        array[idx1] = array[idx2]
        array[idx2] = temp
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    def __partition2(self,array, idx_from_left, idx_from_right):
        # Algorithm: Run through the partition and compare with the pivot. All values smaller than the pivot
        # must be placed on the left.
        
        v_pivot = array[idx_from_right]
        idx_pivot = idx_from_right    # we picked pivot as the last item, so we skip the swap between pivot and the last item
        #---
        for i in range(idx_from_left, idx_from_right): # index i is used to scan the array partition
            v_i = array[i]
            if v_i < v_pivot: #select all items that are smaller than the pivot and put them in the left partition
                v_from_left = array[idx_from_left]
                self.__swap(array, idx_from_left, i) # we are sure to be placing an smaller item on the left side
                idx_from_left += 1                   #  and then we increase the index by 1
            #---
        #end of for

        # now we know the position which the pivot must be placed, which is idx_from_left. So we swap the pivot with the item
        #  note: all elements on the right side are now guaranteed to be larger than the pivot
        self.__swap(array, idx_from_left, idx_pivot)
        return idx_from_left
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def sort(self,array, idx_from_left, idx_from_right):

        if idx_from_left < idx_from_right:
            partition_idx = self.__partition2(array, idx_from_left, idx_from_right)
            self.sort(array, idx_from_left, partition_idx-1)
            self.sort(array, partition_idx+1, idx_from_right)
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    def sort2(self, array, idx_from_left, idx_from_right):
        stack = [(idx_from_left, idx_from_right)]

        while stack:
            idx_from_left, idx_from_right = stack.pop()

            if idx_from_left < idx_from_right:
                partition_idx = self.__partition2(array, idx_from_left, idx_from_right)
                                                                           # suppose partition_idx = 5
                stack.append( ( idx_from_left     , partition_idx - 1 ) )  # (0, 4)
                stack.append( ( partition_idx + 1 , idx_from_right    ) )  # (6, 9)
            # else:
            #     print(f'---\nInvalid condition, idx_from_left >= idx_from_right.\n\tidx_from_left: {idx_from_left}\tidx_from_right: {idx_from_right}')
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


numbers =  [18,6,27,2,30,9,15,21,4,25,11,12,0,8,3,22,14,7,16,20,28,1,19,26,10,17,5,23,13,29,24]
expected = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

x = QuickSort()
x.sort2(numbers, 0, len(numbers)-1)
print(f'Quick sort result: {numbers}')
print(f'Is the result correct? {numbers == expected}')