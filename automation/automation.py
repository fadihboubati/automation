import re

def get_text (file_path):
    with open(file_path) as f:
        text = f.read()
        return text

def extract_emails( text ):
    mail_pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+'
    all_mails_in_text =  re.findall( mail_pattern, text )
    emails = []
    for mail in all_mails_in_text:
        if mail not in emails:
            emails.append(mail)
    emails.sort()

    with open('emails.txt', 'w+') as f:
        index = 1
        for i in emails:
            f.write( 'email number ' + str(index) + ':\t\t' + i + '\n')
            index += 1
    return
      
def extract_phone_number(text):
    #phone_number_pattern = r'((\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?.?))((\d{3}(\s|-?.?))|(\d{2}(\s|-?)))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?)'
    #phone_number_pattern = r'(((\(\d{3}\)\s?)|(\d{3})(\s|-?.?))?(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?.?))((\d{3}(\s|-?.?))|(\d{2}(\s|-?)))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?)'
    phone_number_pattern = r'(((\(\d{3}\)\s?)|(\+\d{1})(\s|-?.?))?((\(\d{3}\)\s?)|(\d{3})(\s|-?.?))?(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?.?))((\d{3}(\s|-?.?))|(\d{2}(\s|-?)))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?)'
    all_numbers_in_text = re.findall(phone_number_pattern, text)
    phone_numbers = []
    for number in all_numbers_in_text:
        if number[0] not in phone_numbers:
            phone_numbers.append(number[0])
    phone_numbers.sort()
    with open('phone_numbers.txt', 'w+') as f:
        index = 1
        for i in phone_numbers:
            f.write( 'phone number ' + str(index) + ':\t\t' + i + '\n')
            index += 1
    return


    

if __name__ == "__main__":
    file_path = 'automation/assets/potential-contacts.txt'
    text = get_text(file_path)
    extract_emails(text)
    extract_phone_number(text)

