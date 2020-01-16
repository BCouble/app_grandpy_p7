#! /usr/bin/env python3
# coding: utf-8
import re

from pbapp.constant import STOPWORDS


class Parser:
    def __init__(self, message):
        self.message = message
        self.spl_message = []
        self.low_message = []
        self.r_p_blank = []
        self.r_st_words = []

    def split_message(self):

        self.spl_message = self.message.split()

    def lowercase_message(self):

        self.low_message = self.message.lower()

    def remove_punct_blank(self):

        self.r_p_blank = re.sub(r"\W", " ", self.message)

    def remove_stop_words(self):
        quest_api = []
        for w in self.message:
            if w not in STOPWORDS:
                quest_api.append(w)

        quest_api = "-".join(self.r_st_words)
        self.r_st_words = quest_api
