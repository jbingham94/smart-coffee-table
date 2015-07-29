import imaplib
import email
import pywapi
import pprint
import string

# email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('smartcoffee6@gmail.com', 'iluvcs69yo')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox")  # connect to inbox.
print "Your most recent emails:" + '\n'

for x in range(-1, 1):  # will expand range later - second number = number of emails to display minus 1
    result, data = mail.uid('search', None, "ALL")  # search and return uids instead
    latest_email_uid = data[0].split()[x]
    result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_string(raw_email)

    print("Time:"),
    print email_message['Date']
    print("To:"),
    print email_message['To']
    print("From:"),
    print email_message['From']
    print("Subject:"),
    print email_message['Subject']
    print "Body:"
    for part in email_message.walk():
    # each part is a either non-multipart, or another multipart message
    # that contains further parts... Message is organized like a tree
        if part.get_content_type() == 'text/plain':
            print part.get_payload()  # prints the raw text

    #print email_message.items()  # print all headers

# weather
pp = pprint.PrettyPrinter(indent=4)

weather_com_result = pywapi.get_weather_from_weather_com('03755')

print "According to weather.com, it is currently " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C.\n"
