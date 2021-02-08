import re

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