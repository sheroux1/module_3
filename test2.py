def fib(lim_num, last_num = 0, this_num = 1):
    if lim_num > 0:
        print(f'Iteration {last_num}: {this_num}')
        fib(lim_num-1, this_num, last_num+this_num)




    # last_num = 0
    # this_num = 1
    # print(last_num)
    # print(this_num)
    # for i in range(2, lim_num):
    #     i = last_num + this_num
    #     last_num = this_num
    #     this_num = i
    #     print(i)



fib(10)