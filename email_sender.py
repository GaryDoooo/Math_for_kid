# import os
import subprocess


def send_list(content_list, email_addr):
    filename = "./temp.txt"
    # subprocess.check_output(["mktemp", "/tmp/du.tmp.XXXXXX"])
    # print "temp file", filename
    temp_file = open(filename, "w")
    for item in content_list:
        temp_file.write(item + "\n")
    temp_file.close()
    pipe1 = subprocess.Popen(("cat", filename), stdout=subprocess.PIPE)
    screen_output = subprocess.check_output("./sendnote", stdin=pipe1.stdout)
    print screen_output
    # print pipe1.stdout
    # call(["sendfile", filename])
    subprocess.call(["rm", filename])
    # call(["./send_temp.txt_and_del", email_addr])
