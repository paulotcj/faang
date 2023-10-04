class PriorityQueue_Dict:
    def __init__(self) -> None:
        self.dict = {}

    def insert(self,priority,value):
        if priority not in self.dict:
            self.dict[priority] = []
            self.dict = {key: self.dict[key] for key in sorted(self.dict)}

        self.dict[priority].append(value)

    def pop(self):
        return_value = None
        for dict_k, dict_v in self.dict.items():
            return_value = [dict_k,dict_v.pop(0)]
            break
        #---

        if return_value:
            if self.dict[return_value[0]] == None or len(self.dict[return_value[0]]) == 0:
                del self.dict[return_value[0]]

        return return_value
    
    def print(self):

        for i in self.print_generate_output():
            print(f'Priority: {i[0]} - Value: {i[1]}')

    def print_generate_output(self):
        return_obj = []
        #-------
        temp = self.pop()
        while temp:
            return_obj.append(temp)
            temp = self.pop()        

        return return_obj
    
    #--------




    
class Test_PriorityQueue_Dict:
    def test_test1(self):
        pass
        #arrange
        pq = PriorityQueue_Dict()
        pq.insert(1 , 'John')
        pq.insert(4 , 'Mike')
        pq.insert(7 , 'Alan')
        pq.insert(3 , 'Jessica')
        pq.insert(1 , 'Miley')
        pq.insert(2 , 'Ron')
        pq.insert(1 , 'Travis')
        pq.insert(2 , 'Johnny')
        pq.insert(7 , 'Lamar')
        pq.insert(2 , 'Don')
        pq.insert(2 , 'Mackenzie')
        pq.insert(1 , 'Ashley')
        pq.insert(5 , 'Jenny')
        
        assert_values = [[1, 'John'], 
                         [1, 'Miley'], 
                         [1, 'Travis'], 
                         [1, 'Ashley'], 
                         [2, 'Ron'], 
                         [2, 'Johnny'], 
                         [2, 'Don'], 
                         [2, 'Mackenzie'], 
                         [3, 'Jessica'], 
                         [4, 'Mike'], 
                         [5, 'Jenny'], 
                         [7, 'Alan'], 
                         [7, 'Lamar']]
        
        #act
        result_list = pq.print_generate_output()
        
        #assert
        for i in range(len(assert_values)):
            assert assert_values[i][0] == result_list[i][0]
            assert assert_values[i][1] == result_list[i][1]
            

