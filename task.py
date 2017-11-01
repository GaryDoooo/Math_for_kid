#!/usr/bin/python

# Copyright 2017 Garry Du
#

import argparse
#import glob
#import os

import generator
import output
from press_any_key import press_any_key_to_continue


def dispatch(time_length,
             first_number,
             second_number,
             operator,
             problem_num,
             email_addr
             ):
    ###### input validation ########
    if not (0 < time_length <= 1000):
        print "Expect time within 1 to 1000 minutes. Set time to 10 min."
        press_any_key_to_continue()
        time_length = 10
    if not (0 < first_number <= 18):
        print "Digits of a number is expected between 1 and 18. Set to 3."
        press_any_key_to_continue()
        first_number = 3
    if not (0 < second_number <= 18):
        print "Digits of a number is expected between 1 and 18. Set to 3."
        press_any_key_to_continue()
        second_number = 3
    operator_in_number = 1  # 1 is add
    print operator
    if (operator == "s"):
        operator_in_number = 2  # 2 is sub
    elif (operator == "m"):
        operator_in_number = 3  # 3 is mul
    elif (operator == "d"):
        operator_in_number = 4  # 4 is div
    if not (0 < problem_num <= 200):
        print "We usually give at least one problem or no more than 200... Set to 10."
        press_any_key_to_continue()
        problem_num = 10

    ##### Generate problems. #####
    problem_list, answer_list = generator.two_number_operation(
        first_number, second_number, operator_in_number, problem_num)
    # problem and answer should be lists of strings

    ##### Output answer and problems #####
    output.output(problem_list, answer_list, time_length, email_addr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--time-length',
                        required=True,
                        type=int,
                        help='How many minutes to finish the problem set. After that an email reminder will be sent.')
    parser.add_argument('--first-number',
                        required=True,
                        type=int,
                        help='How many digits the first number has.')
    parser.add_argument('--second-number',
                        required=True,
                        type=int,
                        help='How many digits the second number has.')
    parser.add_argument('--operator',
                        type=str,
                        default='a',
                        help="The operator in the middle. Can be a, s, m, and d.")
    parser.add_argument('--problem-num',
                        type=int,
                        default=10,
                        help='The number of problems to generate.')
    parser.add_argument('--email-addr',
                        type=str,
                        default="gdu@gmx.us",
                        help='The Email address to receive ansers and reminders.')
    parse_args, unknown = parser.parse_known_args()

    dispatch(**parse_args.__dict__)
