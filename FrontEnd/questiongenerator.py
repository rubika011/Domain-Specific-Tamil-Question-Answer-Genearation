import snowballstemmer
import tamil

from FrontEnd import tamilutils, gazetteers, grammaticalrules
from FrontEnd.crf_model_prediction import predictnertag


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

def nerquestiongeneration(sentences):
    namedentitiespredicted = predictnertag(sentences)
    namedentitytagtypes = ['COU', 'CITY', 'CON', 'PER', 'KIN', 'ORG', 'EVE', 'TRO']
    i = 0
    for sentence in sentences:
        predictednamedentitytags = namedentitiespredicted[i]
        print(sentence)
        print(namedentitiespredicted[i])
        for namedentitytag in namedentitytagtypes:
            processquestionword(sentence, predictednamedentitytags, namedentitytag)
        i = i + 1

def processquestionword(sentence, predictednamedentitytags, namedentitytag):
    btag = "B-" + namedentitytag
    itag = "I-" + namedentitytag

    startindex = returnindexoflist(predictednamedentitytags, btag)
    endindex = startindex

    if startindex > 0:
        while 0 < endindex < len(predictednamedentitytags) - 1:
            endindex = endindex + 1
            if predictednamedentitytags[endindex] != itag:
                break
        words = sentence.split()
        namedentity = ''.join(words[startindex: endindex])
        prevword = ''.join(words[startindex-1])
        nextword = ''.join(words[endindex])

        generatequestion(sentence, namedentity, prevword, nextword, namedentitytag)


def returnindexoflist(list, item):
    try:
        return list.index(item)
    except ValueError:
        return -1
