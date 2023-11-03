
#-------------------------------------------------------------------------
class QuickSort:
    #-------------------------------------------------------------------------
    def __swap(self, array, idx1, idx2):
        temp = array[idx1]
        array[idx1] = array[idx2]
        array[idx2] = temp
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def partition(self, array, idx_from_left, idx_from_right):
        i = idx_from_left
        pivot = array[idx_from_right]

        for j in range(idx_from_left, idx_from_right):
            if array[j] <= pivot:
                self.__swap(array, i, j)
                i += 1

        # end of FOR
        #------
        self.__swap(array, i, idx_from_right)

        return i
    #-------------------------------------------------------------------------


    #-------------------------------------------------------------------------
    def sort(self,array, idx_from_left, idx_from_right):
        # index and items from left - is the first item starting from the left that
        #   is larger than our pivot

        #index and items from right - is the first item starting from the right that
        #  is smaller than our pivot
        
        if idx_from_left < idx_from_right:
            partition_idx = self.partition(array, idx_from_left, idx_from_right)
            self.sort(array, idx_from_left, partition_idx-1)
            self.sort(array, partition_idx+1, idx_from_right)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


numbers = [18, 6, 27, 2, 30, 9, 15, 21, 4, 25, 11, 12, 0, 8, 3, 22, 14, 7, 16, 20, 28, 1, 19, 26, 10, 17, 5, 23, 13, 29, 24]

x = QuickSort()
x.sort(numbers, 0, len(numbers)-1)
print(f'Quick sort result: {numbers}')