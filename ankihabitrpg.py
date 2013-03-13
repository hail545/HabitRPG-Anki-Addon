user_id = "Your HabitRPG user id here"
api_token = "Your HabitRPG api token here"

##########################################
import urllib2, urllib
from anki.hooks import wrap
from aqt.reviewer import Reviewer
from aqt.utils import showInfo
from anki.sync import Syncer

def card_answered(self, ease):
    #Cache number of correct answers
    if ease > 1:
        Syncer.correct_answers += 1
        #showInfo(str(Syncer.correct_answers))#For debugging

def habit_sync(x):
    #Call API once for every correct answer during Ankiweb sync
    while Syncer.correct_answers > 0:
        urllib2.urlopen(url,urllib.urlencode(headers))
        Syncer.correct_answers -= 1
       #showInfo("Called API. " + str(Syncer.correct_answers) + " Times remaining" )#For debugging

Syncer.correct_answers = 0
url = 'https://habitrpg.com/v1/users/' + user_id + '/tasks/Anki/up'
headers = {"apiToken":api_token,"title":"Anki"}

#Wrap funtions to Anki
Reviewer._answerCard = wrap(Reviewer._answerCard, card_answered)
Syncer.sync = wrap(Syncer.sync, habit_sync)
