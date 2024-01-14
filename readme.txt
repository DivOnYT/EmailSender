Readme for Email Sender by cmedhrouville:
first of all, you have to fill in several files:
 - in data emails.txt the emails to send the message to
 - and in mail_to_send.html, the html page that will be displayed as the email

Then you have to open the program main.py or the .exe that will be generated.
You have to enter the names of the files in the programs:
Examples :
  [-] The HTML File to Send (ONLY HTML) or (Q)uit
  >>> data/mail_to_send.html


  [-] The File With the Mailboxes targets (ONLY TXT) or (Q)uit
  >>> data/emails.txt

Then the program will send mails to all the people in the emails.txt file then return to the main menu

Program made by cmedhrouville : https://www.fiverr.com/cmedhrouville

For change mail adress and password : go in data_smtp_mail.json

More Explainations about SMTP Servers : https://www.ionos.com/digitalguide/e-mail/technical-matters/smtp-server/

In data_smtp_mail.json :
 - Mailbox -> the mailbox who send mails
 - Password -> Password for the mailbox
 - smtp_server -> website's smtp_server
 - smtp_port -> smtp's port to connect to smtp server
 - timer -> time between two mails in seconds


ALL THE FILES ARE DEPENDENCIES : The sofwtare will not run if you delete them
Exceptions :
 - data/emails.txt -> can be change to another file, you only have to entry the path of the file in the software
 - data/mail_to_send.html -> can be change to another file, you only have to entry the path of the file in the software
