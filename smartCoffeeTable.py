import imaplib
import email
import pywapi
import httplib2
import os
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import datetime
import feedparser

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
#print "Your most recent emails:" + '\n'

emailNum = 5
zipcode = '03755'
def getMail(emailNum):

    mailMatrix = [[0 for x in range(5)] for x in range(emailNum)]

    for x in range(-1, (emailNum-1)):  # will expand range later - second number = number of emails to display minus 1
        result, data = mail.uid('search', None, "ALL")  # search and return uids instead
        latest_email_uid = data[0].split()[x]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)

        mailMatrix[x][0] = email_message['Date']
        mailMatrix[x][1] = 'To: ' + email_message['To']
        mailMatrix[x][2] = 'From: ' + email_message['From']
        mailMatrix[x][3] = email_message['Subject']
        body = ""
        for part in email_message.walk():
        # each part is a either non-multipart, or another multipart message
        # that contains further parts... Message is organized like a tree
            if part.get_content_type() == 'text/plain':
                body = body + part.get_payload()  # prints the raw text

        mailMatrix[x][4] = body
        #print email_message.items()  # print all headers

    return mailMatrix

def convertToF(celcius):
    return str(((int(celcius)*9)/5) + 32)

# first entry is weather description, second is high temp
def getWeather(zipcode):
    # pp = pprint.PrettyPrinter(indent=4)
    weatherMatrix = [[0 for x in range(2)] for x in range(2)]
    weather_com_result = pywapi.get_weather_from_weather_com(zipcode)
    weatherMatrix[0][0] = weather_com_result['current_conditions']['text']
    weatherMatrix[0][1] = convertToF((weather_com_result['forecasts'][0]['high']))
    weatherMatrix[1][0] = weather_com_result['forecasts'][1]['day']['text']
    weatherMatrix[1][1] = convertToF((weather_com_result['forecasts'][1]['high']))
    return weatherMatrix

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

eventNum = 5
# first entry is time, second is event title
def getCalendar(eventNum):

    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """

    calMatrix = [[0 for x in range(2)] for x in range(eventNum)]
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
   # print 'Upcoming events:'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    track = 0
    if (not events):
        calMatrix[track][0] = "No Upcoming events found."
        calMatrix[track][1] = "Get Planning!"
        #print 'No upcoming events found.'
    else:

        for event in events:

            start = event['start'].get('dateTime', event['start'].get('date'))
            calMatrix[track][0] = start
            calMatrix[track][1] = event['summary']
            track += 1
        
    return calMatrix

newsNum = 5
# first entry is title, second is author(s)
def getNews(newsNum):

    newsMatrix = [[0 for x in range(2)] for x in range(newsNum)]
    d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/World.xml')
    for x in range(0, newsNum):
        newsMatrix[x][0] = d.entries[x].title
        newsMatrix[x][1] = d.entries[x].author

    return newsMatrix
        
