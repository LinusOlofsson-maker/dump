import smtplib
from datetime import datetime
def emailer():
    sender_email = "timmy.degrano@gmail.com"  #
    rec_email = "olofssonlinus97@gmail.com"
    current_time = datetime.now()
    now = current_time.strftime("%d/%m/%Y %H:%M:%S")
    password = str("INSERT EMAIL PASSWORD OR LINK TO ENCRYPTED FILE")
    t = 54
    message = str("ALARM Movement detected at home!\nOccurred at: " + now)
    print(message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print('Login success')

    server.sendmail(sender_email, rec_email, message)

    print('Email been sent')


def main():
    emailer()


if __name__ == "__main__":
    main()
