from indicnlp.tokenize import sentence_tokenize
from FrontEnd import gazetteers
import rulebased
import snowballstemmer
import re

from FrontEnd.crf_model_prediction import predictnertag

ignorewordlistfile = open("ignoresentence.txt", encoding="utf-8")
ignorewordlist = ignorewordlistfile.read().splitlines()

def getlistofsentences(file_content):
    sentences = []
    while file_content != "":
        sentenceregex = re.compile('^[^.]+([0-9]+\.{0,1}\s*){0,}[^.]+[^\s.]{2,}\.')
        match = re.search(sentenceregex, file_content)
        sentences.append(match.string)
        if match:
            file_content = re.sub(sentenceregex, '', file_content)

    return sentences

def checkanophoricresolution(sentence, firstword, stemword):
    personrefs = ['அவர்', 'அவருக்கு', 'அவரை', 'அவரின்', 'அவரது', 'அவரால்', 'இவர்', 'இவரை', 'இவரது', 'இவரின்',
                  'இவருக்கு', 'அவரால்']
    locationrefs = ['அங்கே', 'இங்கே', 'அங்கு', 'இங்கு']

    return True

def ignorenonsuitablesentence(sentence):
    firstword = sentence.partition(' ')[0]
    if firstword in ignorewordlist:
        return False
    stemmer = snowballstemmer.stemmer('tamil')
    stemWord = stemmer.stemWords(firstword.split())
    if stemWord and stemWord[0] in ignorewordlist:
        return False

    return checkanophoricresolution(sentence, firstword, stemWord)

def processfile(filecontent, filewritepath):
    stopwordsfile = open("stopwords.txt", encoding="utf-8")
    stopwords = stopwordsfile.read().splitlines()

    writefile = open(filewritepath, "w", encoding="utf-8")
    sentences = sentence_tokenize.sentence_split(filecontent, lang='tam')

    cleanedsentences = []
    for sentence in sentences:
        sentence = ' '.join(sentence.split())
        sentence = re.sub('\u200c', '', sentence)
        cleanedsentences.append(sentence)
        issentencesuitable = ignorenonsuitablesentence(sentence)
        if not issentencesuitable:
            continue

        matchFound = rulebased.regex_match_date_time_quantity(sentence, writefile)
        #if matchFound:
        #    continue

        matchFound = rulebased.regex_match_multiple_items(sentence, writefile)
        #if matchFound:
        #    continue

        rulebased.checkgazetteer(sentence, writefile)

    predictnertag(cleanedsentences)

