import time
import subprocess as sp
import email_sender
import os
#from press_any_key import press_any_key_to_continue
from terminaltables import SingleTable
import threading
from select import select
import sys

#  from twisted.internet import task
#  from twisted.internet import reactor
#
#
#  class time_count_down:
#  def __init__(self, time_length_in_sec):
#  self.start_time = time.time()
#  self.end_time = self.start_time + time_length_in_sec
#  self.interrupt_process = task.LoopingCall(self.run_every_sec)
#  self.interrupt_process.start(1)
#  reactor.run()
#  self.ended = False
#
#  def run_every_sec(self):
#  t = self.end_time - time.time()
#  mins, secs = divmod(int(t + 0.5), 60)
#  timeformat = "%02d:%02d" % (mins, secs)
#  # print "\033[F"  # to the upper left corner of screen
#  print '\033[H'
#  print timeformat
#  if t < 1:
#  self.terminate()
#
#  def terminate(self):
#  self.interrupt_process.stop()
#  reactor.stop()
#  self.ended = True
#  sp.call('clear', shell=True)
#  print('Goodbye!\n\n\n\n\n')
#
#  def runEverySecond():
#  print "a second has passed"
#
#  def countdown(t):
#
#  l = task.LoopingCall(runEverySecond)
#  l.start(1.0)  # call every second
#  # l.stop() will stop the looping calls
#  reactor.run()

#  def countdown(t):
#  print ""
#  while t:
#  mins, secs = divmod(t, 60)
#  timeformat = "%02d:%02d" % (mins, secs)
#  # print "\033[F"  # to the upper left corner of screen
#  print '\033[H'
#  print timeformat
#  time.sleep(1)
#  t -= 1
#  sp.call('clear', shell=True)
#  print('Goodbye!\n\n\n\n\n')


class output:
    def __init__(self, problem_list, answer_list, time_length, email_addr):
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
        self.table = table
        self.countdown(60 * time_length)
        #  count_down = time_count_down(60 * time_length)
        #  while not count_down.ended:
        #  time.sleep(0.1)
        #  print count_down.ended
        # print "end"

    def waiting_keys(self):
        while not self.ended:
            # press_any_key_to_continue()
            # print "a key ",
            #timeout = 10
            # while is_alive(): # is_alive is a method to check some stuffs, might take 5 secs
            rlist, _, _ = select([sys.stdin], [], [], 0.001)
            if rlist:
                s = sys.stdin.readline()
                print repr(s), s
            # handle(s) # handle is a method to handle and react according to input

    def countdown(self, t):
        print ""
        self.ended = False
        thd = threading.Thread(target=self.waiting_keys)
        thd.start()
        while t:
            mins, secs = divmod(t, 60)
            timeformat = "%02d:%02d" % (mins, secs)
            # print "\033[F"  # to the upper left corner of screen
            print '\033[H'
            print timeformat
            time.sleep(1)
            t -= 1
        self.ended = True
        sp.call('clear', shell=True)
        print('Goodbye!\n\n\n\n\n')
