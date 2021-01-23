# -*- coding: utf-8 -*-

import random


def get_random_number():
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    if user_input_number.isdigit() == True:
        return True
    else:
        return False


def is_between_100_and_999(user_input_number):
    if int(user_input_number) >= 100 and int(user_input_number) < 1000:
        return True
    else:
        return False
        

def is_duplicated_number(three_digit):
    if len(list(set(list(three_digit)))) == len(list(three_digit)):
        return False
    else:
        return True


def is_validated_number(user_input_number):
    if is_digit(user_input_number) == True:
        if is_between_100_and_999(user_input_number) == True:
            if is_duplicated_number(user_input_number) == False:
                return True
    return False


def get_not_duplicated_three_digit_number():
    random_number_result = get_random_number()
    while is_duplicated_number(str(random_number_result)) == True:
        random_number_result = get_random_number()
    return random_number_result


def get_strikes_or_ball(user_input_number, random_number):
    result = [0, 0]
    for i in range(len(user_input_number)):
        if user_input_number[i] == random_number[i]:
            result[0] += 1
        elif user_input_number[i] in random_number:
            result[1] += 1
    return result

def is_yes(one_more_input):
    if one_more_input.upper() in ['Y', 'YES']:
        return True
    else:
        return False


def is_no(one_more_input):
    if one_more_input.upper() in ['N', 'NO']:
        return True
    else:
        return False


def main():
    play = True
    print('Play Baseball')
    while play:
        # display random number
        user_input = 999
        random_number = str(get_not_duplicated_three_digit_number())
        print('Random Number is : ', random_number)
        
        # get user input and return strikes & balls
        strikes = 0
        while strikes != 3:
            user_input = input('Input guess number : ')
            while is_validated_number(user_input) == False:
                if user_input == '0':
                    play = False
                    break
                print('Wrong Input, Input again')
                user_input = input('Input guess number : ')
            if play == False:
                break
            strikes, balls = get_strikes_or_ball(user_input, random_number)
            print(f'Strikes : {strikes} , Balls : {balls}')
        if play == False:
            break
        
        # get response and decide game restart or end
        response = input('You win, one more(Y/N)?')
        while True:
            if is_yes(response):
                break
            elif is_no(response):
                play = False
                break
            else:
                print('Wrong Input')
                response = input('You win, one more(Y/N)?')
                      
    print('Thank you for using the program')
    print('End of the Game')    


if __name__ == "__main__":
    main()
