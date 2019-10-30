#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python
Innehåller metoder för att göra textanalyserna.
kakl19
2019-10-16
"""
from operator import itemgetter
import re

fname = "phil.txt"

def lines():
    """
    Counts the number of lines in a text.
    """
    text = []
    with open(fname) as filehandler:
        for line in filehandler:
            line = line.strip()
            if line:
                text.append(line)

        return {"lines" : len(text)}



def words_dict():
    """
    Counts the number of words_dict in a text.
    """
    with open(fname) as filehandle:
        text = filehandle.read().split()

    return {"words_dict" : len(text)}



def letters():
    """
    Counts the number of letters in a text.
    """
    with open(fname) as filehandle:
        text = filehandle.read()
        count = 0
        for letter in text:
            if letter.isalpha():
                count += 1

        return {"letters" : count}



def word_frequency():
    """
    Counts the frequency of words in a text.
    """
    words = dict()
    with open(fname) as filehandle:
        text = filehandle.read().split()
        total = len(text)

    for word in text:
        word = word.lower()
        word = re.sub(r'[^a-z]', "", word)
        words[word] = words.get(word, 0) + 1

    lst = sort_dic_and_return_list(words, total)

    return {"word_frequency" : lst}



def letter_frequency():
    """
    Counts the frequency of letters in a text.
    """
    letter_freq = dict()
    total = letters()
    with open(fname) as filehandle:
        text = filehandle.read()

    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

    lst = sort_dic_and_return_list(letter_freq, total["letters"])

    return {"letter_frequency" : lst}



def sort_dic_and_return_list(dic, total):
    """
    Takes a dictionary, sorts it by value. Creates a list of tuples and returns
    the 7 first items in the list.
    """
    lst = list()
    for key, value in sorted(dic.items(), key=itemgetter(1), reverse=True):
        freq = round(value / total * 100, 1)
        tup = (key, value, freq)
        lst.append((tup))

    lst = lst[:7]
    return lst


def all_analyzes():
    """
    Calla all of the methods.
    """
    all_dict = dict()

    all_dict.update(lines())
    all_dict.update(words_dict())
    all_dict.update(letters())
    all_dict.update(word_frequency())
    all_dict.update(letter_frequency())

    return all_dict



def change():
    """
    Changes the file.
    """
    new_name = input()

    if not ".txt" in new_name:
        new_name += ".txt"

    global fname
    fname = new_name



def pretty_print(result):
    """
    Prints the key and values of a dictionary.
    """
    for key in result:
        if isinstance(result[key], list):
            print(key + ": ")
            for value in result[key]:
                print("    {}: {} | {}%".format(value[0], value[1], value[2]))
        else:
            print(key + ": " + str(result[key]))
