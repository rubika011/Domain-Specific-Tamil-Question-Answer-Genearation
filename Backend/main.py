#regex match for எந்த, எவை question generation
def regex_match_multiple_items(sentence):
    multipleItemsRegex1 = re.compile('(.*,\s)+.*(?:ஆகிய\s|போன்ற\s)')
    match = re.match(multipleItemsRegex1, sentence)
    if match:
        question = re.sub(multipleItemsRegex1, 'எந்த ', sentence)
        print('question: ' + question + '?')
        return True
    else:
        multipleItemsRegex2 = re.compile('(.*,\s)+.*(?:ஆகியன\s|என்பன\s|போன்றன\s|போன்றவை\s|ஆகியவை\s|என்பவை\s)')
        match2 = re.match(multipleItemsRegex1, sentence)
        if match2:
            question = re.sub(multipleItemsRegex2, 'எவை ', sentence)
            print('question2: ' + question + '?')
            return True

#regex match for எப்போது, எத்தனை question generation
def regex_match_date_time_quantity(sentence):
    dateTimeRegex = re.compile('(கி.பி\s)?[1-2][0-9]{3}\s?(?:இல்)')
    match = re.match(dateTimeRegex, sentence)
    print("line 21")
    if match:
        question = re.sub(dateTimeRegex, 'எந்த வருடம் ', sentence)
        print('question: ' + question + '?')
        return True
    else:
        dateTimeRegex2 = re.compile('[1-2][0-9]{3}\s?(?:ஆம்)')
        match2 = re.match(dateTimeRegex2, sentence)
        print("line 29")
        if match2:
            question = re.sub(dateTimeRegex2, 'எந்த', sentence)
            print('question2: ' + question + '?')
            return True
        else:
            dateTimeRegex3 = re.compile('\d{1,2}\s(?:ஆம் நூற்றாண்)')
            match3 = re.match(dateTimeRegex3, sentence)
            print("line 37")
            if match3:
                question = re.sub(dateTimeRegex3, 'எத்தனையாம் நூற்றாண்', sentence)
                print('question3: ' + question + '?')
                return True

import re

from rippletagger.tagger import Tagger
from tamil.txt2unicode import auto2unicode
import snowballstemmer

tscii = 'C÷u Põ»¨£Sv°À ¤µõßì •u¼¯ |õkPÎ¾® \ÚzöuõøP AvPÍÂÀ'
uni = auto2unicode(tscii)
print(uni)


file = open("SampleDoc.txt", encoding="utf-8")
text = ""
for line in file:
    line = line.rstrip()
    if line:
        text = text + line

stopwordsFile = open("stopwords.txt", encoding="utf-8")
stopWords = stopwordsFile.read().splitlines()
print(stopWords)

sentences = text.split(".")

for sentence in sentences:
    matchFound = regex_match_multiple_items(sentence)
    if (matchFound):
        continue

    matchFound = regex_match_date_time_quantity(sentence)
    if (matchFound):
        continue

    tagger = Tagger(language='tam')
    posTagger = tagger.tag(sentence)
    print(sentence)
    print('POS tag', posTagger)
    for (word, tag) in posTagger:
        if tag == 'NOUN' and word not in stopWords:
            stemmer = snowballstemmer.stemmer('tamil')
            stemWord = stemmer.stemWords(word.split())
            print(stemWord)


#import PyPDF2
#import textract
#import tamil
#import transliterate
#from rippletagger.tagger import Tagger
#INDIC_NLP_RESOURCES=r"C:\Users\ASUS\Desktop\MSC\Research Seminar\indic_nlp_resources-master"

#text = tamil.txt2unicode.auto2unicode("©Ûuß uÚx øPPÍõÀ ö£õ¸ÒPøÍ EØ£zv ö\´ÁuØS¨ £v»õP C¯¢vµ[PøÍ¨ £¯ß£kzv ö£õ¸Ò EØ£zvø¯ ÷©ØöPõshxhß _©õº BÖ u\õ¨uPõ»¨£Sv°À øPzöuõÈÀ ©ØÖ® öuõÈÝm£z xøÓ°À HØ£kzv¯ £õ›¯Ó÷© øPzö Ø ¦µm] GßÖ AøÇUP¨£kQÓx. CøÁ öuõhº£õP C¨ £õhzvÀ UP¨£mkÒÍx. ")
#print(text)
#Export the path to the Indic NLP Resources directory programmatically

#from indicnlp import common
#common.set_resources_path(INDIC_NLP_RESOURCES)

#Initialize the Indic NLP library
#from indicnlp import loader
#loader.load()

#from indicnlp.tokenize import indic_tokenize
#indic_string='अनूप,अनूप?।फोन'
#print('Input String: {}'.format(indic_string))
#print('Tokens: ')
#for t in indic_tokenize.trivial_tokenize(indic_string):
    #print(t)


#file = open("Sample doc tscii.txt", errors='ignore')
#text = ""
#for line in file:
 #   line= line.rstrip()
 #   if line:
  #      text= text + line

#text1 = tamil.tscii.convert_to_unicode("Áµ»õÖ Gß£x CÓ¢u Põ»zvÀ ÁõÌ¢u ©Ûu ö\¯Ø£õkPÒ £ØÔU PØS® £õh©õS®. £À»õ°µ® Á¸h[PÐUS •ßÚµõÚ Áµ »õØøÓU PØS®÷£õx AUPõ»Pmh[PÎÀ AÁºPÒ GÊv øÁzu  h¯[PÐ® AÁºPÎß £À÷ÁÖ BUP[PÐ® QøhUP¨ ö£ÖQßÓÚ. A¢u GÊzuõÁn[PÒ AÀ»x BUP[PÒ ‰»® •ØPõ» ©Ûu ö\¯Ø£õkPÒ £ØÔ¯ uPÁÀPøÍ¨ ö£ØÖUöPõÒÍ •iÁuÚõÀ AøÁ ‰»õuõµ[PÒ GÚ¨£kQßÓÚ. JÆöÁõ¸ Põ»PmhzvØS® E›¯uõPU QøhUP¨ö£Ö® CÆÁõÓõÚ ‰»õuõµ[PÎß ‰»® AUPõ»a \‰Pa `ÇÀ £ØÔ AÔ¢x öPõÒÍ •i²®. CÆÁõÓõÚ ‰»õuõµ[PÎß ‰»® ö£ØÖUöPõÒÐ® uPÁÀPøÍz uºUP Ÿv¯õPU PØS®÷£õx AÆÁU Põ»¨ £SvUPõÚ ©Ûu ÁõÌUøP £ØÔ¯ Áµ»õÖ Pmiö¯Ê¨£¨£kQßÓx. Áµ»õØøÓ PØS®÷£õx uPÁÀPøÍ¨ ö£ØÖU öPõÒÍUTi¯ ‰»õuõµ[PÒ AvPÍ À Põn¨£mh ÷£õv¾® AÁØøÓ Cµsk ÁøP PÍõP¨ ¤›zx ÷|õUP»õ®.")
#print(text1)

#x = text.split(".")
#for t in x:
 #tagger = Tagger(language='tam')
 #posTagger = tagger.tag(t)
 #print('POS tag', posTagger)
 #if posTagger.contains('NOUN'):
 #   print(posTagger, 'with noun')


from polyglot.text import Text

# text = Text('புத்துணர்ச்சியான')
# text.language = "ta"
# print(text.morphemes)



#text = tamil.txt2unicode.auto2unicode("©Ûuß uÚx øPPÍõÀ ö£õ¸ÒPøÍ EØ£zv ö\´ÁuØS¨ £v»õP C¯¢vµ[PøÍ¨ £¯ß£kzv ö£õ¸Ò EØ£zvø¯ ÷©ØöPõshxhß _©õº BÖ u\õ¨uPõ»¨£Sv°À øPzöuõÈÀ ©ØÖ® öuõÈÝm£z xøÓ°À HØ£kzv¯ £õ›¯Ó÷© øPzö Ø ¦µm] GßÖ AøÇUP¨£kQÓx. CøÁ öuõhº£õP C¨ £õhzvÀ UP¨£mkÒÍx. ")
#print(text)

#text = tamil.txt2unicode.tam2unicode("©Ûuß uÚx øPPÍõÀ ö£õ¸ÒPøÍ EØ£zv ö\´ÁuØS¨ £v»õP C¯¢vµ[PøÍ¨ £¯ß£kzv ö£õ¸Ò EØ£zvø¯ ÷©ØöPõshxhß _©õº BÖ u\õ¨uPõ»¨£Sv°À øPzöuõÈÀ ©ØÖ® öuõÈÝm£z xøÓ°À HØ£kzv¯ £õ›¯Ó÷© øPzö Ø ¦µm] GßÖ AøÇUP¨£kQÓx. CøÁ öuõhº£õP C¨ £õhzvÀ UP¨£mkÒÍx. ")
#print(text)

