import pickle, re

from indicnlp.tokenize import sentence_tokenize
from rippletagger.tagger import Tagger

from FrontEnd.crf_impl import sent2features

def loadmodel():
    #loaded_model = joblib.load('crf_model.sav')
    loaded_model = pickle.load(open('crf_model.sav', 'rb'))
    return loaded_model

def tagsentence(sentences):
    sentencetaglist = []
    for sentence in sentences:
        sentence = ' '.join(sentence.split())
        sentence = re.sub('\u200c', '', sentence)
        tagger = Tagger(language='tam')
        postagger = tagger.tag(sentence)
        sentencetag = []
        for (word, tag) in postagger:
            sentencetag.append((word, tag, 'O'))

        sentencetaglist.append(sentencetag)
    return sentencetaglist

def predictnertag(sentences):
    taggeddata = tagsentence(sentences)
    print(taggeddata)
    features = [sent2features(ts) for ts in taggeddata]
    predicted = loadmodel().predict(features)

    print(predicted)
    return predicted
