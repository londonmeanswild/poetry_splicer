#!/usr/local/bin/python3
# A text-generating Oracle.
# (c) 2017 by Landon A Marchant

"""Removes all numeric and special characters from a text file."""
import re
"""
def cleanfile():
    searched_file = input("File to modify: ")
    output_file = input("save file as ")
    with open(r(input(searched_file), 'r')) as infile, open (r(input(output_file), 'r')) as outfile:
        text = infile.read()
        text = re.sub(r'\d+', '')
        outfile.write(data)
    return outfile"""

text = open('headlines2_15').read()
new_text = re.sub('[^\w\d-]', ' ', text)
new_text = new_text.replace("NEWS", "RELATED COVERAGE",  ".", "\n")

# need to change all instances of integer +m or integer+h to words at some point
#new_text = new_text.replace(")", "")"""

open('headlines2_15', 'w').write(new_text)