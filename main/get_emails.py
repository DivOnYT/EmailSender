
def get_targets_emails(file: str) -> list:
    """
    Function that retrieves all emails put in a text file and converts them into a list
            **Emails.txt**
            salut1983@gmail.com
            coucou124@nul.com
            etc@gmail.com
    The email text file in this form

    RETURN -> List
    ["salut1983@gmail.com", "coucou124@nul.com", "etc@gmail.com"]
    """
    f = open(file, "r", encoding="Utf-8") # we open the text file
    reading = f.read() # we read the entire text file
    read = reading.split("\n")  # we split the mails by all the <enter>
    f.close() # we close the file to liberate memory
    return read # return the list of emails

'''
Not serving 
def get_senders_email(file: str):
    """
    Function that retrieves all emails of senders put in a CSV file and return them
    Example : 
                **test.csv**
                email;Password
                salut@coucou.com;1234Password
                chien@laposte.net;12salut
    """
    f = pd.read_csv(file) # we read the data of the CSV file
    return f # we return it to use forward'''
