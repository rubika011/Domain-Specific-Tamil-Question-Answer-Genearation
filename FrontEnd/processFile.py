from rippletagger.tagger import Tagger
from indicnlp.tokenize import sentence_tokenize
from FrontEnd import gazetteers
import rulebased
import snowballstemmer
import re

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

def lookup_search(lookup):
    for key, value in gazetteers.dictionary.items():
        for v in value:
            partnames = v.split(" ")
            if lookup in partnames:
                return key
    return 'None'

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

    for sentence in sentences:
        sentence = ' '.join(sentence.split())
        sentence = re.sub('\u200c', '', sentence)
        issentencesuitable = ignorenonsuitablesentence(sentence)
        if not issentencesuitable:
            continue

        tagger = Tagger(language='tam')
        postagger = tagger.tag(sentence)
        print(sentence)
        print('POS tag', postagger)

        matchFound = rulebased.regex_match_date_time_quantity(sentence, writefile, postagger)
        if matchFound:
            continue

        matchFound = rulebased.regex_match_multiple_items(sentence, writefile)
        if matchFound:
            continue

        for (word, tag) in postagger:
            if (tag == 'NOUN' or tag == 'PROPN') and word not in stopwords:
                matchFound = lookup_search(word)
                if matchFound == 'location':
                    question = sentence.replace(word, "எந்த நாடு")
                    rulebased.writeqafile(writefile, question, word)
                    break
                elif matchFound == 'person':
                    question = sentence.replace(word, "யார்")
                    rulebased.writeqafile(writefile, question, word)
                    break

