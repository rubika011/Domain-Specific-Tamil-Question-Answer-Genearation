from rippletagger.tagger import Tagger
import rulebased
import snowballstemmer
from polyglot.text import Text

dictionary = {
    'location': ['ரஷ்யா', 'பிரான்ஸ்', 'ஆஸ்திரியா-ஹங்கேரி', 'பல்கேரியா', 'ஐக்கிய அமெரிக்கா',
                 'பிரித்தானியா', 'இத்தாலி', 'ஓட்டோமான்', 'ஜெர்மன்', 'ரோமானியா', 'ஜப்பான்'],

    'person': ['நிக்கோலாஸ் II', 'அலெக்சேய் புருசிலோவ்', 'ஜார்ஜஸ் கிளெமென்சியு', 'ஜோசப் ஜோப்ரே', 'பேர்டினண்ட் ஃபோக்',
               'ராபர்ட் நிவேலே','பிலிப் பெட்டேன்','ஹெர்பேர்ட் எச். அஸ்குயித்', 'டே. லாயிட் ஜார்ஜ்', 'டக்ளஸ் ஹேக்',
               'ஜான் ஜெலிக்கோ', 'விக்டர் இம்மானுவேல் III', 'லுய்கி கடோர்னா', 'ஆர்மண்டோ டயஸ்', 'வூட்ரோ வில்சன்',
               'ஜான் பேர்ஷிங்', 'வின்ஸ்டன் சர்ச்சில்', 'பிராங்க்ளின் டெலானோ ரூஸ்வெல்ட்', 'பேரரசர் ஹிரோஹிட்டோ',
               'அடோல்ஃப் ஹிட்லர்', 'பெனிட்டோ முசோலினி', 'ஜோசப் ஸ்டாலின்', 'டக்ளஸ் மாக்ஆர்தர்', 'டுவைட் ஐசனோவர்',
               'மன்னர் ஜார்ஜ் V']
}

def lookup_search(lookup):
    for key, value in dictionary.items():
        for v in value:
            if lookup in v:
                return key
    return 'None'

def checkanophoricresolution(sentence, firstword, stemword):
    personrefs = ['அவர்', 'அவருக்கு', 'அவரை', 'அவரின்', 'அவரது', 'அவரால்', 'இவர்', 'இவரை', 'இவரது', 'இவரின்',
                  'இவருக்கு', 'அவரால்']
    locationrefs = ['அங்கே', 'இங்கே', 'அங்கு', 'இங்கு']

    return True

def ignorenonsuitablesentence(sentence):
    ignorewordlistfile = open("ignoresentence.txt", encoding="utf-8")
    ignorewordlist = ignorewordlistfile.read().splitlines()

    firstword = sentence.partition(' ')[0]
    if firstword in ignorewordlist:
        return False
    stemmer = snowballstemmer.stemmer('tamil')
    stemWord = stemmer.stemWords(firstword.split())
    if stemWord and stemWord[0] in ignorewordlist:
        return False

    return checkanophoricresolution(sentence,firstword, stemWord)

def processfile(filecontent, filewritepath):
    stopwordsfile = open("stopwords.txt", encoding="utf-8")
    stopwords = stopwordsfile.read().splitlines()

    writefile = open(filewritepath, "w", encoding="utf-8")
    sentences = filecontent.split(".")

    for sentence in sentences:
        sentence = ' '.join(sentence.split())
        issentencesuitable = ignorenonsuitablesentence(sentence)
        if not issentencesuitable:
            continue

        tagger = Tagger(language='tam')
        postagger = tagger.tag(sentence)
        print(sentence)
        print('POS tag', postagger)

        matchFound = rulebased.regex_match_date_time_quantity(sentence, writefile)
        if matchFound:
            continue

        matchFound = rulebased.regex_match_multiple_items(sentence, writefile)
        if matchFound:
            continue

        for (word, tag) in postagger:

            if tag == 'NOUN' and word not in stopwords:

                matchFound = lookup_search(word)
                if matchFound == 'location':
                    question = sentence.replace(word, "எந்த நாட்டில்")
                    rulebased.writeqafile(writefile, question, word)
                    break
                elif matchFound == 'person':
                    question = sentence.replace(word, "யார்")
                    rulebased.writeqafile(writefile, question, word)
                    break

