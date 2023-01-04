import os
import smtplib
import time


def emailer(ip):
    sender_email = "timmy.degrano@gmail.com"  #
    rec_email = "olofssonlinus97@gmail.com"

    password = str("INSERT EMAIL PASSWORD OR LINK TO ENCRYPTED FILE")

    message = str(ip)+str(" is down")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print('Login success')
    server.sendmail(sender_email, rec_email, message)
    print('Email been sent')


def scan(end):
    # results_file_up = open("results_up.txt", "w")
    ip_list = []
    for ip in range(1, end):
        ip_list.append("192.168.50." + str(ip))

    ip_controll = ["192.168.50.1", '192.168.50.5', '192.168.50.17', "192.168.50.35", '192.168.50.99', '192.168.50.238']

    for ip in ip_list:
        print(f"current {ip} to be pinged")
        response = os.popen(f"ping {ip} -n 1").read()
        if "Received = 1" and "Approximate" in response:
            # results_file_up.write(f"UP: {ip} Ping Successful" + "\n")
            print(f"UP {ip} ping successful")
        else:
            for i in ip_controll:
                if ip == i:
                    msg=i
                    emailer(msg)
    # results_file_up.close()

localtime = time.localtime()
print('Initial scan starting at:' + time.strftime("%I:%M:%S %p", localtime))

while True:
    scan(10)
    localtime = time.localtime()
    print('breaktime at:' + time.strftime("%I:%M:%S %p", localtime) + '\nNext scan in 30 minutes')
    time.sleep(1800)
    print('NewScan starting at:' + time.strftime("%I:%M:%S %p", localtime))
