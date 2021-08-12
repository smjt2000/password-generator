import string
import random
import os


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


settings = {
    'lower case': True,
    'upper case': True,
    'number': True,
    'symbol': True,
    'space': False,
    'length': 8,
}
def get_password_length(option, default):
    while True:
        user_input = input(f'Enter password length. (Default is {default}) (enter: choose default) : ')

        if user_input == '':
            return default

        if user_input.isdigit():
            password_len = int(user_input)
            if 6 <= password_len <= 30:
                return password_len
            print("Invalid Input.")
            print("password length should be between 6 and 30")
        else:
            print('Invalid input. Please try again')


def get_yes_or_no(option, default):
    while True:
        user_input = input(f'Include {option}?'
                           f' (Default is {default}) (y:Yes, n:No, enter: default) :')

        if user_input == '':
            return default

        if user_input in ('y', 'n'):
            return user_input == 'y'

        print('Invalid Input, Please try again')


def get_settings(settings: dict):
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no(option, default)
        else:
            user_choice = get_password_length(option, default)
        settings[option] = user_choice


def password_generator(settings):
    chars = {
        'upper case': string.ascii_uppercase,
        'lower case': string.ascii_lowercase,
        'number': string.digits,
        'symbol': '({!@#$&*?})',
        'space': ' ',
    }
    selected_type = list(
        filter(lambda option: settings[option] == True, chars))

    final_password = ''
    password_length = settings['length']

    for i in range(password_length):
        char_type = random.choice(selected_type)
        final_password += random.choice(chars[char_type])

    return f'Generated Password: {final_password}'


def ask_to_generate_new_password():
    while True:
        user_answer = input('Regenerate? (y: Yes ,enter: yes, n: No) ')

        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('Invalid input.')
            print('Please try again.')


def password_generator_loop(settings):
    while True:
        print('-'*20)
        print(password_generator(settings))

        if not ask_to_generate_new_password():
            break


def ask_to_change_settings(settings):
    while True:
        for option, default in settings.items():
            print(f"{option} = {default}")

        user_answer = input("Do you want to change settings? (y:Yes, n:No, enter: Yes) ")
        clear()
        if user_answer in ['y', 'n', '']:
            if user_answer in ('y', ''):
                print('-'*5, 'change settings', '-'*5, sep='')
                get_settings(settings)
            break
        else:
            print('Invalid input.')
            print('Please try again.')


def run():
    clear()
    ask_to_change_settings(settings)
    password_generator_loop(settings)


run()
