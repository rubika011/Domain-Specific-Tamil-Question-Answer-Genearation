import re
from rippletagger.tagger import Tagger
from indicnlp.tokenize import sentence_tokenize

def ner_tagging():
    nertaggingfile = open('training_data_renaissance.txt', encoding="utf-8")
    nertaggingsentences = nertaggingfile.read()
    sentences = sentence_tokenize.sentence_split(nertaggingsentences, lang='tam')

    writefile = open("ner_training_dataset.txt", mode="a", encoding="utf-8")
    nersentencestag = []
    nersentencestagstring = ""
    for sentence in sentences:
        sentence = ' '.join(sentence.split())
        sentence = re.sub('\u200c', '', sentence)
        tagger = Tagger(language='tam')
        postagger = tagger.tag(sentence)
        nertaglist = []
        for (word, tag) in postagger:
            nertaglist.append((word, tag, 'O'))

        nersentencestag.append(nertaglist)
        nersentencestagstring = nersentencestagstring + str(nertaglist) + ',\n'

    writefile.write(nersentencestagstring)
    writefile.close()

    nertaggingfile = open('testing_data_renaissance.txt', encoding="utf-8")
    nertaggingsentences = nertaggingfile.read()
    sentences = sentence_tokenize.sentence_split(nertaggingsentences, lang='tam')

    writefile = open("ner_testing_dataset.txt", mode="a", encoding="utf-8")
    nersentencestag = []
    nersentencestagstring = ""
    for sentence in sentences:
        sentence = ' '.join(sentence.split())
        sentence = re.sub('\u200c', '', sentence)
        tagger = Tagger(language='tam')
        postagger = tagger.tag(sentence)
        nertaglist = []
        for (word, tag) in postagger:
            nertaglist.append((word, tag, 'O'))

        nersentencestag.append(nertaglist)
        nersentencestagstring = nersentencestagstring + str(nertaglist) + ',\n'

    writefile.write(nersentencestagstring)
    writefile.close()