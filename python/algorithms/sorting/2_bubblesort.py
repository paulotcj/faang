#-------------------------------------------------------------------------
class BubbleSort:

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




