import generator

##### Generate problems. #####
problem_list, answer_list = generator.krypto(
    200, 8, enable_mul=True, enable_div=True, enable_num_combine=True, max_answer=100)
# problem_num, number_of_digits, enable_mul, enable_div, enable_num_combine)
# print problem_list
print answer_list
