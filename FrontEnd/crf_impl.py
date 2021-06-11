import sklearn_crfsuite
import snowballstemmer
from sklearn_crfsuite import metrics
from FrontEnd import gazetteers, processFile

from FrontEnd import training_data, testing_data

def checkcluewordlist(word, key):
    stemmer = snowballstemmer.stemmer('tamil')
    stemword = stemmer.stemWords(word.split())
    if word in gazetteers.cluewords.get(key) or stemword in gazetteers.cluewords.get(key):
        return True

    return False

def checkifordinalnumericword(word):
    if word in gazetteers.previousword.get('ordinal'):
        return True
    return False

def gazettercheck(word):
    return processFile.lookup_search(word)

def isclueword(word):
    if checkcluewordlist(word, 'clueword-city'):
        return 'city'

    elif checkcluewordlist(word, 'clueword-country'):
        return 'country'

    elif checkcluewordlist(word, 'clueword-continent'):
        return 'continent'

    elif checkcluewordlist(word, 'clueword-city'):
        return 'city'

    elif checkcluewordlist(word, 'clueword-person'):
        return 'person'

    elif checkcluewordlist(word, 'clueword-org'):
        return 'org'

    elif checkcluewordlist(word, 'clueword-time'):
        return 'time'

    elif checkcluewordlist(word, 'clueword-quantity'):
        return 'quantity'

    elif checkcluewordlist(word, 'clueword-troop'):
        return 'troop'

    elif checkcluewordlist(word, 'clueword-event'):
        return 'event'

    elif checkcluewordlist(word, 'clueword-gpe'):
        return 'gpe'

    else:
        return 'None'

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word[-3:]': word[-3:],
        'isdigit': word.isdigit(),
        'postag': postag,
        'clueword': isclueword(word),
        'gazetteerword': gazettercheck(word),
        'isordinal': checkifordinalnumericword(word)
    }

    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:postag': postag1,
            '-1:clueword': isclueword(word1),
            '-1:isdigit': word1.isdigit(),
            '-1:isordinal': checkifordinalnumericword(word1)
        })
        if i > 1:
            word2 = sent[i - 2][0]
            postag2 = sent[i - 2][1]
            features.update({
                '-2:postag': postag2
            })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:postag': postag1,
            '+1:clueword': isclueword(word1),
            '+1:isdigit': word1.isdigit()
        })
        if i < len(sent) - 2:
            word2 = sent[i + 2][0]
            postag2 = sent[i + 2][1]
            features.update({
                '+2:postag': postag2,
                '+2:clueword': isclueword(word2),
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
        max_iterations=20,
        all_possible_transitions=False,
    )
    crf.fit(X_test, y_test)

    # obtaining metrics such as accuracy, etc. on the train set
    labels = list(crf.classes_)
    #labels.remove('X')

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

    def predict_class_text(self, text):
        sentence = text.split()
        other_label_dataset = self.add_other_label2dataset([sentence])
        postagged_data = self.add_postag2dataset(other_label_dataset)
        features = [self.sent2features(sent) for sent in postagged_data]
        predicted = self.loaded_model.predict(features)
        return predicted
