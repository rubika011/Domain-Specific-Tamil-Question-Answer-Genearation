import pickle

import joblib
import sklearn_crfsuite
import snowballstemmer
import re

from rippletagger.tagger import Tagger
from sklearn_crfsuite import metrics
from FrontEnd import gazetteers

from FrontEnd import training_data, testing_data

def lookup_search(lookup):
    for key, value in gazetteers.gazetteerlist.items():
        for v in value:
            partnames = v.split(" ")
            if lookup in partnames:
                return key
    return 'None'

def isyearformat(word):
    return (word.isdigit() and (re.match('^[1-2][0-9]{3}[^0-9]*', word) != 'None'))

def checkifordinalnumericword(word):
    return word in gazetteers.previousword.get('ordinal')

def checkprefixword(word):
    if word in gazetteers.previousword.get('location'):
        return 'location'
    if word in gazetteers.previousword.get('country'):
        return 'country'
    if word in gazetteers.previousword.get('org'):
        return 'org'
    if word in gazetteers.previousword.get('time'):
        return 'time'

    return 'None'

def checkifwordendswithcomma(word):
    return word.endswith(',')

def wordisaconjunction(word):
    common_conj_words = ['மற்றும்', 'ஆகிய',  'ஆகியன', 'போன்ற', 'போன்றன', 'போன்றவை', 'ஆகியவை',
                         'என்பன', 'என்பவை', 'ஆகியோர்', 'போன்றோர்']
    return word in common_conj_words

def checkifwordisnumber(word):
    if word.isdigit():
        return True
    for key, value in gazetteers.numbers.items():
        for v in value:
            if word == v:
                return True
    return False

def checkcluewordlist(word, key):
    stemmer = snowballstemmer.stemmer('tamil')
    stemword = stemmer.stemWords(word.split())
    if word in gazetteers.cluewords.get(key) or stemword in gazetteers.cluewords.get(key):
        return True

    return False

def iswordcontainshyphen(word):
    return re.search(r'-', word) != 'None'

def ishyphen(word):
    return word == '-'

def isclueword(word):
    if checkcluewordlist(word, 'city'):
        return 'city'

    elif checkcluewordlist(word, 'country'):
        return 'country'

    elif checkcluewordlist(word, 'continent'):
        return 'continent'

    elif checkcluewordlist(word, 'person'):
        return 'person'

    elif checkcluewordlist(word, 'org'):
        return 'org'

    elif checkcluewordlist(word, 'time'):
        return 'time'

    elif checkcluewordlist(word, 'quantity'):
        return 'quantity'

    elif checkcluewordlist(word, 'troop'):
        return 'troop'

    elif checkcluewordlist(word, 'event'):
        return 'event'

    elif checkcluewordlist(word, 'gpe'):
        return 'gpe'

    elif checkcluewordlist(word, 'gov'):
        return 'gov'

    else:
        return 'None'

def gazettercheck(word):
    return lookup_search(word)

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word[-3:]': word[-3:],
        'isnumber': checkifwordisnumber(word),
        'postag': postag,
        'clueword': isclueword(word),
        'gazetteerword': gazettercheck(word),
        'isordinal': checkifordinalnumericword(word),
        'isyearformat': isyearformat(word),
        'endwithcomma': checkifwordendswithcomma(word),
        'containhyphen': iswordcontainshyphen(word),
        'ishyphen': ishyphen(word)
    }

    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:postag': postag1,
            '-1:clueword': isclueword(word1),
            '-1:isnumber': checkifwordisnumber(word1),
            '-1:gazetteerword': gazettercheck(word1),
            '-1:isordinal': checkifordinalnumericword(word1),
            '-1:isyearformat': isyearformat(word1),
            '-1:isconjunction': wordisaconjunction(word1),
            '-1:endwithcomma': checkifwordendswithcomma(word1),
            '-1:ishyphen': ishyphen(word)
        })
        if i > 1:
            word2 = sent[i-2][0]
            postag2 = sent[i-2][1]
            features.update({
                '-2:postag': postag2,
                '-2:gazetteerword': gazettercheck(word2),
                '-2:isyearformat': isyearformat(word2),
                '-2:clueword': isclueword(word2),
                '-2:endwithcomma': checkifwordendswithcomma(word2)
            })
    else:
        features['BOS'] = True

    if i < len(sent) - 1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:postag': postag1,
            '+1:clueword': isclueword(word1),
            '+1:gazetteerword': gazettercheck(word1),
            '+1:isnumber': checkifwordisnumber(word1),
            '+1:isconjunction': wordisaconjunction(word1),
            '+1:endwithcomma': checkifwordendswithcomma(word1),
            '+1:ishyphen': ishyphen(word)
        })
        if i < len(sent) - 2:
            word2 = sent[i+2][0]
            postag2 = sent[i+2][1]
            features.update({
                '+2:postag': postag2,
                '+2:gazetteerword': gazettercheck(word2),
                '+2:clueword': isclueword(word2),
                '+2:isconjunction': wordisaconjunction(word2),
                '+2:endwithcomma': checkifwordendswithcomma(word2)
            })

    else:
        features['EOS'] = True

    return features

def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]

def trainandtest():
    #nertrainingdatasetfile = open('ner_training_dataset.txt', encoding="utf-8")
    #nertrainingdata = nertrainingdatasetfile.readlines()

    #nertestingdatasetfile = open('ner_testing_dataset.txt', encoding="utf-8")
    #nertestingdata = nertestingdatasetfile.readlines()

    train_sents = training_data.get_training_data()
    test_sents = testing_data.get_testing_data()


    X_train = [sent2features(s) for s in train_sents]
    y_train = [sent2labels(s) for s in train_sents]


    X_test = [sent2features(s) for s in test_sents]
    y_test = [sent2labels(s) for s in test_sents]

    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True,
    )
    crf.fit(X_test, y_test)

    filename = 'crf_model.sav'
    #joblib.dump(crf, filename)
    pickle.dump(crf, open(filename, 'wb'))

    # obtaining metrics such as accuracy, etc. on the train set
    labels = list(crf.classes_)
    labels.remove('O')

    ypred = crf.predict(X_train)
    print('F1 score on the train set = {}\n'.format(
        metrics.flat_f1_score(y_train, ypred, average='weighted', labels=labels)))
    print('Accuracy on the train set = {}\n'.format(metrics.flat_accuracy_score(y_train, ypred)))

    sorted_labels = sorted(
        labels,
        key=lambda name: (name[1:], name[0])
    )
    print('Train set classification report: \n\n{}'.format(metrics.flat_classification_report(
        y_train, ypred, labels=sorted_labels, digits=3
    )))
    # obtaining metrics such as accuracy, etc. on the test set
    ypred = crf.predict(X_test)
    print('F1 score on the test set = {}\n'.format(metrics.flat_f1_score(y_test, ypred,
                                                                         average='weighted', labels=labels)))
    print('Accuracy on the test set = {}\n'.format(metrics.flat_accuracy_score(y_test, ypred)))

    sorted_labels = sorted(
        labels,
        key=lambda name: (name[1:], name[0])
    )
    print('Test set classification report: \n\n{}'.format(metrics.flat_classification_report(y_test, ypred, labels=sorted_labels, digits=3)))

def tagsentence(sentence):
    tagger = Tagger(language='tam')
    postagger = tagger.tag(sentence)
    sentencetaglist = []
    for (word, tag) in postagger:
        sentencetaglist.append((word, tag, 'O'))

    return sentencetaglist

def predictnertag(sentence):
    taggeddata = tagsentence(sentence)
    print(taggeddata)
    features = sent2features(taggeddata)
    #predicted = trainandtest().predict(features)
    #print(predicted)
    #return predicted
