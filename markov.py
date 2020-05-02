#!/usr/local/bin/python3
# Markov
# (c) 2017 by Landon A Marchant

import markovify

def mark():
    with open("CHANTS_DEMOCRATIC.txt") as f:
        text = f.read()

    text_model = markovify.Text(text)

    for i in range(5):
        print(text_model.make_short_sentence(140))

mark()
