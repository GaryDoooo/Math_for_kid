from numpy import random


def two_number_add(
        first_number, second_number):
    a = random.randint(10**(first_number - 1), 10**first_number)
    b = random.randint(10**(second_number - 1), 10**second_number)
    new_problem = "%d + %d = " % (a, b)
    new_answer = new_problem + "%d" % (a + b)
    return new_problem, new_answer


def two_number_sub(
        first_number, second_number):
    a = random.randint(10**(first_number - 1), 10**(first_number))
    b = random.randint(10**(second_number - 1), 10**second_number)
    big = max(a, b)
    small = min(a, b)
    new_problem = "%d - %d = " % (big, small)
    new_answer = new_problem + "%d" % (big - small)
    return new_problem, new_answer


def two_number_mul(
        first_number, second_number):
    a = random.randint(10**(first_number - 1), 10**first_number)
    b = random.randint(10**(second_number - 1), 10**second_number)
    new_problem = "%d x %d = " % (a, b)
    new_answer = new_problem + "%d" % (a * b)
    return new_problem, new_answer


def two_number_div(
        first_number, second_number):
    a = random.randint(10**(first_number - 1), 10**first_number)
    b = random.randint(10**(second_number - 1), 10**second_number)
    new_problem = "%d / %d = " % (a, b)
    shang = int(a / b)
    remain = a % b
    if remain == 0:
        new_answer = new_problem + "%d " % shang
    else:
        new_answer = new_problem + "%d R%d" % (shang, remain)
    return new_problem, new_answer


def two_number_operation(
        first_number=3,
        second_number=3,
        operator=1,
        problem_num=10):
    problem_list = []
    answer_list = []
    for i in range(1, problem_num + 1):
        if operator == 1:
            new_problem, new_answer = two_number_add(
                first_number, second_number)
        elif operator == 2:
            new_problem, new_answer = two_number_sub(
                first_number, second_number)
        elif operator == 3:
            new_problem, new_answer = two_number_mul(
                first_number, second_number)
        elif operator == 4:
            new_problem, new_answer = two_number_div(
                first_number, second_number)
        problem_list.append(("[%d] " % i) + new_problem)
        answer_list.append(("[%d] " % i) + new_answer)
    return problem_list, answer_list
