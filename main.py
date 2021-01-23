from rippletagger.tagger import Tagger

file = open("wikipedia.txt", encoding="utf-8")
text = ""
for line in file:
    line = line.rstrip()
    if line:
        text = text + line

stopwordsFile = open("stopwords.txt", encoding="utf-8")
lines = stopwordsFile.read().splitlines()
print(lines)

words = text.split(".")
for word in words:
 tagger = Tagger(language='tam')
 posTagger = tagger.tag(word)
 print(word)
 print('POS tag', posTagger)
 for (word, tag) in posTagger:
     if tag=='NOUN' and word not in lines:
         print("Noun: " + word)



