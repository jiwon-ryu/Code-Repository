# -*- coding: utf8 -*-

import re

# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    return True if user_input.lower() in ['h', 'help'] else False


def is_validated_english_sentence(user_input):
    special_letters = set('_@#$%^&*()-+=[]}{";:|`~' + "'")
    punctuations = set('!?.,')
    if user_input.strip() != '':
        if len(re.findall('\d', user_input)) == 0:
            if len(set(user_input).intersection(special_letters)) == 0:
                if len(set(user_input) - punctuations) != 0:
                    return True
    return False


def is_validated_morse_code(user_input):
    units = {'-', '.', ' '}
    if len(set(user_input) - units) == 0:
        units =  {'-', '.', ' ', 'S'}
        user_input = user_input.strip().replace('  ', 'S').split('S')
        words = []
        for word in user_input:
            word = word.split(' ')
            words += [w for w in word]
        for w in set(words):
            if w not in get_morse_code_dict().values():
                return False
        return True
    return False


def get_cleaned_english_sentence(raw_english_sentence):
    result = re.sub('[!?.,]', '', raw_english_sentence).strip()
    return result


def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    result = [alphabet for alphabet, morse in morse_code_dict.items() if morse == morse_character]
    return result[0]


def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict[english_character]


def decoding_sentence(morse_sentence):
    result = ''
    morse_words_list = morse_sentence.strip().split(' ')
    for i in range(len(morse_words_list)-1):
        if is_validated_morse_code(morse_words_list[i]):
            result += decoding_character(morse_words_list[i])
        elif morse_words_list[i] == '':
            result += ' '
    result += decoding_character(morse_words_list[-1])
    return result


def encoding_sentence(english_sentence):
    word_list = list(get_cleaned_english_sentence(english_sentence).upper())
    result = ''
    for i in range(len(word_list)-1):
        if word_list[i] in get_morse_code_dict().keys():
            result += encoding_character(word_list[i]) + ' '
        elif word_list[i] not in get_morse_code_dict().keys():
            if word_list[i+1] in get_morse_code_dict().keys():
                result += ' '
    result +=  encoding_character(word_list[-1])
    return result.rstrip()


def main():
    print("Morse Code Program!!")
    user_input = 'default'
    while user_input:
        # get valid user input
        user_input = str(input('Input your message(H - Help, 0 - Exit): '))
        while is_validated_english_sentence(user_input) == False and is_validated_morse_code(user_input) == False:
            if user_input == '0':
                user_input = False
                break
            print('Wrong Input')
            user_input = str(input('Input your message(H - Help, 0 - Exit): '))
    
        # return 1) help, 2) encoded result, or 3) decoded result
        if user_input:
            if user_input.lower() in ['h', 'help']:
                print(get_help_message())
            elif is_validated_english_sentence(user_input):
                print(encoding_sentence(user_input))
            else:   
                print(decoding_sentence(user_input))
                
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
