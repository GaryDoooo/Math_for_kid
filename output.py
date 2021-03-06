import time
import subprocess as sp
import email_sender
import os
from terminaltables import SingleTable
import threading
from press_any_key import getch_timeout


def single_line_length(input_string):
    try:
        return input_string.index("\n")
    except ValueError:
        return len(input_string)


class output:
    def __init__(self, problem_list, answer_list, time_length, email_addr, send_html=False):
        rows, columns = os.popen('stty size', 'r').read().split()
        ##### Convert the problem list into a table #####
        problem_length = 0
        for problem in problem_list:
            problem_length = max(single_line_length(problem), problem_length)
        self.cols_in_table = int(int(columns) / (problem_length + 8))
        if (int(len(problem_list) / self.cols_in_table) > (int(rows) - 4) / 2):
            print "Too many problems for a small terminal screen... Try less."
            return
        self.current_problem = -1
        self.problem_list = problem_list
        self.problem_number = len(problem_list)
        #  if send_html:
            #  email_sender.send_list_in_webpage(answer_list, email_addr)
        #  else:
            #  email_sender.send_list(answer_list, email_addr)
        self.print_table(problem_list, self.current_problem)
        self.countdown(60 * time_length)

    def print_table(self, problem_list, highlight_position):
        if 0 <= highlight_position < len(problem_list):
            problem_list[highlight_position] = "\033[2;39m" + \
                problem_list[highlight_position].replace(
                "\n", "\033[22;39m\n\033[2;39m") + \
                "\033[22;39m"  # \033[2m set print to dim, \033[22m reset back dim
        newlist = []
        for i in range(0, len(problem_list), self.cols_in_table):
            start = i
            end = i + self.cols_in_table
            newlist.append(problem_list[start:end])
        table = SingleTable(newlist)
        table.inner_heading_row_border = False
        table.title = 'Enjoy'
        table.inner_row_border = True
        sp.call('clear', shell=True)
        print "Timer:\n\n"
        print table.table

    def waiting_keys(self):
        while not self.ended:
            s = getch_timeout(0.01)
            if s is not None:
                self.current_problem += 1
                if self.current_problem >= self.problem_number:
                    self.ended = True
                self.print_table(self.problem_list, self.current_problem)

    def countdown(self, t):
        print ""
        self.ended = False
        thd = threading.Thread(target=self.waiting_keys)
        thd.start()
        while t:
            mins, secs = divmod(t, 60)
            timeformat = "%02d:%02d" % (mins, secs)
            print '\033[H'  # Go to the upper left corner
            print timeformat
            time.sleep(1)
            t -= 1
            if self.ended:
                break
        self.ended = True
        sp.call('clear', shell=True)
        print('Goodbye!\n\n\n\n\n')
