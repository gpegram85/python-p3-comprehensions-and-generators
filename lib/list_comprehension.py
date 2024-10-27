#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list) <= 0:
        return []
    
    evens_list = [n for n in num_list if n % 2 == 0]
    return evens_list


def make_exclamation(sentence_list):
    if len(sentence_list) <= 0:
        return []
    
    excited_list = [s + "!" for s in sentence_list]
    return excited_list