# -*- coding: utf-8 -*-
from rasa_sdk import Action
import datetime
import random 
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, FollowupAction, ActionReverted, UserUttered, ActionExecuted
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
import re
import time
import requests
import json
from rasa_sdk.events import SlotSet
import ast
import random

class ActionDefaultFallback(Action):


    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        poeme_deja_affiche = tracker.get_slot('liste_poeme_ecrit').split(" ")
        poeme_trouve = False
        cur_poeme = ""
        list_poeme_deja_affiche = ""
        if (len(poeme_deja_affiche) <11):
            while poeme_trouve != True:
                poeme_au_hasard = str(random.randrange(1,11))
                if poeme_au_hasard not in poeme_deja_affiche:
                    poeme_trouve = True
                    cur_poeme = "utter_poeme"+poeme_au_hasard
                    list_poeme_deja_affiche = str(' '.join(poeme_deja_affiche) + " "+ poeme_au_hasard)
                    #dispatcher.utter_message(cur_poeme)
                    #dispatcher.utter_message(list_poeme_deja_affiche)
                    dispatcher.utter_message(template = cur_poeme)
        else:
            dispatcher.utter_message("Je t'ai affiché tous les poèmes que j'ai selectionnés mais même un nombre infini ne suffirait à t'exprimer mes sentiments aussi complexe et fort que j'ai pour toi.")
        #return [FollowupAction("ecriture_tracker"), SlotSet("poeme_courant", cur_poeme),SlotSet("liste_poeme_ecrit", list_poeme_deja_affiche)]
        return [SlotSet("poeme_courant", cur_poeme),SlotSet("liste_poeme_ecrit", list_poeme_deja_affiche)]
