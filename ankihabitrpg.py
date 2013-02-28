user_id = "Your HabitRPG user id here"
api_token = "Your HabitRPG api token here"

#############################################################################
import urllib2, urllib
from anki.hooks import wrap
from aqt.reviewer import Reviewer

url = 'https://habitrpg.com/v1/users/' + user_id + '/tasks/anki/up'

def habitTaskComplete(self, ease):
    if ease > 1:
        urllib2.Request(url)
        urllib2.urlopen(urllib2.Request(url), urllib.urlencode({"apiToken":api_token, "title":"Anki"}))

Reviewer._answerCard = wrap(Reviewer._answerCard, habitTaskComplete)
