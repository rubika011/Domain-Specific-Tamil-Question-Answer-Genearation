import pickle
import warnings

import sklearn_crfsuite
import snowballstemmer
import csv

from sklearn.model_selection import train_test_split, StratifiedKFold, KFold
from sklearn_crfsuite.metrics import flat_classification_report
from sklearn_crfsuite.metrics import flat_accuracy_score
from sklearn_crfsuite.metrics import flat_f1_score

from FrontEnd import gazetteers
import re

from FrontEnd import training_data, testing_data

def lookup_search(lookup):
    for key, value in gazetteers.gazetteerlist.items():
        for v in value:
            partnames = v.split(" ")
            if lookup in partnames:
                return key
    return 'None'

def isyearformat(word):
    return (re.match('^[1-2][0-9]{3}(?:இல்|ல்|ஆம்|ம்){0,1}', word) != 'None')

def checkifordinalnumericword(word):
    return word in gazetteers.previousword.get('ORDINAL')

def checkprefixword(word):
    if word in gazetteers.previousword.get('LOC'):
        return 'location'
    if word in gazetteers.previousword.get('COU'):
        return 'country'
    if word in gazetteers.previousword.get('ORG'):
        return 'org'
    if word in gazetteers.previousword.get('TIME'):
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

def getstemword(word):
    stemmer = snowballstemmer.stemmer('tamil')
    return stemmer.stemWords(word.split())

def iswordcontainshyphen(word):
    return re.search(r'-', word) != 'None'

def ishyphen(word):
    return word == '-'

def isclueword(word):
    if checkcluewordlist(word, 'CITY'):
        return 'city'

    elif checkcluewordlist(word, 'COU'):
        return 'country'

    elif checkcluewordlist(word, 'CON'):
        return 'continent'

    elif checkcluewordlist(word, 'PER'):
        return 'person'

    elif checkcluewordlist(word, 'ORG'):
        return 'org'

    elif checkcluewordlist(word, 'TIME'):
        return 'time'

    elif checkcluewordlist(word, 'NUM'):
        return 'quantity'

    elif checkcluewordlist(word, 'TRO'):
        return 'troop'

    elif checkcluewordlist(word, 'EVE'):
        return 'event'

    elif checkcluewordlist(word, 'GPE'):
        return 'gpe'

    elif checkcluewordlist(word, 'GOV'):
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
        'word[-2:]': word[-2:],
        'isnumber': checkifwordisnumber(word),
        'postag': postag,
        'clueword': isclueword(word),
        'gazetteerword': gazettercheck(word),
        'isordinal': checkifordinalnumericword(word),
        'isyearformat': isyearformat(word),
        'endwithcomma': checkifwordendswithcomma(word),
        'containhyphen': iswordcontainshyphen(word),
        'ishyphen': ishyphen(word),
        'stemword': getstemword(word)
    }

    if i > 0:
        pword1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word': pword1,
            '-1:postag': postag1,
            '-1:clueword': isclueword(pword1),
            '-1:isnumber': checkifwordisnumber(pword1),
            '-1:gazetteerword': gazettercheck(pword1),
            '-1:isordinal': checkifordinalnumericword(pword1),
            '-1:isyearformat': isyearformat(pword1),
            '-1:isconjunction': wordisaconjunction(pword1),
            '-1:endwithcomma': checkifwordendswithcomma(pword1),
            '-1:prefixword': checkprefixword(pword1),
            '-1:stemword': getstemword(pword1),
            '-1:ishyphen': ishyphen(word),
        })
        if i > 1:
            pword2 = sent[i-2][0]
            postag2 = sent[i-2][1]
            features.update({
                '-2:word': pword2,
                '-2:postag': postag2,
                '-2:gazetteerword': gazettercheck(pword2),
                '-2:isyearformat': isyearformat(pword2),
                '-2:clueword': isclueword(pword2),
                '-2:endwithcomma': checkifwordendswithcomma(pword2)
            })
    else:
        features['BOS'] = True

    if i < len(sent) - 1:
        nword1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word': nword1,
            '+1:postag': postag1,
            '+1:clueword': isclueword(nword1),
            '+1:gazetteerword': gazettercheck(nword1),
            '+1:isnumber': checkifwordisnumber(nword1),
            '+1:isconjunction': wordisaconjunction(nword1),
            '+1:endwithcomma': checkifwordendswithcomma(nword1),
            '+1:ishyphen': ishyphen(word),
            '+1:stemword': getstemword(nword1)
        })
        if i < len(sent) - 2:
            nword2 = sent[i+2][0]
            postag2 = sent[i+2][1]
            features.update({
                '+2:word': nword2,
                '+2:postag': postag2,
                '+2:gazetteerword': gazettercheck(nword2),
                '+2:clueword': isclueword(nword2),
                '+2:isconjunction': wordisaconjunction(nword2),
                '+2:endwithcomma': checkifwordendswithcomma(nword2)
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
    sentences = read_conll_as_list()
    X = [sent2features(sentence) for sentence in sentences]
    y = [sent2labels(sentence) for sentence in sentences]

    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    #stratified_split = StratifiedKFold(n_splits=5)

    #for train_index, test_index in stratified_split.split(X, y):
    #    print("TRAIN:", train_index, "TEST:", test_index)
    #    X_train, X_test = X[train_index], X[test_index]
    #    y_train, y_test = y[train_index], y[test_index]
    str_fold = KFold(n_splits=5)
    # fold = KFold(n_splits=4, random_state=0, shuffle=False)

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=20,
        all_possible_transitions=True,
    )

    for train_index, test_index in str_fold.split(X, y):
        print("TRAIN:", train_index, "TEST:", test_index)

        X_train, X_test = X[int(train_index)], X[int(test_index)]
        y_train, y_test = y[train_index], y[test_index]

        crf.fit(X_train, y_train)

        filename = 'crf_model.sav'
        # joblib.dump(crf, filename)
        pickle.dump(crf, open(filename, 'wb'))

        # obtaining metrics such as accuracy, etc. on the train set
        labels = list(crf.classes_)
        labels.remove('O')
        print(labels)

        # y_pred_train = crf.predict(X_train)
        # print('F1 score on the train set = {}\n'.format(flat_f1_score(y_train, y_pred_train, average='weighted', labels=labels)))
        # print('Accuracy on the train set = {}\n'.format(flat_accuracy_score(y_train, y_pred_train)))
        #
        # sorted_labels = sorted(labels, key=lambda name: (name[1:], name[0]))
        # print('Train set classification report: \n\n{}'.format(flat_classification_report(y_train, y_pred_train, labels=sorted_labels, digits=3)))

        # obtaining metrics such as accuracy, etc. on the test set
        y_pred_test = crf.predict(X_test)
        print('F1 score on the test set = {}\n'.format(flat_f1_score(y_test, y_pred_test, average='weighted', labels=labels)))
        print('Accuracy on the test set = {}\n'.format(flat_accuracy_score(y_test, y_pred_test)))

        with warnings.catch_warnings():
            # ignore all caught warnings
            warnings.filterwarnings("ignore")

        sorted_labels = sorted(labels, key=lambda name: (name[1:], name[0]))
        print('Test set classification report: \n\n{}'.format(flat_classification_report(y_test, y_pred_test, labels=sorted_labels, digits=3)))

def convertToList():
    sentence_list_string = ""
    sentence_list = []
    tag_list = []

    with open("C:\\Users\ASUS\PycharmProjects\QuestionAnswerGeneration\FrontEnd\dataset\\tagged_dataset\\tagged_data.conll",
                        encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            data_tags = csv.reader(line, delimiter='\t')
            tag_list.append(i for i in data_tags)

            if line == '.   PUNCT   O\n':
                sentence_list.append(tag_list)
                sentence_list_string = sentence_list_string + str(tag_list) + ',\n'
                tag_list = []

    return sentence_list_string




def read_conll_as_list():
    with open("C:\\Users\ASUS\PycharmProjects\QuestionAnswerGeneration\FrontEnd\dataset\\tagged_dataset\\tagged_data.conll",
            encoding="utf-8") as file:

        raw_docs = file.read().split('\n\n')
        sentence_list = []
        for doc in raw_docs:
            tags = []
            for line in doc.split('\n'):
                token, pos_tag, ner_tag = line.split('\t')
                tags.append((token, pos_tag, ner_tag))
                print(tags)

            sentence_list.append(tags)
            print(tags)

    return sentence_list