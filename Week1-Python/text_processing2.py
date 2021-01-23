#######################
# Test Processing II  #
#######################

import re

def digits_to_words(input_string):
    strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = re.findall('\d', input_string)
    if len(digits) == 0:
        return ''
    else:
        answer = []
        for s in digits:
            answer.append(strings[int(s)])
        return ' '.join(answer)


def to_camel_case(underscore_str):
    if '_' not in underscore_str:
        return underscore_str
    string = underscore_str.lower().strip('_')
    count_underscore = string.count('_')
    for i in range(count_underscore):
        string = string[:string.find('_')] + string[string.find('_')+1:].capitalize()
    return string
