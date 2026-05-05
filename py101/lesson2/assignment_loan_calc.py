"""Loan Calculator script.

Prompts user to enter the loan amount, APR, duration in months, and returns the monthly payment"""

import json

def messages(message, lang='en'):
    """returns localized message string from loan_messages.json for the given key"""
    return MESSAGES[lang][message]

with open('loan_messages.json', encoding="utf-8") as file:
    MESSAGES = json.load(file)

def prompt(string):
    """prints trail of hyphens to differentiate between user input and output"""
    print(f"---- {string} ----")

def invalid_number(number_str):
    """return True if number_str is not positive, False otherwise"""
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be greater than 0: {number}")
    except ValueError:
        return True
    return False

prompt(messages('welcome'))

while True:
    while True:
        prompt(messages('loan_prompt'))
        loan_amount = input()
        if not invalid_number(loan_amount):
            break
        prompt(messages('invalid_number'))

    while True:
        prompt(messages('apr'))
        apr = input()
        if not invalid_number(apr):
            break
        prompt(messages('invalid_apr'))

    apr = float(apr) * .01

    while True:
        prompt(messages('loan_dur_months'))
        loan_duration = input()
        if not invalid_number(loan_duration):
            break
        prompt(messages('invalid_number'))

    monthly_ir = apr / 12
    loan_amount = float(loan_amount)
    loan_duration = float(loan_duration)


    monthly_pmt = loan_amount * (monthly_ir / (1 - (1 + monthly_ir) ** (-loan_duration)))

    prompt(f"{messages('monthly_pmt')} ${monthly_pmt:.2f}")

    prompt(messages('another_calc'))
    answer = input()
    if answer and answer[0].lower() not in ('y', 'o', 's'):
        break
