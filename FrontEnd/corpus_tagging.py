import re
from rippletagger.tagger import Tagger

def ner_tagging():
    nertaggingfile = open('ner_tagging_test_data.txt', encoding="utf-8")
    nertaggingsentences = nertaggingfile.read()
    sentences = nertaggingsentences.split(".")
    #sentences = processFile.getlistofsentences(nertaggingsentences)

    writefile = open("ner_testing_dataset.txt", "w", encoding="utf-8")
    nersentencestag = []
    nersentencestagstring = ""
    for sentence in sentences:
        sentence = ' '.join(sentence.split())
        sentence = re.sub('\u200c', '', sentence)
        tagger = Tagger(language='tam')
        postagger = tagger.tag(sentence)
        nertaglist = []
        for (word, tag) in postagger:
            nertaglist.append('({}, {}, {})'.format(word, tag, 'O'))

        nersentencestag.append(nertaglist)
        nersentencestagstring = nersentencestagstring + str(nertaglist) + '\n'

    writefile.write(nersentencestagstring)