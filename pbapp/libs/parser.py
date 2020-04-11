#! /usr/bin/env python3
# coding: utf-8
import re
import string
from pbapp.constant import STOPWORDS


class Parser:
    def __init__(self, message):
        self.message = message
        self.split = []
        self.lower = []
        self.r_ponct_blank = []
        self.r_st_words = []

    def split_message_with_ponc(self):
        a = self.message.replace("'", " ")
        t = a.replace("-", " ")
        self.split = t.split()

        return self.split

    def lowercase_message(self):
        for w in self.split:
            self.lower.append(w.lower())

        return self.lower

    def remove_punct_blank(self):
        for w in self.lower:
            f = re.sub(r"\W+", "", w)
            self.r_ponct_blank.append(f)

        return self.r_ponct_blank

    def remove_stop_words(self):
        for w in self.r_ponct_blank:
            if w not in STOPWORDS:
                self.r_st_words.append(w)

        return " ".join(self.r_st_words)
