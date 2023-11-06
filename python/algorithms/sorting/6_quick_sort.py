
#-------------------------------------------------------------------------
class QuickSort:
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