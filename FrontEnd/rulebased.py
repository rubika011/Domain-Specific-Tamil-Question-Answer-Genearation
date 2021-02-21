import re

def writeqafile(writefile, question, answer):
    writefile.write(question + "?\n")
    print(answer)
    writefile.write(answer + "\r\n")
    return True

#regex match for எந்த, எவை question generation
def regex_match_multiple_items(sentence, writefile):
    multipleItemsRegex1 = re.compile('(.*,\s)+.*(?:ஆகிய\s|போன்ற\s)')
    match = re.match(multipleItemsRegex1, sentence)
    if match:
        question = re.sub(multipleItemsRegex1, 'எந்த ', sentence)
        return writeqafile(writefile, question, match.string)
    else:
        multipleItemsRegex2 = re.compile('(.*,)+.*(?:ஆகியன\s|என்பன\s|போன்றன\s|போன்றவை\s|ஆகியவை\s|என்பவை\s)')
        match2 = re.match(multipleItemsRegex1, sentence)
        if match2:
            question = re.sub(multipleItemsRegex2, 'எவை ', sentence)
            return writeqafile(writefile, question, match.string)

#regex match for எப்போது, எத்தனை type of question generation
def regex_match_date_time_quantity(sentence, writefile):
    dateTimeRegex = re.compile('(வருடம்\s)*[1-2][0-9]{3}\s*(?:இல்\s|ல்\s)')
    match = re.search(dateTimeRegex, sentence)
    if match:
        question = re.sub(dateTimeRegex, 'எந்த வருடம் ', sentence)
        return writeqafile(writefile, question, match.string)
    else:
        dateTimeRegex2 = re.compile('[1-2][0-9]{3}(\s)*(?:ஆம்)')
        match2 = re.search(dateTimeRegex2, sentence)
        if match2:
            question = re.sub(dateTimeRegex2, 'எந்த', sentence)
            return writeqafile(writefile, question, match2.string)
        else:
            dateTimeRegex3 = re.compile('\d{1,2}\s(?:ஆம் நூற்றாண்)')
            match3 = re.search(dateTimeRegex3, sentence)
            if match3:
                question = re.sub(dateTimeRegex3, 'எத்தனையாம் நூற்றாண்', sentence)
                return writeqafile(writefile, question, match3.string)

    return False
