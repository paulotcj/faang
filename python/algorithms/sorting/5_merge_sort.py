#-------------------------------------------------------------------------
class MergeSort:
    #-------------------------------------------------------------------------
    def sort(self,numbers):
        sor_list = []
        for i in numbers:
            sor_list.append( [i] )

        #house keeping we want to have an even number of lists
        if len(sor_list) % 2 != 0: sor_list.append( [] )

        current_idx = 0
        while len(sor_list) > 1:
            
            temp = self.merge(sor_list[current_idx], sor_list[current_idx+1])
            sor_list[current_idx] = temp
            sor_list.pop(current_idx+1)
            current_idx += 1

            if current_idx == len(sor_list):
                current_idx = 0
                if len(sor_list) != 1 and len(sor_list) % 2 != 0: sor_list.append( [] )

        #-----------------------
        return sor_list[0]


    #-------------------------------------------------------------------------

    def merge(self,left_l, right_l):
        return_list = []
        while len(left_l) > 0 and len(right_l) > 0:
            if left_l[0] <= right_l[0]:
                return_list.append(left_l.pop(0))
            else:
                return_list.append(right_l.pop(0))

        return return_list + left_l + right_l #if any of the lists is not empty, merge them here

        

#-------------------------------------------------------------------------

numbers = [18, 6, 27, 2, 30, 9, 15, 21, 4, 25, 11, 12, 0, 8, 3, 22, 14, 7, 16, 20, 28, 1, 19, 26, 10, 17, 5, 23, 13, 29, 24]

x = MergeSort()
result = x.sort(numbers)
print(f'Merge sort result: {result}')