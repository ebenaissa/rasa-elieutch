# -*- coding: utf-8 -*-
from rasa_sdk import Action
import datetime
import random 
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, FollowupAction, ActionReverted, UserUttered
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
import re
import time
import requests
import json
from rasa_sdk.events import SlotSet
import ast 
import logging

logger = logging.getLogger(__name__)


class ActionEcriture(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "ecriture_tracker"

    def run(self, dispatcher, tracker, domain):
        from datetime import datetime
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        
        string = []
        user = tracker.latest_message['text']
        tracker_all = tracker.current_state()['events']
        events = tracker.current_state()['events'][-15:]
        user_events = [[str(event_['parse_data']['intent']['name']), str(float(event_['parse_data']['intent']['confidence']))] for event_ in events if event_['event'] =='user']
        
        if len(tracker_all) < 15:
            if len(user_events) == 1:
                string.append(["_____ Nouvelle conversation : "])

        #prediction = tracker.latest_message['intent'].get('name')

        prediction = user_events[-1][0] + " ("+user_events[-1][1]+")"
        string.append(["user",user,str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))])
        string.append(["bot",prediction,str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")), str(tracker.get_slot('liste_poeme_ecrit'))])
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds_googlesheet.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open('Logs').sheet1
        for elt in string:
            try:
                sheet.insert_row(elt, len(sheet.get_all_values())+1)
            except:
                logger.info("Interaction non injecte "+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

        #import io
        #fichier = io.open("conv.txt", mode="a", encoding="utf-8")
        #fichier.write(string)
        #fichier.close()
            

        return []
            
