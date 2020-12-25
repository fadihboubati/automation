import re

def get_text (file_path):
    with open(file_path) as f:
        text = f.read()
        return text

def extractEmails( text ):
    all_mails_in_text =  re.findall(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+' ,text )
    emails = []
    for mail in all_mails_in_text:
        if mail not in emails:
            emails.append(mail)

    with open('emails.txt', 'w+') as f:
        index = 1
        for i in emails:
            f.write( 'email number ' + str(index) + ':\t\t' + i + '\n')
            index += 1
    return
      




    

if __name__ == "__main__":
    file_path = 'automation/assets/potential-contacts.txt'
    text = get_text(file_path)
    extractEmails(text)

