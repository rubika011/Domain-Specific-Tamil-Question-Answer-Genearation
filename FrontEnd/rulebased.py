import re

from FrontEnd import gazetteers
from FrontEnd.questiongenerator import generatequestion
from FrontEnd.run import writeqafile

#regex match for எந்த, எவை question generation
def regex_match_multiple_items(sentence, writefile):
    multipleItemsRegex1 = re.compile('([^,\s]+,\s)+[^,]+(?:ஆகிய\s|போன்ற\s)')
    match = re.match(multipleItemsRegex1, sentence)
    if match:
        question = re.sub(multipleItemsRegex1, 'எந்த ', sentence)
        return writeqafile(writefile, question, match.string)
    else:
        multipleItemsRegex2 = re.compile('(.*,)+.*(?:ஆகியன\s|என்பன\s|போன்றன\s|போன்றவை\s|ஆகியவை\s|என்பவை\s)')
        match2 = re.match(multipleItemsRegex1, sentence)
        if match2:
            question = re.sub(multipleItemsRegex2, 'எவை ', sentence)
            return writeqafile(writefile, question, match.string)

#regex match for எப்போது, எத்தனை type of question generation
def regex_match_date_time_quantity(sentence, writefile):

    dateTimeRegex = re.compile('(வருடம்\s)*[1-2][0-9]{3}\s*(?:இல்\s|ல்\s)')
    match = re.search(dateTimeRegex, sentence)
    if match:
        question = re.sub(dateTimeRegex, 'எந்த வருடம் ', sentence)
        return writeqafile(writefile, question, match.string)
    else:
        dateTimeRegex2 = re.compile('[1-2][0-9]{3}(\s)*(ஆம்\s(?:வருடம்|ஆண்டு)\s){0,1}[^\s]+\s(மாதம்\s){0,1}[0-3][0-9](\s)*(?:ஆம்|ஆந்|இல்|ல்)(\s(?:திகதி|நாள்|தேதி)){0,1}')
        match2 = re.search(dateTimeRegex2, sentence)
        if match2:
            question = re.sub(dateTimeRegex2, 'எந்த ஆண்டு எந்த மாதம் எத்தனையாம் திகதி', sentence)
            return writeqafile(writefile, question, match2.string)

        dateTimeRegex3 = re.compile('[1-2][0-9]{3}(\s)*-(\s)*[1-2][0-9]{3}')
        match3 = re.search(dateTimeRegex3, sentence)
        if match3:
            question = re.sub(dateTimeRegex3, 'எந்த ஆண்டு தொடக்கம் எந்த ஆண்டு', sentence)
            return writeqafile(writefile, question, match3.string)

        dateTimeRegex4 = re.compile('\d+\s*ஆம்')
        match4 = re.search(dateTimeRegex4, sentence)
        if match4:
            question = re.sub(dateTimeRegex4, 'எத்தனையாம்', sentence)
            return writeqafile(writefile, question, match4.string)

        dateTimeRegex5 = re.compile('\d+\s*(?:ஆவது|வது)')
        match5 = re.search(dateTimeRegex5, sentence)
        if match5:
            question = re.sub(dateTimeRegex5, 'எத்தனையாவது', sentence)
            return writeqafile(writefile, question, match5.string)

        dateTimeRegex6 = re.compile('[1-2][0-9]{3}(\s)')
        match6 = re.search(dateTimeRegex6, sentence)
        if match6:
            return False

        dateTimeRegex7 = re.compile('\d+\s')
        match7 = re.search(dateTimeRegex7, sentence)
        if match7:
            question = re.sub(dateTimeRegex7, 'எத்தனை ', sentence)
            return writeqafile(writefile, question, match7.string)

    return False

def checkgazetteer(sentence, writefile):
     words = sentence.split()
     for wordindex in range(len(words)):
        firstword = words[wordindex]
        namedentitytype, gazetteerval = gazetteersearch(firstword)
        if (namedentitytype != 'None'):
            searchvalparts = gazetteerval.split(" ")
            lastindex = returngazetteerwordlastindex(words, wordindex, searchvalparts)
            namedentity = ''.join(words[wordindex: lastindex])
            prevword = ''.join(words[wordindex-1]) if wordindex != 0 else ''
            nextword = ''.join(words[lastindex]) if wordindex != len(words)-1 else ''
            generatequestion(sentence, namedentity, prevword, nextword, namedentitytype, writefile)

def returnindexoflist(list, item):
    try:
        return list.index(item)
    except ValueError:
        return -1

def gazetteersearch(word):
    for key, value in gazetteers.gazetteerlist.items():
        for val in value:
            partnames = val.split(" ")
            if word in partnames:
                return key, val
    return 'None', 'None'

def returngazetteerwordlastindex(wordlist, index, searchvalparts):
    i = 1
    if len(searchvalparts) > 1:
        while i < len(searchvalparts) - 1:
            if not wordlist[i] == searchvalparts[i]:
                break
            i = i + 1
    return index+i
