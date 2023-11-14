#-------------------------------------------------------------------------
class MergeSort:
    # Merge Sort is an efficient, general-purpose sorting algorithm. Most implementations produce a stable sort. Merge sort is a divide-and-conquer algorithm.
    # Performance-wise, Merge Sort has a worst case of O(n.log n).
    #
    # The algorithm:
    # - Break down the array ist until you have only the individual elements, so in the case of the array:
    # [38,27,43,3,9,89,10]
    #
    #    we get -> [  [38],  [27],  [43],  [3],  [9],  [89],  [10]  ]
    #
    #    Note this is not an even number of elements, and to make this algorithm to work we need to fix this, so the final list should be:
    # [  [38],  [27],  [43],  [3],  [9],  [89],  [10],  []  ]
    #
    # Now we merge:
    #
    # [  [38],  [27],  [43],  [3],  [9],  [89],  [10],  []  ]
    #      |    /       |    /       |    /       |    /
    # [  [27,38]    ,  [3,43]    ,  [9,89]    ,  [10]       ]
    #       |           /              |        /
    # [  [3, 27, 38,  43]        ,  [9, 10, 89]             ]
    #       |                      /   
    # [  3, 9, 10, 27, 38, 43, 89]       -> sorted    


    #-------------------------------------------------------------------------
    def sort(self,numbers):
        #-----
        sor_list = []
        for i in numbers:
            sor_list.append( [i] ) #this will be a list of lists, each list will have only one element

        #house keeping we want to have an even number of lists
        if len(sor_list) % 2 != 0: 
            sor_list.append( [] )
        #-----

        current_idx = 0
        while len(sor_list) > 1: #keep looping until we have only one list. Stop at 1 list since this is the final and sorted list
            
            temp = self.merge(sor_list[current_idx], sor_list[current_idx+1]) #merge and sort the both lists
            sor_list[current_idx] = temp
            sor_list.pop(current_idx+1) #this list is no longer needed since we have a merged and sorted list at 'sor_list[current_idx] = temp'
            current_idx += 1

            if current_idx == len(sor_list): #time to reset and start over processing pairs of lists
                current_idx = 0
                if len(sor_list) != 1 and len(sor_list) % 2 != 0: #keep the list numbers even
                    sor_list.append( [] )

        #-----------------------
        return sor_list[0] #return the final and sorted list


    #-------------------------------------------------------------------------
    # Merge function algorithm: This function receives 2 parameters a left list and a right list, and both lists should or
    #  are expected to have a similar size. So then the function will loop until one of the lists turns empty. Inside the loop
    #  the function compare the first item im both lists, whichever is smaller is poped from the source list and then appended
    #  to the return list. Ths process repeats until one of the lists is empty. Then before returning the return list, there's a
    #  possibility that one of the lists is not empty, in which case we append this list to the return list, because at this point
    #  we know the remaining element should be the largest one.
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