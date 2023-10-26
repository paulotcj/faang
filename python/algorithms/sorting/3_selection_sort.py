class SelectionSort:
    def sort(self,numbers):
        
        sorted = []
        while len(numbers) > 0:
            min_index = 0
            min_value = numbers[min_index]
            #----
            for i in range(len(numbers)):
                if numbers[i] < min_value:
                    min_index = i
                    min_value = numbers[i]
            #----
            numbers.pop(min_index)
            sorted.append(min_value)
        #end of while
        #----
        return sorted
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


numbers = [18, 6, 27, 2, 30, 9, 15, 21, 4, 25, 11, 12, 0, 8, 3, 22, 14, 7, 16, 20, 28, 1, 19, 26, 10, 17, 5, 23, 13, 29]

x = SelectionSort()
result = x.sort(numbers)   
print(f'Selection sort result: {result}')