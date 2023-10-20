from heap_priority_queue_array import MinHeapArray

#------------------------------------------------------------------
class Test_MinHeapArray:
    #------------------------------------------------------------------
    def test_get_parent_idx(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0, 'parent_idx':None},
            {'idx':1, 'parent_idx':0},
            {'idx':2, 'parent_idx':0},
            {'idx':3, 'parent_idx':1},
            {'idx':4, 'parent_idx':1},
            {'idx':5, 'parent_idx':2},
            {'idx':6, 'parent_idx':2},
            {'idx':7, 'parent_idx':3},
            {'idx':8, 'parent_idx':3},
            {'idx':9, 'parent_idx':4},
            {'idx':10, 'parent_idx':4},
            {'idx':11, 'parent_idx':5},
            {'idx':12, 'parent_idx':5},
            {'idx':13, 'parent_idx':6},
            {'idx':14, 'parent_idx':6},
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            parent_idx = heap.get_parent_idx(idx)
            test_result.append( {'idx': idx, 'parent_idx': parent_idx} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_parent_idx = expected_result[i]['parent_idx']
            t_idx = test_result[i]['idx']
            t_parent_idx = test_result[i]['parent_idx']

            assert e_idx == t_idx
            assert e_parent_idx == t_parent_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_parent_value(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        expected_result = [
            {'idx':0,  'parent_idx':None , 'value' : (0  + 2), 'parent_value' : None  },
            {'idx':1,  'parent_idx':0    , 'value' : (1  + 2), 'parent_value' : (0+2) },
            {'idx':2,  'parent_idx':0    , 'value' : (2  + 2), 'parent_value' : (0+2) },
            {'idx':3,  'parent_idx':1    , 'value' : (3  + 2), 'parent_value' : (1+2) },
            {'idx':4,  'parent_idx':1    , 'value' : (4  + 2), 'parent_value' : (1+2) },
            {'idx':5,  'parent_idx':2    , 'value' : (5  + 2), 'parent_value' : (2+2) },
            {'idx':6,  'parent_idx':2    , 'value' : (6  + 2), 'parent_value' : (2+2) },
            {'idx':7,  'parent_idx':3    , 'value' : (7  + 2), 'parent_value' : (3+2) },
            {'idx':8,  'parent_idx':3    , 'value' : (8  + 2), 'parent_value' : (3+2) },
            {'idx':9,  'parent_idx':4    , 'value' : (9  + 2), 'parent_value' : (4+2) },
            {'idx':10, 'parent_idx':4    , 'value' : (10 + 2), 'parent_value' : (4+2) },
            {'idx':11, 'parent_idx':5    , 'value' : (11 + 2), 'parent_value' : (5+2) },
            {'idx':12, 'parent_idx':5    , 'value' : (12 + 2), 'parent_value' : (5+2) },
            {'idx':13, 'parent_idx':6    , 'value' : (13 + 2), 'parent_value' : (6+2) },
            {'idx':14, 'parent_idx':6    , 'value' : (14 + 2), 'parent_value' : (6+2) },
        ]
        for i in expected_result:
            value = i['value']
            heap.heap.append(value)

        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            parent_value = heap.get_parent(idx)
            test_result.append( {'idx': idx, 'parent_value' : parent_value} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_parent_value = expected_result[i]['parent_value']

            t_idx = test_result[i]['idx']
            t_parent_value = test_result[i]['parent_value']

            assert e_idx == t_idx
            assert e_parent_value == t_parent_value
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_right_idx(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0, 'right_idx':2},
            {'idx':1, 'right_idx':4},
            {'idx':2, 'right_idx':6},
            {'idx':3, 'right_idx':8},
            {'idx':4, 'right_idx':10},
            {'idx':5, 'right_idx':12},
            {'idx':6, 'right_idx':14},
            {'idx':7, 'right_idx':16},
            {'idx':8, 'right_idx':18},
            {'idx':9, 'right_idx':20},
            {'idx':10, 'right_idx':22},
            {'idx':11, 'right_idx':24},
            {'idx':12, 'right_idx':26},
            {'idx':13, 'right_idx':28},
            {'idx':14, 'right_idx':30},
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            right_idx = heap.get_right_idx(idx)
            test_result.append( {'idx': idx, 'right_idx': right_idx} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_right_idx = expected_result[i]['right_idx']
            t_idx = test_result[i]['idx']
            t_right_idx = test_result[i]['right_idx']

            assert e_idx == t_idx
            assert e_right_idx == t_right_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_right_value(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0,  'right_value':2  },
            {'idx':1,  'right_value':4  },
            {'idx':2,  'right_value':6  },
            {'idx':3,  'right_value':8  },
            {'idx':4,  'right_value':10 },
            {'idx':5,  'right_value':12 },
            {'idx':6,  'right_value':14 },
            {'idx':7,  'right_value':16 },
            {'idx':8,  'right_value':18 },
            {'idx':9,  'right_value':20 },
            {'idx':10, 'right_value':22 },
            {'idx':11, 'right_value':24 },
            {'idx':12, 'right_value':26 },
            {'idx':13, 'right_value':28 },
            {'idx':14, 'right_value':30 },
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            right_idx = heap.get_right(idx)
            test_result.append( {'idx': idx, 'right_value': right_idx} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_right_value = expected_result[i]['right_value']
            t_idx = test_result[i]['idx']
            t_right_value = test_result[i]['right_value']

            assert e_idx == t_idx
            assert e_right_value == t_right_value
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    def test_get_left_idx(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0,  'left_idx':1  },
            {'idx':1,  'left_idx':3  },
            {'idx':2,  'left_idx':5  },
            {'idx':3,  'left_idx':7  },
            {'idx':4,  'left_idx':9  },
            {'idx':5,  'left_idx':11 },
            {'idx':6,  'left_idx':13 },
            {'idx':7,  'left_idx':15 },
            {'idx':8,  'left_idx':17 },
            {'idx':9,  'left_idx':19 },
            {'idx':10, 'left_idx':21 },
            {'idx':11, 'left_idx':23 },
            {'idx':12, 'left_idx':25 },
            {'idx':13, 'left_idx':27 },
            {'idx':14, 'left_idx':29 },
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            left_idx = heap.get_left_idx(idx)
            test_result.append( {'idx': idx, 'left_idx': left_idx} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_left_idx = expected_result[i]['left_idx']
            t_idx = test_result[i]['idx']
            t_left_idx = test_result[i]['left_idx']

            assert e_idx == t_idx
            assert e_left_idx == t_left_idx
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_get_left_value(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
         
        #arrange   
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for i in numbers:
            heap.heap.append(i)
        
        expected_result = [
            {'idx':0,  'left_value':1  },
            {'idx':1,  'left_value':3  },
            {'idx':2,  'left_value':5  },
            {'idx':3,  'left_value':7  },
            {'idx':4,  'left_value':9  },
            {'idx':5,  'left_value':11 },
            {'idx':6,  'left_value':13 },
            {'idx':7,  'left_value':15 },
            {'idx':8,  'left_value':17 },
            {'idx':9,  'left_value':19 },
            {'idx':10, 'left_value':21 },
            {'idx':11, 'left_value':23 },
            {'idx':12, 'left_value':25 },
            {'idx':13, 'left_value':27 },
            {'idx':14, 'left_value':29 },
        ]
        #act
        test_result = []
        for i in expected_result:
            idx = i['idx']
            left_value = heap.get_left(idx)
            test_result.append( {'idx': idx, 'left_value': left_value} )

        #assert
        for i in range(len(expected_result)):
            e_idx = expected_result[i]['idx']
            e_left_value = expected_result[i]['left_value']
            t_idx = test_result[i]['idx']
            t_left_value = test_result[i]['left_value']

            assert e_idx == t_idx
            assert e_left_value == t_left_value
    #------------------------------------------------------------------ 
    #------------------------------------------------------------------ 
    def test_is_idx_in_range(self):
        #arrange
        heap = MinHeapArray()
        numbers = [0,1,2,3,4,5,6,7,8,9]
        for i in numbers:
            heap.heap.append(i)

        expected_results = [
            {'idx': 0, 'result': True},
            {'idx': 1, 'result': True},
            {'idx': 2, 'result': True},
            {'idx': 3, 'result': True},
            {'idx': 4, 'result': True},
            {'idx': 5, 'result': True},
            {'idx': 6, 'result': True},
            {'idx': 7, 'result': True},
            {'idx': 8, 'result': True},
            {'idx': 9, 'result': True},

            {'idx': 10, 'result': False},
            {'idx': 11, 'result': False},
            {'idx': -1, 'result': False},
            {'idx': -2, 'result': False},
        ]
        #act
        test_results = []
        for i in expected_results:
            idx = i['idx']
            result = heap.is_idx_in_range(idx)
            test_results.append( {'idx':idx, 'result': result})

        #assert
        for i in range(len(expected_results)):
            e_idx = expected_results[i]['idx']
            e_result = expected_results[i]['result']
            t_idx = test_results[i]['idx']
            t_result = test_results[i]['result']

            assert e_idx == t_idx
            assert e_result == t_result
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_sift_up(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        # ------
        #                  90
        #        80                 100      
        #   70        85        95        105
        # 60  74    83  86    93  97   103  2
        #
        #arrange
        heap = MinHeapArray()
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13 14
        numbers = [90,  80,100,  70,85,95,105,  60,74,83,86,93,97,103,2]
        for i in numbers:
            heap.heap.append(i)

        expected_results = [2, 80, 90, 70, 85, 95, 100, 60, 74, 83, 86, 93, 97, 103, 105]

        #act
        heap.sift_up(14)
        test_results = heap.heap

        #assert
        for i in range(len(expected_results)):
            assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    def test_sift_up_2(self):
        #                              0,
        #               1,                           2,
        #        3,            4,              5,           6,
        #    7,     8,     9,    10,       11,    12,    13,   14
        #  15,16, 17,18, 19,20, 21,22,   23,24, 25,26, 27,28, 29,30  
        # ------
        #                  90
        #        80                 100      
        #   70        85        95        105
        # 60  74    83  2     93  97   103  107
        #
        #arrange
        heap = MinHeapArray()
        #          0    1   2    3  4  5  6     7  8  9  10 11 12 13  14
        numbers = [90,  80,100,  70,85,95,105,  60,74,83,2 ,93,97,103,107]
        for i in numbers:
            heap.heap.append(i)

        #                   0  1   2    3   4   5   6    7   8   9   10  11  12  13   14
        expected_results = [2, 90, 100, 70, 80, 95, 105, 60, 74, 83, 85, 93, 97, 103, 107]

        #act
        heap.sift_up(10)
        test_results = heap.heap
        print(test_results)

        # #assert
        # for i in range(len(expected_results)):
        #     assert expected_results[i] == test_results[i]
    #------------------------------------------------------------------    
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------
    #------------------------------------------------------------------

        
#------------------------------------------------------------------

e = Test_MinHeapArray()
e.test_sift_up_2()