import time
import subprocess as sp
import email_sender
import os
from terminaltables import SingleTable


def countdown(t):
    print ""
    while t:
        mins, secs = divmod(t, 60)
        timeformat = "%02d:%02d" % (mins, secs)
        # print "\033[F"  # to the upper left corner of screen
        print '\033[H'
        print timeformat
        time.sleep(1)
        t -= 1
    sp.call('clear', shell=True)
    print('Goodbye!\n\n\n\n\n')


def output(problem_list, answer_list, time_length, email_addr):
    rows, columns = os.popen('stty size', 'r').read().split()
    ##### Convert the problem list into a table #####
    problem_length = 0
    for problem in problem_list:
        problem_length = max(len(problem), problem_length)
    cols_in_table = int(int(columns) / (problem_length + 8))
    if (int(len(problem_list) / cols_in_table) > (int(rows) - 4) / 2):
        print "Too many problems for a small terminal screen... Try less."
        return
    newlist = []
    for i in range(0, len(problem_list), cols_in_table):
        start = i
        end = i + cols_in_table
        newlist.append(problem_list[start:end])
    table = SingleTable(newlist)
    table.inner_heading_row_border = False
    table.title = 'Enjoy'
    table.inner_row_border = True

    email_sender.send_list(answer_list, email_addr)
    sp.call('clear', shell=True)
    print "Timer:\n\n"
    print table.table
    countdown(60 * time_length)
