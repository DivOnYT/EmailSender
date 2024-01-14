#Importing all resources
import os, smtplib, time, json,ssl
from get_emails import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Variables Const
timer = 5 # Timer in seconds between each email
SMTP_SERVER = "smtp.gmail.com"  # link of the SMTP SERVER
SMTP_PORT = 587 # port to connect of the SMTP SERVER
mailbox = "" # mailbox like test@gmail.com
password_google = "" # password google

def get_smtp_mail(file: str) -> None:
    global SMTP_PORT, SMTP_SERVER, mailbox, password_google
    """
    Function for getting informations of the json content for
    smtp server
    smtp port
    password
    email"""
    fileContent = open(file, "r")
    jsonContent = fileContent.read()
    obj_python = json.loads(jsonContent)
    SMTP_SERVER = obj_python["SMTP_SERVER"]
    SMTP_PORT = obj_python["SMTP_PORT"]
    mailbox = obj_python["Mailbox"]
    password_google = obj_python["Password"]
    timer = obj_python["Timer"]

get_smtp_mail("data_smtp_mail.json")


banner = """
███████╗███╗   ███╗ █████╗ ██╗██╗         ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                        by cmedhrouville
""" # banner representating the software

def send_email(object: str, file_mail: str, mail_adress: str, sender_mail: list) -> True or False:
    """
    Fonction qui permet d'envoyer un mail a une adresse mail
    PARAMETERS:
        - object : Object of the mail -> Object of the Mail
        ###- title : Title of the mail -> Title of the mail
        - file_mail : the html for the mail -> main.html
        - mail_adress : mail adress to send the mail -> salut@gmail.com
        - sender_mail : sender's mail and password -> ["test@gmail.com", "123Password"]
        """
    message = MIMEMultipart("alternative") # we create an email
    message["Subject"] = object # we add the object of the mail
    message["From"] = sender_mail[0] # we keep the sender mail
    message["To"] = mail_adress # we create the target of the mail
    with open(file_mail, 'r') as f: # we read the HTML file and assign to a variable
        file_html = f.read()
    message.attach(MIMEText(file_html, 'html')) # The body and the attachments for the mail
    context = ssl.create_default_context() # we create context
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls() #enable security
    session.ehlo()  
    session.login(sender_mail[0], sender_mail[1])
    text = message.as_string()
    session.sendmail(sender_mail[0], mail_adress, text)
    session.quit()
    return True
    

    

def clear_cmd() -> None:
    """
    Function to clean the cmd after write in it"""
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    run = True # setup the loop
    while run: # creating the loop
        clear_cmd() # clear the command line
        print(banner) # print the banner of the software
        choice = input("1) Send Emails \n2) Informations \n3) Quit \n>>> ") # ask what to do
        if choice == "1": # if the choice is to send emails
            # creating another loop
            run2 = True
            while run2:
                clear_cmd()
                print(banner) # print the banner of the software
                object = input("[-] The Object of the Mail or (Q)uit\n>>> ")
                if object != "":
                    run3 = True
                    while run3:
                        clear_cmd()
                        print(banner)
                        try:
                            file_html = input("[-] The HTML File to Send (ONLY HTML) or (Q)uit \n>>> ")
                            f = open(file_html, "r")
                            a = f.read()
                            f.close()
                            if a == "":
                                file_html=""
                                print("[x] Error the html file is empty")
                                input("Press Enter to Continue ...")
                        except:
                            file_html=""
                            print(f"[x] There is an error with the HTML File.")
                            input("Press Enter to Continue ...")
                        if file_html != "" and file_html[len(file_html)-5:] == ".html": # si le fichier est html
                            run4 = True
                            while run4 :
                                clear_cmd()
                                print(banner)
                                try:
                                    file_mail_target = input("[-] The File With the Mailboxes targets (ONLY TXT) or (Q)uit\n>>> ")
                                    f = open(file_mail_target)
                                    a = f.read()
                                    f.close()
                                    if a == "":
                                        file_mail_target = ""
                                        print("[x] Something gone wrong with the txt file. It is empty.")
                                        input("Press Enter to Continue ...")
                                except:
                                    file_mail_target=""
                                    print("[x] Something gone wrong with the text file. ")
                                    input("Press Enter to Continue ...")
                                    
                                if file_mail_target != "" and file_mail_target[len(file_mail_target)-4:] == ".txt": # si le fichier est txt
                                    clear_cmd()
                                    print(banner)
                                    run5 = True
                                    while run5:
                                        print("Working ...")
                                        mails = get_targets_emails(file_mail_target)
                                        for index, email in enumerate(mails):
                                            try:
                                                send_email(object, file_html, email, [mailbox, password_google])
                                                print(f"Successful {index+1} mail sended - {email}")
                                                if index == len(mails)-1:
                                                    pass
                                                else:
                                                    time.sleep(timer)
                                            except:
                                                print(f"Error Detected - '{email}'")
                                                input("Mail Doesn't Work or SMTP Server or SMTP Port or Your mail or password is incorrect")
                                        
                                        run5 = False
                                        run4 = False
                                        run3 = False
                                        run2 = False


                                elif file_mail_target in ["Q", "q"]:
                                    run4 = False
                        elif file_html in ["Q", "q"]:
                            run3 = False
                elif object in ["Q", "q"]:
                    run2 = False
            

        
        elif choice == "2": # if the choice is to get informations
            clear_cmd() # clear the cmd
            print(banner)# print the banner of the software
            input("[-] To get information on the program, there are : \n - texts files \n - screenshots \nto explain the use in the file README. \nThank you for using l'Email Sender by cmedhrouville \n Press Enter ...")
        elif choice == "3": # if the choice is to quit the software
            clear_cmd() # clear the cmd
            print(banner)# print the banner of the software
            input("[Q] Thank you for using l'Email Sender by cmedhrouville. Have a nice day. [Enter to QUIT] ... ") # message of congrats
            run = False  # stop the loop
        else:
            print("[x] Error, you have entered an unavailable number") # error message
