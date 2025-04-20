def is_even_with_return( i ):
    print('with return')
    remainder = i % 2
    return remainder == 0


#####################################
print("=====================================")
print("**              Test1              **")
print("=====================================")
print(f"input: 20, output: {is_even_with_return(20)}")
print("-------------------------------------")
print(f"input: 21, output: {is_even_with_return(21)}")