#! /usr/bin/env python3
# coding: utf-8
import re

from pbapp.constant import STOPWORDS


class Parser:
    def __init__(self, message):
        self.message = message
        self.findall = []
        self.lower = []
        self.r_ponct_blank = []
        self.r_st_words = []

    def split_message_with_ponc(self):
        self.findall = re.findall(r'^|\w+', self.message)

        return self.findall

    def lowercase_message(self):
        for w in self.findall:
            self.lower.append(w.lower())

        return self.lower

    def remove_punct_blank(self):
        for w in self.lower:
            w = re.sub(r"\W", "", w)
            self.r_ponct_blank.append(w)

        return self.r_ponct_blank

    def remove_stop_words(self):
        for w in self.lower:
            if w not in STOPWORDS:
                self.r_st_words.append(w)

        return self.r_st_words
