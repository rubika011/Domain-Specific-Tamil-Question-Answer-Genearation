import snowballstemmer
import tamil

from FrontEnd import tamilutils, gazetteers, grammaticalrules
from FrontEnd.crf_model_prediction import predictnertag
from FrontEnd.run import writeqafile


def findinflectionsuffix(word):
    letters = tamil.utf8.get_letters(word)
    if len(letters) > 1:
        lastletter = letters[-1]
        secondlastletter = letters[-2]
        lastletterunicode = tamilutils.getUnicodePoints(lastletter)
        thirdlastletter = letters[-3] if len(letters) > 2 else ''
        forthlastletter = letters[-4] if len(letters) > 3 else ''

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
        elif lastletter == u"ம்":
            tuple = tamilutils.getUnicodePoints(secondlastletter)
            if tuple[1] == u"உ":
                return u"உம்"
        elif lastletter == u"ன":
            tuple = tamilutils.getUnicodePoints(secondlastletter)
            if tuple[1] == u"ஆ":
                return u"ஆன"
        elif lastletterunicode[1] == u"ஐ":
            return u"ஐ"
        elif word.endswith(u"டைய"):
            if thirdlastletter != '':
                tuple = tamilutils.getUnicodePoints(thirdlastletter)
                if tuple[1] == u"உ":
                    return u"உடைய"
        elif word.endswith(u"டன்"):
            if thirdlastletter != '':
                tuple = tamilutils.getUnicodePoints(thirdlastletter)
                if tuple[1] == u"உ":
                    return u"உடன்"
        elif word.endswith(u"டன்"):
            if thirdlastletter != '':
                tuple = tamilutils.getUnicodePoints(thirdlastletter)
                if tuple[1] == u"உ":
                    return u"உடன்"
        elif word.endswith(u"கிய"):
            if thirdlastletter != '':
                tuple = tamilutils.getUnicodePoints(thirdlastletter)
                if tuple[1] == u"ஆ":
                    return u"ஆகிய"
        elif word.endswith(u"ருந்து"):
            if forthlastletter != '':
                tuple = tamilutils.getUnicodePoints(forthlastletter)
                if tuple[1] == u"இ":
                    return u"இருந்து"
        elif word.endswith('மீது'):
            return u"மீது"

        return 'None'
    return 'None'

def generatequestion(sentence, word, prevword, nextword, namedentitytype, writefile):
    listofwords = word.split()
    lastentityword = listofwords[-1]
    inflectionsuffix = findinflectionsuffix(lastentityword)
    if prevword != '' and searchcluewordlist(prevword, namedentitytype) != 'None':
        questionword = searchrules(namedentitytype, inflectionsuffix)
        question = sentence.replace(prevword + "\s" + word, questionword)
    elif nextword != '' and searchcluewordlist(nextword, namedentitytype) != 'None':
        nextwordinflectionsuffix = findinflectionsuffix(nextword)
        questionword = searchrules(namedentitytype, nextwordinflectionsuffix)
        question = sentence.replace(word + "\s" + nextword, questionword)
    else:
        questionword = searchrules(namedentitytype, inflectionsuffix)
        question = sentence.replace(word, questionword)

    if questionword != '':
        writeqafile(writefile, question, sentence)

def searchrules(namedentitytype, inflectionsuffix):
    try:
        return grammaticalrules.rules[namedentitytype][inflectionsuffix]
    except KeyError:
        return ''

def searchcluewordlist(word, key):
    stemmer = snowballstemmer.stemmer('tamil')
    stemword = stemmer.stemWords(word.split())
    if word in gazetteers.cluewords.get(key):
        return word
    if stemword[0] in gazetteers.cluewords.get(key):
        return stemword
    return 'None'

def nerquestiongeneration(sentences, writefile):
    namedentitiespredicted = predictnertag(sentences)
    namedentitytagtypes = ['COU', 'CITY', 'CON', 'PER', 'KIN', 'EVE', 'TRO']
    i = 0
    for sentence in sentences:
        predictednamedentitytags = namedentitiespredicted[i]
        print(sentence)
        print(namedentitiespredicted[i])
        for namedentitytag in namedentitytagtypes:
            processquestionword(sentence, predictednamedentitytags, namedentitytag, writefile)
        i = i + 1

def processquestionword(sentence, predictednamedentitytags, namedentitytag, writefile):
    btag = "B-" + namedentitytag
    itag = "I-" + namedentitytag

    startindex = returnindexoflist(predictednamedentitytags, btag)
    endindex = startindex

    if startindex >= 0:
        while 0 <= endindex < len(predictednamedentitytags) - 1:
            endindex = endindex + 1
            if predictednamedentitytags[endindex] != itag:
                break
        words = sentence.split()
        namedentity = ''.join(words[startindex: endindex])
        prevword = ''.join(words[startindex-1])
        nextword = ''.join(words[endindex])

        generatequestion(sentence, namedentity, prevword, nextword, namedentitytag, writefile)

def returnindexoflist(list, item):
    try:
        return list.index(item)
    except ValueError:
        return -1
