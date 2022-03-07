import re
import string
import nltk
import pandas as pd
import numpy as np
from luhn import (sumarize_by_luhn, variables)
from  common import (simple_clear, stop_word, wiegth_sentency, normalize_text, frenquency, frequency_in_text, init)

init()

def resume(sentency, list_):
    
    '''
    resume a text starting of the dictonary with grades and index of the sentences
    :param sentency: dict -> sentences and weight
    :param list_weight:list -> list of the index of the sent 
    :return string  " ".join(sent):
    
    '''
    sent = [sentency[index] for index in list_]
    return " ".join(sent)

def sumarize_per_frequency(text, n = 10, order = False, lemma = False):
    
    harmonized_words = normalize_text(text, lemma)
    harmonized_text = " ".join(harmonized_words)
    
    frenquencia = frenquency(harmonized_words, harmonized_text)
    max_frenquency = max(frenquencia.values())
    wiegth = { word : note/max_frenquency for word, note in frenquencia.items()}
    sentenc_text = nltk.sent_tokenize(simple_clear(text), language = "Portuguese")
        
    wiegth_sent = [[index , wiegth_sentency(sentenc_text[index], wiegth)] for index in range(len(sentenc_text))]
    ordenate = sorted(wiegth_sent, key = lambda x: x[1] , reverse = True)
    
    ordenate_rank = [index[0] for index in ordenate]
    if order:
        ordenate_rank = sorted(ordenate_rank[:n])

    return resume(sentenc_text, ordenate_rank[:n])

