class BinarySearch:
    def __init__()-> None:
        pass
    def search_iteractive(self, list, lookup_item):
        low_idx = 0
        high_idx = len(list) - 1

        while low_idx <= high_idx:
            mid_idx = (low_idx + high_idx) // 2 #integer division only
            guess = list[mid_idx]
            if guess == lookup_item: 
                return mid_idx #return the index where we found the item
            
            if guess > lookup_item :
                pass
            else:
                pass


        return None



#-------------

bs = BinarySearch()

