# import os
import subprocess
import time


def send_list_in_webpage(content_list, email_addr):
    filename = str(time.time()) + ".html"
    # filename_with_path = "\home\du\httpd\math\\" + filename
    temp_file = open(filename, "w")
    temp_file.write('<html><body><font face = "courier" size="7">')
    for item in content_list:
        temp_file.write(item.replace(
            "\n", "<br>").replace(" ", "&nbsp") + "<br>")
    temp_file.write("</font></body></html>")
    temp_file.close()
    # subprocess.call(["mv", filename, "/home/du/httpd/math/"])

    filename_for_email = "./temp.txt"
    temp_file = open(filename_for_email, "w")
    temp_file.write("http://18691db489.iok.la/math/" + filename)
    temp_file.close()

    pipe1 = subprocess.Popen(
        ("cat", filename_for_email), stdout=subprocess.PIPE)
    screen_output = subprocess.check_output(
        ("./sendnote", filename), stdin=pipe1.stdout)
    print screen_output
    subprocess.call(["rm", filename_for_email])
    subprocess.call(["rm", filename])


def send_list_in_html(content_list, email_addr):
    filename = "./temp.html"
    temp_file = open(filename, "w")
    temp_file.write('<html><body><font face = "courier" size="3">')
    for item in content_list:
        temp_file.write(item + "\n")
    temp_file.write("</font></body></html>")
    temp_file.close()
    pipe1 = subprocess.Popen(("cat", filename), stdout=subprocess.PIPE)
    screen_output = subprocess.check_output("./sendnote", stdin=pipe1.stdout)
    print screen_output
    subprocess.call(["rm", filename])


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
