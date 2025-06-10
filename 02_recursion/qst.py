<<<<<<< HEAD
def new_func (n):
    # new function
    if n == 0:
        #print(stop)
        return 0
    else:
        print(f"value of n is(n)")
        new_func(n-1)


=======
def new_func(n):
    # new_func(n)
    if n == 0:
        # print("Stop")
        return 0
    else:
        print(f"Value of n is {n}")
        new_func(n - 1)  # function calling itself 
    
>>>>>>> 3e6d2e96315ea3893c9c59ebe125def4ca12ee42
new_func(5)