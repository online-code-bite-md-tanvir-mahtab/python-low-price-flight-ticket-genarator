import smtplib

# we are going to define some context
MY_GMAAIL ="rpg736tanvir@gmail.com"
MY_PASSWORD ="01955005706#@"
MAIL_RECIVER ="tanzin736@gmail.com"

class NotificationManager :

    # now i am going to create a method 
    # that will take message as argument
    # and return string
    def send_mail(self,message):
        # setting up the mail server
        # i am going to established theh connection with the email server
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            # for secure our messge and server we are going to do this
            connection.starttls()
            # then we are going to login to the gmail that we went to send thhe message from
            connection.login(user=MY_GMAAIL,password=MY_PASSWORD,initial_response_ok=True)
            # now i am goingn to send the meesage
            connection.sendmail(from_addr=MY_GMAAIL,to_addrs=MAIL_RECIVER,msg=f"Subject:plane ticket\n\n\n {message}")
        return "Mail is Sended...!"