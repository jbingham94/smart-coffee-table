import imaplib
import email
import pywapi
import pprint
import string
import httplib2
import os
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

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
        Matrix[x][1] = 'To: ' + email_message['To']
        Matrix[x][2] = 'From: ' + email_message['From']
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

def convertToF(celcius):
    return str(((int(celcius)*9)/5) + 32)

def getWeather(zipcode):
    pp = pprint.PrettyPrinter(indent=4)

    weather_com_result = pywapi.get_weather_from_weather_com(zipcode)

    print "Weather Report:"
    print "Currently: " + weather_com_result['current_conditions']['text'] + " and " + convertToF(weather_com_result['current_conditions']['temperature']) + "F.\n"
    print "Today's high will be " + convertToF((weather_com_result['forecasts'][0]['high'])) + "F.\n"
    print "Tomorrow's forecast: " + weather_com_result['forecasts'][1]['day']['text'] + ", high " + convertToF((weather_com_result['forecasts'][1]['high'])) + "F.\n"
getWeather(zipcode)

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials


def getCalendar():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print 'Upcoming events:'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print start, event['summary']

getCalendar()
