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

emailNum = 5
zipcode = '03755'
def getMail(emailNum):

    Matrix = [[0 for x in range(5)] for x in range(emailNum)]

    for x in range(-1, (emailNum-1)):  # will expand range later - second number = number of emails to display minus 1
        result, data = mail.uid('search', None, "ALL")  # search and return uids instead
        latest_email_uid = data[0].split()[x]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)

        Matrix[x][0] = email_message['Date']
        Matrix[x][1] = email_message['To']
        Matrix[x][2] = email_message['From']
        Matrix[x][3] = email_message['Subject']
        body = ""
        for part in email_message.walk():
        # each part is a either non-multipart, or another multipart message
        # that contains further parts... Message is organized like a tree
            if part.get_content_type() == 'text/plain':
                body = body + part.get_payload()  # prints the raw text

        Matrix[x][4] = body
        #print email_message.items()  # print all headers

    x = emailNum - 1
    while x > -1:
        for y in range(0, 5):
            print Matrix[x][y]
        x -= 1

getMail(emailNum)

def getWeather(zipcode):
    pp = pprint.PrettyPrinter(indent=4)

    weather_com_result = pywapi.get_weather_from_weather_com(zipcode)

    print "According to weather.com, it is currently " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C.\n"

getWeather(zipcode)
