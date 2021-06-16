import snowballstemmer
import tamil

from FrontEnd import tamilutils, gazetteers, grammaticalrules
from FrontEnd.crf_impl import checkcluewordlist

def findinflectionsuffix(word):
    letters = tamil.utf8.get_letters(word)
    lastletter = letters[-1]
    secondlastletter = letters[-2]
    lastletterunicode = tamilutils.getUnicodePoints(lastletter)

    if lastletter == u"கு":
        return u"கு"
    elif lastletter == u"ன்":
        tuple = tamilutils.getUnicodePoints(secondlastletter)
        if tuple[1] == u"இ":
            return u"இன்"
    elif lastletter == u"ல்":
        tuple = tamilutils.getUnicodePoints(secondlastletter)
        if tuple[1] == u"ஆ":
            return u"ஆல்"
        elif tuple[1] == u"இ":
            return u"இல்"
    elif lastletter == u"து":
        tuple = tamilutils.getUnicodePoints(secondlastletter)
        if tuple[1] == u"அ":
            return u"அது"
    elif lastletterunicode[1] == u"ஐ":
        return u"ஐ"
    return 'None'

def generatequestion(sentence, word, prevword, nextword, namedentitytype):
    listofwords = word.split()
    lastentityword = listofwords[-1]
    inflectionsuffix = findinflectionsuffix(lastentityword)
    if prevword != '' and searchcluewordlist(prevword, namedentitytype) != 'None':
        question = sentence.replace(prevword + "\s" + word, grammaticalrules.rules[namedentitytype][inflectionsuffix])
        return question
    if nextword != '' and searchcluewordlist(nextword, namedentitytype) != 'None':
        question = sentence.replace(nextword + "\s" + nextword, grammaticalrules.rules[namedentitytype][inflectionsuffix])
        return question
    question = sentence.replace(word, grammaticalrules.rules[namedentitytype][inflectionsuffix])
    return question

def searchcluewordlist(word, key):
    stemmer = snowballstemmer.stemmer('tamil')
    stemword = stemmer.stemWords(word.split())
    if word in gazetteers.cluewords.get(key):
        return word
    if stemword[0] in gazetteers.cluewords.get(key):
        return stemword
    return 'None'

