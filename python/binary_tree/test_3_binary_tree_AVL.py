from binary_tree_AVL import BinaryTreeAVL



#----------------
# INSERT tests
def test_insert_rightHeavy_straight():
    #  50
    #    75
    #      100

    #arrange
    tree = BinaryTreeAVL()

    assert_values = [
        'curr v: 50,\tleft: None,\tright: 75,\theight: 3,\tparent:None,\tbalance:-2',
        'curr v: 75,\tleft: None,\tright: 100,\theight: 2,\tparent:50,\tbalance:-1',
        'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0'
    ]    

    #act
    tree.insert(50)
    tree.insert(75)
    tree.insert(100)    
    result_list = tree.print_generate_strings()


    #assert
    assert assert_values[0] == result_list[0]
    assert assert_values[1] == result_list[1]
    assert assert_values[2] == result_list[2]

def test_insert_leftHeavy_straight():
    #      50
    #    25
    #  10

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 50,\tleft: 25,\tright: None,\theight: 3,\tparent:None,\tbalance:2', 
                     'curr v: 25,\tleft: 10,\tright: None,\theight: 2,\tparent:50,\tbalance:1', 
                     'curr v: 10,\tleft: None,\tright: None,\theight: 1,\tparent:25,\tbalance:0']   

    #act
    tree.insert(50)
    tree.insert(25)
    tree.insert(10) 
    result_list = tree.print_generate_strings()

    #assert
    assert assert_values[0] == result_list[0]
    assert assert_values[1] == result_list[1]
    assert assert_values[2] == result_list[2]   

def test_insert_rightHeavy_angled():
    #  50
    #    75
    #  60

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 50,\tleft: None,\tright: 75,\theight: 3,\tparent:None,\tbalance:-2', 
                     'curr v: 75,\tleft: 60,\tright: None,\theight: 2,\tparent:50,\tbalance:1', 
                     'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']  

    #act
    tree.insert(50)
    tree.insert(75)
    tree.insert(60) 
    result_list = tree.print_generate_strings()


    #assert
    assert assert_values[0] == result_list[0]
    assert assert_values[1] == result_list[1]
    assert assert_values[2] == result_list[2]

def test_insert_leftHeavy_angled():
    #    50
    #  25
    #    30

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 50,\tleft: 25,\tright: None,\theight: 3,\tparent:None,\tbalance:2', 
                     'curr v: 25,\tleft: None,\tright: 30,\theight: 2,\tparent:50,\tbalance:-1', 
                     'curr v: 30,\tleft: None,\tright: None,\theight: 1,\tparent:25,\tbalance:0'] 

    #act
    tree.insert(50)
    tree.insert(25)
    tree.insert(30)
    result_list = tree.print_generate_strings()


    #assert
    assert assert_values[0] == result_list[0]
    assert assert_values[1] == result_list[1]
    assert assert_values[2] == result_list[2]

def test_insert_tree_50_25_75_60_100():
    #       50
    #    25     75
    #         60  100   

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 50,\tleft: 25,\tright: 75,\theight: 3,\tparent:None,\tbalance:-1', 
                     'curr v: 25,\tleft: None,\tright: None,\theight: 1,\tparent:50,\tbalance:0', 
                     'curr v: 75,\tleft: 60,\tright: 100,\theight: 2,\tparent:50,\tbalance:0', 
                     'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                     'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']
    tree.insert(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(60)
    tree.insert(100)

    #act
    result_list = tree.print_generate_strings()


    #assert
    for i in range(len(result_list)):
        assert assert_values[i] == result_list[i]

#----------------
#----------------
# ROTATE TEST
def test_rotate_left():
    #       50
    #    25     75
    #         60  100   

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 75,\tleft: 50,\tright: 100,\theight: 3,\tparent:None,\tbalance:1', 
                     'curr v: 50,\tleft: 25,\tright: 60,\theight: 2,\tparent:75,\tbalance:0', 
                     'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                     'curr v: 25,\tleft: None,\tright: None,\theight: 1,\tparent:50,\tbalance:0', 
                     'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:50,\tbalance:0'] 

    tree.insert(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(60)
    tree.insert(100)   

    #act
    target = tree.lookup(50)
    tree.left_rotate(target)
    result_list = tree.print_generate_strings()

    #assert
    #assert
    for i in range(len(result_list)):
        assert assert_values[i] == result_list[i]    

def test_rotate_right():
    #       50
    #    25     75
    #         60  100   

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 25,\tleft: None,\tright: 50,\theight: 4,\tparent:None,\tbalance:-3', 
                     'curr v: 50,\tleft: None,\tright: 75,\theight: 3,\tparent:25,\tbalance:-2', 
                     'curr v: 75,\tleft: 60,\tright: 100,\theight: 2,\tparent:50,\tbalance:0', 
                     'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                     'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']

    tree.insert(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(60)
    tree.insert(100) 

    #act
    target = tree.lookup(50)
    tree.right_rotate(target)
    result_list = tree.print_generate_strings()

    #assert
    #assert
    for i in range(len(result_list)):
        assert assert_values[i] == result_list[i]    

def test_rotate_left_then_rotate_rigth():
    #       50                  75                 50
    #    25     75   ->     50      100   ->   25     75
    #         60  100     25  60                    60  100
    # 
    # left followed by a right rotation should reverse all changes
    # and the tree should be back to its original configuration 

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 50,\tleft: 25,\tright: 75,\theight: 3,\tparent:None,\tbalance:-1', 
                     'curr v: 25,\tleft: None,\tright: None,\theight: 1,\tparent:50,\tbalance:0', 
                     'curr v: 75,\tleft: 60,\tright: 100,\theight: 2,\tparent:50,\tbalance:0', 
                     'curr v: 60,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                     'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']

    tree.insert(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(60)
    tree.insert(100)   

    #act
    #---------
    target = tree.lookup(50) #initial root node
    tree.left_rotate(target)

    target = tree.lookup(75) #new root node after rotating
    tree.right_rotate(target)  
    #---------  

    result_list = tree.print_generate_strings()

    #assert
    for i in range(len(result_list)):
        assert assert_values[i] == result_list[i]      
#----------------
#----------------
# BALANCE AVL tests
def test_insert_rightHeavy_straight_balance_AVL():
    #  50
    #    75
    #      100

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 75,\tleft: 50,\tright: 100,\theight: 2,\tparent:None,\tbalance:0', 
                     'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                     'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0']

    #act
    tree.insert(50)
    tree.insert(75)
    tree.insert(100)    
    target = tree.lookup(100)
    tree.balance_avl(target)
    result_list = tree.print_generate_strings()


    #assert
    assert assert_values[0] == result_list[0]
    assert assert_values[1] == result_list[1]
    assert assert_values[2] == result_list[2]

def test_insert_leftHeavy_straight_balance_AVL():
    #      50
    #    25
    #  10

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 25,\tleft: 10,\tright: 50,\theight: 2,\tparent:None,\tbalance:0', 
                     'curr v: 10,\tleft: None,\tright: None,\theight: 1,\tparent:25,\tbalance:0', 
                     'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:25,\tbalance:0']  

    #act
    tree.insert(50)
    tree.insert(25)
    tree.insert(10) 
    target = tree.lookup(10)
    tree.balance_avl(target)
    result_list = tree.print_generate_strings()

    #assert
    assert assert_values[0] == result_list[0]
    assert assert_values[1] == result_list[1]
    assert assert_values[2] == result_list[2]   

def test_insert_rightHeavy_angled_balance_AVL():
    #  50
    #    75
    #  60

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 60,\tleft: 50,\tright: 75,\theight: 2,\tparent:None,\tbalance:0', 
                     'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:60,\tbalance:0', 
                     'curr v: 75,\tleft: None,\tright: None,\theight: 1,\tparent:60,\tbalance:0'] 

    #act
    tree.insert(50)
    tree.insert(75)
    tree.insert(60) 
    target = tree.lookup(60)
    tree.balance_avl(target)    
    result_list = tree.print_generate_strings()


    #assert
    assert assert_values[0] == result_list[0]
    assert assert_values[1] == result_list[1]
    assert assert_values[2] == result_list[2]

def test_insert_leftHeavy_angled_balance_AVL():

    #    50
    #  25
    #    30

    #arrange
    tree = BinaryTreeAVL()

    assert_values = ['curr v: 30,\tleft: 25,\tright: 50,\theight: 2,\tparent:None,\tbalance:0', 
                     'curr v: 25,\tleft: None,\tright: None,\theight: 1,\tparent:30,\tbalance:0', 
                     'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:30,\tbalance:0']

    #act
    tree.insert(50)
    tree.insert(25)
    tree.insert(30)
    target = tree.lookup(30)
    tree.balance_avl(target)    
    result_list = tree.print_generate_strings()


    #assert
    for i in range(len(result_list)):
        assert assert_values[i] == result_list[i]
#----------------
#----------------
# INSERT AVL
def test_insertAVL_right_straight():

    #arrange
    tree = BinaryTreeAVL()

    # assert_values = ['curr v: 75,\tleft: 50,\tright: 125,\theight: 3,\tparent:None,\tbalance:-1', 
    #                  'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
    #                  'curr v: 125,\tleft: 100,\tright: 150,\theight: 2,\tparent:75,\tbalance:0', 
    #                  'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:125,\tbalance:0', 
    #                  'curr v: 150,\tleft: None,\tright: None,\theight: 1,\tparent:125,\tbalance:0']
    
    assert_values = ['curr v: 75,\tleft: 50,\tright: 125,\theight: 6,\tparent:None,\tbalance:-4', 
                     'curr v: 50,\tleft: None,\tright: None,\theight: 1,\tparent:75,\tbalance:0', 
                     'curr v: 125,\tleft: 100,\tright: 175,\theight: 5,\tparent:75,\tbalance:-3', 
                     'curr v: 100,\tleft: None,\tright: None,\theight: 1,\tparent:125,\tbalance:0', 
                     'curr v: 175,\tleft: 150,\tright: 225,\theight: 4,\tparent:125,\tbalance:-2', 
                     'curr v: 150,\tleft: None,\tright: None,\theight: 1,\tparent:175,\tbalance:0', 
                     'curr v: 225,\tleft: 200,\tright: 250,\theight: 3,\tparent:175,\tbalance:-1', 
                     'curr v: 200,\tleft: None,\tright: None,\theight: 1,\tparent:225,\tbalance:0', 
                     'curr v: 250,\tleft: None,\tright: 275,\theight: 2,\tparent:225,\tbalance:-1', 
                     'curr v: 275,\tleft: None,\tright: None,\theight: 1,\tparent:250,\tbalance:0']
    tree.insert_avl(50)
    tree.insert_avl(75)
    tree.insert_avl(100)
    tree.insert_avl(125)
    tree.insert_avl(150)

    tree.insert_avl(175)
    tree.insert_avl(200)
    tree.insert_avl(225)
    tree.insert_avl(250)
    tree.insert_avl(275)

    #act
    result_list = tree.print_generate_strings()


    #assert
    for i in range(len(result_list)):
        assert assert_values[i] == result_list[i]    






    


