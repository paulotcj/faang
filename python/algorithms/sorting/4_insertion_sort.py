class InsertionSort:
    # 9,8,7,6,5,4,3,2,1,0
    # 9,8 -> 8,9 | 7,6,5,4,3,2,1,0
    # 8,9,7 -> 8,7,9 -> 7,8,9 | 6,5,4,3,2,1,0
    #-------------------------------------------------------------------------
    def sort(self,numbers):
        for i in range(1,len(numbers)):
            self.find_order(numbers, i)
        return numbers
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def find_order(self,numbers, from_idx): #back-tracking

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
