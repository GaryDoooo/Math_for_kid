#  import signal
#  TIMEOUT = 5  # number of seconds your want for timeout
#
#
#  def interrupted(signum, frame):
#  #    "called when read times out"
#  print 'interrupted!'
#
#
#  signal.signal(signal.SIGALRM, interrupted)
#
#
#  def input():
#  try:
#  print 'You have 5 seconds to type in your stuff...'
#  foo = raw_input()
#  print foo
#  #  return foo
#  except:
#  # timeout
#  return
#
#
#  # set alarm
#  signal.alarm(TIMEOUT)
#  s = input()
#  # disable the alarm after success
#  signal.alarm(0)
#  print 'You typed', s

#from press_any_key import raw_input_with_timeout

# raw_input_with_timeout(prompt="test", timeout=2)

from press_any_key import getch_timeout

s = None
i = 1
while s is None:
    print i
    i = i + 1
    s = getch_timeout()
