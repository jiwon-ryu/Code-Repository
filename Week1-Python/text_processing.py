#######################
# Test Processing I   #
#######################


def normalize(input_string):
    return ' '.join(input_string.lower().lstrip().rstrip().split())


def no_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for s in input_string:
        if s.lower() in vowels:
            input_string = input_string.replace(s, '')
    return input_string
