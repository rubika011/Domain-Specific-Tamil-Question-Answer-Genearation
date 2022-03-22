import re

from FrontEnd import gazetteers
from FrontEnd.questiongenerator import generate_question, process_gap_fill_question
from FrontEnd.run import write_qa_file


# regex match for எந்த, எவை question generation
def regex_match_multiple_items(sentence, writefile):
    multiple_items_regex1 = re.compile('([^,\s]+,\s)+[^,]+(?:ஆகிய\s|போன்ற\s|ஆகியன\s|என்பன\s|போன்றன\s|போன்றவை\s|ஆகியவை\s|என்பவை)')
    match = re.search(multiple_items_regex1, sentence)
    if match:
        process_gap_fill_question(sentence, match.start(), match.end(), writefile)


# regex match for எப்போது type of question generation
def regex_match_date_time(sentence, writefile):
    date_time_regex = re.compile('(வருடம்\s)*[1-2][0-9]{3}\s*(?:இல்\s|ல்\s)')
    match = re.search(date_time_regex, sentence)
    if match:
        question = re.sub(date_time_regex, 'எந்த வருடம் ', sentence, 1)
        return write_qa_file(writefile, question, match.string)

    date_time_regex2 = re.compile('[1-2][0-9]{3}(\s)*(ஆம்\s(?:வருடம்|ஆண்டு)\s){0,1}[^\s]+\s(மாதம்\s){0,1}[0-3][0-9](\s)*(?:ஆம்|ஆந்|இல்|ல்)(\s(?:திகதி|நாள்|தேதி)){0,1}')
    match2 = re.search(date_time_regex2, sentence)
    if match2:
        question = re.sub(date_time_regex2, 'எந்த வருடம், எந்த மாதம், எத்தனையாம் திகதி', sentence, 1)
        return write_qa_file(writefile, question, match2.string)

    date_time_regex3 = re.compile('[1-2][0-9]{3}(\s)*-(\s)*[1-2][0-9]{3}')
    match3 = re.search(date_time_regex3, sentence)
    if match3:
        question = re.sub(date_time_regex3, 'எந்த ஆண்டு தொடக்கம் எந்த ஆண்டு', sentence, 1)
        return write_qa_file(writefile, question, match3.string)

    date_time_regex3 = re.compile('[1-2][0-9]{3}(\s)*(ஆம்\s(?:வருடம்|ஆண்டு|ஆண்டில்|வருடத்தில்)\s){0,1}')
    match3 = re.search(date_time_regex3, sentence)
    if match3:
        question = re.sub(date_time_regex3, 'எத்தனையாம் ஆண்டு', sentence, 1)
        return write_qa_file(writefile, question, match3.string)

    return False


# regex match for எத்தனை type of question generation
def regex_match_quantity(sentence, writefile):
    date_time_regex = re.compile('[1-2][0-9]{3}(\s)')
    match = re.search(date_time_regex, sentence)
    if match:
        return False

    date_time_regex1 = re.compile('\d+\s*ஆம்|ம்')
    match = re.search(date_time_regex1, sentence)
    if match:
        question = re.sub(date_time_regex1, 'எத்தனையாம்', sentence)
        return write_qa_file(writefile, question, match.string)

    date_time_regex2 = re.compile('\d+\s*(?:ஆவது|வது)')
    match2 = re.search(date_time_regex2, sentence)
    if match2:
        question = re.sub(date_time_regex2, 'எத்தனையாவது', sentence)
        return write_qa_file(writefile, question, match2.string)

    date_time_regex3 = re.compile('\d+%\s')
    match3 = re.search(date_time_regex3, sentence)
    if match3:
        return False

    date_time_regex4 = re.compile('\d+\s')
    match4 = re.search(date_time_regex4, sentence)
    if match4:
        question = re.sub(date_time_regex4, 'எத்தனை ', sentence)
        return write_qa_file(writefile, question, match4.string)

    return False


def check_gazetteer(sentence, writefile):
    words = sentence.split()
    for word_index in range(len(words)):
        first_word = words[word_index]
        named_entity_type, gazetteer_val = gazetteer_search(first_word)
        if named_entity_type != 'None':
            search_val_parts = gazetteer_val.split(" ")
            last_index = return_gazetteer_word_last_index(words, word_index, search_val_parts)
            word = ''.join(words[word_index: last_index])
            prev_word = ''.join(words[word_index - 1]) if word_index != 0 else ''
            next_word = ''.join(words[last_index]) if word_index != len(words) - 1 else ''
            generate_question(sentence, word, prev_word, next_word, named_entity_type, writefile)


def return_list_index(list, item):
    try:
        return list.index(item)
    except ValueError:
        return -1


def gazetteer_search(word):
    for key, value in gazetteers.gazetteer_list.items():
        for val in value:
            part_names = val.split(" ")
            if word in part_names:
                return key, val
    return 'None', 'None'


def return_gazetteer_word_last_index(wordlist, index, search_val_parts):
    i = 1
    if len(search_val_parts) > 1:
        while i < len(search_val_parts) - 1:
            if not wordlist[i] == search_val_parts[i]:
                break
            i = i + 1
    return index + i


def process_single_quote(sentence, writefile):
    single_quote_regex = re.compile(r"'.*'")
    match = re.search(single_quote_regex, sentence)
    if match:
        question = re.sub(single_quote_regex, '________________', sentence)
        return write_qa_file(writefile, question, match.string)

