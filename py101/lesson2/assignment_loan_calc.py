import json

def messages(message, lang='en'):
    return MESSAGES[lang][message]

with open('loan_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(string):
    print(f'---- {string} ----')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt(messages('welcome'))
while True:
    while True:
        prompt(messages('loan_prompt'))
        loan_amount = float(input())
        if not invalid_number(loan_amount):
            break
        prompt(messages('invalid_prompt'))

    while True:
        prompt(messages('apr'))
        apr = float(input())
        if not invalid_number(apr):
            break
        prompt(messages('invalid_apr'))

    apr = apr * .01

    while True:
        prompt(messages('loan_dur_months'))
        loan_duration = float(input())
        if not invalid_number(loan_duration):
            break
        prompt(messages('invalid_number'))

    monthly_ir = apr / 12
    monthly_pmt = loan_amount * (monthly_ir / (1 - (1 + monthly_ir) ** (-loan_duration)))

    output = round(monthly_pmt, 2)

    prompt(f'{messages('monthly_pmt')} ${output}')

    prompt(messages('another_calc'))
    answer = input()
    if answer and answer[0].lower() != 'y':
        break
