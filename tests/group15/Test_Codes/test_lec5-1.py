import lec5_tuples_lists as lec

def quotient_and_remainder_test():
    assert lec.quotient_and_remainder(8,5) == (1,3)
    assert lec.quotient_and_remainder(100, 1) == (100, 0)
    print ("q&r test successful!!")

def get_data_test():
    test1 = ((1,'a'), (2, 'b'),(3, 'c'), (4, 'c') )
    assert lec.get_data(test1) == (1, 4, 3)
    print ("get data test successful!!")

quotient_and_remainder_test()
get_data_test()