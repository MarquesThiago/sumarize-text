import re
import string
import nltk
import pandas as pd
import numpy as np
import spacy

def init():
    nltk.download("punkt")

stpwrds = "a, agora, ainda, alguém, algum, alguma, algumas, alguns, ampla, amplas, amplo, amplos, ante, antes, ao, aos, após, aquela, aquelas, aquele, aqueles, aquilo, as, até, através, cada, coisa, coisas, com, como, contra, contudo, da, daquele, daqueles, das, de, dela, delas, dele, deles, depois, dessa, dessas, desse, desses, desta, destas, deste, deste, destes, deve, devem, devendo, dever, deverá, deverão, deveria, deveriam, devia, deviam, disse, disso, disto, dito, diz, dizem, do, dos, e, é, ela, elas, ele, eles, em, enquanto, entre, era, essa, essas, esse, esses, esta, está, estamos, estão, estas, estava, estavam, estávamos, este, estes, estou, eu, fazendo, fazer, feita, feitas, feito, feitos, foi, for, foram, fosse, fossem, grande, grandes, há, isso, isto, já, la, lá, lhe, lhes, lo, mas, me, mesma, mesmas, mesmo, mesmos, meu, meus, minha, minhas, muita, muitas, muito, muitos, na, não, nas, nem, nenhum, nessa, nessas, nesta, nestas, ninguém, no, nos, nós, nossa, nossas, nosso, nossos, num, numa, nunca, o, os, ou, outra, outras, outro, outros, para, pela, pelas, pelo, pelos, pequena, pequenas, pequeno, pequenos, per, perante, pode, pude, podendo, poder, poderia, poderiam, podia, podiam, pois, por, porém, porque, posso, pouca, poucas, pouco, poucos, primeiro, primeiros, própria, próprias, próprio, próprios, quais, qual, quando, quanto, quantos, que, quem, são, se, seja, sejam, sem, sempre, sendo, será, serão, seu, seus, si, sido, só, sob, sobre, sua, suas, talvez, também, tampouco, te, tem, tendo, tenha, ter, teu, teus, ti, tido, tinha, tinham, toda, todas, todavia, todo, todos, tu, tua, tuas, tudo, última, últimas, último, últimos, um, uma, umas, uns, vendo, ver, vez, vindo, vir, vos, vós"
stop_word = [n.strip() for n  in stpwrds.split(',')] 

def simple_clear(text):
    
    ''' 
    simples clear, elimined space and break lines 
    :param text: str text
    return: str re.sub(r'\s+'," ", text.lower())
    '''
    
    return re.sub(r'\s+'," ", text.lower())

def normalize_text(text, lemma = False):
    
    ''' 
    harmonizetion of text,separede text in words, 
    remove space, simbols and stop word (words not contribuinls to meaning) 
    :param text: str text
    return: list text_harmonization: list fo words harmonizeds 
    '''

    if lemma:
        pln = spacy.load("pt_core_news_sm")
        tokens = [token.lemma_ for token in pln(text) 
                  if str(token) not in stop_word 
                  and str(token) not in string.punctuation 
                  and not str(token).isdigit()]
    else:
        tokens = nltk.word_tokenize(text.lower(), language="Portuguese")
    
    text_harmonization = [word for word  in tokens if word not in stop_word and word not in string.punctuation and not word.isdigit()]  
    return text_harmonization

def frequency_in_text(word, text):
    
    '''
    search word in text and return number of times it appears in the text
    :param word: string -> word search in text
    :páram text: string -> text 
    :return int len(re.findall(word, text)):
    '''
    try: 
        return len(re.findall(word, text))
    except:
        return 1

def frenquency(list_words, text):
    
    '''
    search list if the words in text and return dictonary of word and frequncy on the text
    :param list_word: string -> list of the words search in text
    :páram text: string -> text 
    :return dict { word : frequency_in_text(word, text) for word in list_words}):
    '''
    
    return { word : frequency_in_text(word, text) for word in list_words}

def wiegth_sentency(sentency, wiegths):
    
    '''
    calculate a sumarize of the grades per words in sentence and return a value 
    :param sentency: str 
    :param wieghts: dict -> dictonary of the words with wiegths
    :return float sum([wiegths[word] for word in tokens if word in wiegths.keys()])?
    '''
    
    tokens = nltk.word_tokenize(sentency, language = "Portuguese")
    return sum([wiegths[word] for word in tokens if word in wiegths.keys()])