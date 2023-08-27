class BinarySearch:
    # def __init__()-> None:
    #     pass
        
    def search_iterative(self, list, lookup_item):
        low_idx = 0
        high_idx = len(list) - 1

        while low_idx <= high_idx:
            mid_idx = (low_idx + high_idx) // 2 #integer division only
            guess_v = list[mid_idx]
            if guess_v == lookup_item: 
                return mid_idx #return the index where we found the item
            
            #at this point we know that whatever value we were looking for, 
            # it's not our guess
            if guess_v > lookup_item : 
                #here the implication is that my guess was too high, so the value must be
                # within the low_idx and mid_idx. Therefore, the high_idx must be at least
                # one step below mid_idx
                high_idx = mid_idx - 1

            else: # guess < lookup_item
                #here my guess was too low. So the value must be within mid_idx, and high_idx
                # Therefore, my low_idx must be at least one step above mid_idx
                low_idx = mid_idx + 1


        return None

    def search_recursive(self, list, low_idx, high_idx, lookup_item):
        # Check base case 
        len_list = len(list)
        if high_idx >= low_idx: #considering things normal, this should be the default
    
            mid_idx = (high_idx + low_idx) // 2
            if mid_idx >= len_list: #out of bounds
                return None
            # print(f"    high_idx:{high_idx}, low_idx:{low_idx}, mid_idx:{mid_idx}")
            guess_v = list[mid_idx]
    
            # If element is present at the middle itself 
            if guess_v == lookup_item:
                return mid_idx 
            
            #at this point we know that whatever value we were looking for, 
            # it's not our guess
    
            elif guess_v > lookup_item: 
                #here the implication is that my guess was too high, so the value must be
                # within the low_idx and mid_idx. Therefore, the high_idx must be at least
                # one step below mid_idx  

                high_idx = mid_idx - 1              
                return self.search_recursive(list, low_idx, high_idx, lookup_item) 
    
            else: # guess < lookup_item
                #here my guess was too low. So the value must be within mid_idx, and high_idx
                # Therefore, my low_idx must be at least one step above mid_idx

                low_idx = mid_idx + 1
                return self.search_recursive(list, low_idx, high_idx, lookup_item) 
    
        else: 
            # Element is not present in the array 
            return None        

#-------------

#    1,2,3,4,5,6,7,8,9,10
#
#
#    looking for = 3
#
#    len = 10
#    min = 0
#    max = 9
#    mid = (0 + 9) // 2 = 9 // 2 = 4
#
#    guess = list[4] = 5 (too high)
#
#    max = mid - 1
#
#
#    min = mid + 1


if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,9,10]
    # search_for = 1
    bs = BinarySearch()

    for search_for in my_list:
        search_result_idx = bs.search_iterative(my_list, search_for)
        print(f"Searching for {search_for}, found at index : {search_result_idx}")
    print("---------------------")
    search_result_idx = bs.search_iterative(my_list, 99)
    print(f"Searching for {99}, found at index : {search_result_idx}")

    print("---------------------\n\n")

    for search_for in my_list:
        search_result_idx = bs.search_recursive(list= my_list, low_idx= 0, high_idx= len(my_list), lookup_item= search_for)
        print(f"Searching for {search_for}, found at index : {search_result_idx}")
    
    print("---------------------")
    look_v = 11
    search_result_idx = bs.search_recursive(list= my_list, low_idx= 0, high_idx= len(my_list), lookup_item= look_v)
    print(f"Searching for {look_v}, found at index : {search_result_idx}")

